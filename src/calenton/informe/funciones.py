#!/usr/bin/python
#-*- coding: utf-8 -*-
##############################################################################
#
# CALENTON
# Programa de procesamiento y generación de informes para datos de emisión
# de contaminantes
#
# (C) LITEC, 2009-2010
# (C) Trustserver SL, 2009-2010
# Todos los derechos reservados
#
# $Id: tablelist.py 229 2010-04-28 16:19:09Z picazo $
# $URL: https://ideafix.litec.csic.es/svn/emisiones/trunk/src/calenton/informe/funciones.py $
#
##############################################################################

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtSql import *
from configobj import ConfigObj
from .colores import miColor
import math
import cairo
import pycha.bar
import pycha.stackedbar
import pycha.pie
import pycha.line
try:
    from pychart import *
except ImportError:
    pass  # pychart is not available; pycha is used instead
import sys

def leeConf(nombreDat, obj):
	cfg = {}
	config = ConfigObj(str(nombreDat), encoding='UTF8')
	cfg['descripcion'] = str(config['descripcion'])
	cfg['tipo'] = str(config['tipo'])
	cfg['sql'] = config['sql']
	cfg['filas'] = config['filas']
	cfg['columnas'] = config['columnas']
	try:
		cfg['encabezado'] = config['encabezado']
	except:
		cfg['encabezado'] = ['null'] * 2
	try:
		cfg['factorColumnas'] = config['factor_columnas']
	except:
		if len(cfg['encabezado']) == 0:
			cfg['factorColumnas'] = ['1.']
		else:
			cfg['factorColumnas'] = ['1.'] * (len(cfg['encabezado']) - 1)
	try:
		cfg['columnasNo'] = config['columnas_no']
	except:
		cfg['columnasNo'] = []
	try:
		cfg['decimales'] = int(config['decimales'])
	except:
		cfg['decimales'] = 2
	try:
		cfg['valor_min'] = float(config['valor_minimo'])
	except:
		cfg['valor_min'] = -1
	try:
		cfg['valor_min_grupo'] = float(config['valor_minimo_grupo'])
	except:
		cfg['valor_min_grupo'] = 0.7
#	try:
#		cfg['filtroFilas'] = config['filtro_filas']
#		if not 'fSI' in cfg['filtroFilas'].keys():
#			cfg['filtroFilas']['fSI'] = ''
#		if not 'fNO' in cfg['filtroFilas'].keys():
#			cfg['filtroFilas']['fNO'] = ''
#	except:
#		cfg['filtroFilas']['fSI'] = ''
#		cfg['filtroFilas']['fNO'] = ''
	if obj == 'g':
		cfg['titulo'] = str(config['titulo'])
		cfg['nombreX'] = str(config['nombreX'])
		cfg['nombreY'] = str(config['nombreY'])
		if cfg['tipo'] == 'tarta1':
			cfg['orden'] = config['orden']
			try:
				cfg['rotacion'] = int(config['rotacion'])
			except:
				cfg['rotacion'] = 0
		try:
			cfg['ipcc'] = config['ipcc']
		except:
			cfg['ipcc'] = '0'
		if not cfg['ipcc'] == '0':
			cfg['contaminantes'] = config['contaminantes']
		try:
			cfg['provincia'] = config['provincia']
		except:
			cfg['provincia'] = []

	if obj == 't':
#		cfg['encabezadoList'] = config['encabezado']
		cfg['formato'] = config['formato']
		try:
			cfg['grupos'] = config['grupos']
		except:
			cfg['grupos'] = []
		cfg['sumas'] = config['sumas']
		try:
			cfg['enColor'] = int(config['en_color'])
		except:
			cfg['enColor'] = 0
		try:
			cfg['noCero'] = int(config['no_cero'])
		except:
			cfg['noCero'] = 0
		try:
			cfg['orden'] = int(config['orden'])
		except:
			cfg['orden'] = 0
		try:
			cfg['colorFilas'] = config['color_filas']
		except:
			if cfg['enColor']:
				cfg['colorFilas'] = ['Maroon!40', 'Maroon!20','Maroon!5']
			else:
				cfg['colorFilas'] = []
		if cfg['tipo'] == '2':
			cfg['mFila'] = config['multifila']
		if 'a' in cfg['tipo']:
			try:
				cfg['SNAP'] = config['snap']
			except:
				pass
			try:
				cfg['IPCC'] = config['ipcc']
			except:
				pass
			try:
				cfg['provincia'] = config['provincia']
			except:
				cfg['provincia'] = []


			cfg['sqlFormato'] = config['sql_formato']
			cfg['contaminantes'] = config['contaminantes']
#			cfg['sql'],cfg['filas'] = self.sqlTipoA1(self.tbSNAP, tbContaminantes)
#			tbFontSize = '\\footnotesize'
#			sql_cls2 = "select descripcion from clasificacion where codigo='%s'" % self.tbSNAP
#			q = QSqlQuery(sql_cls2, self.work)
#			q.next()
#			tbNombreGrupoSnap = str(q.value(0) or "")
#			cfg['encabezado'][0] = cfg['']tbNombreGrupoSnap
		if cfg['tipo'] == '1l':
			cfg['ancho'] = config['ancho_tabla']
#			tbColorFilas = config['color_filas']
	return cfg

def dataSetGlobal(cfg, idEscenario, work):
	ds0 = []
	filaSuma = []
	filasSuma = []

	for l2 in cfg['filas']:
		if 'sql' in l2:
			ds1 = dataSetSQL(QSqlQuery(cfg['sql'][l2].replace('_ESCENARIO_', str(idEscenario)), work), cfg)
			if len(ds1) > 0:
				ds0.extend(ds1)
			textoSuma = ''
		if 'gcol' in l2:
			for l3 in range(len(cfg['columnas'][l2])):
				if 'sql' in cfg['columnas'][l2][l3]:
					ds1 = dataSetSQL(QSqlQuery(cfg['sql'][cfg['columnas'][l2][l3]].replace('_ESCENARIO_', str(idEscenario)), work), cfg)
					if len(ds1) > 0:
						uneColumnas(ds0, ds1)
				elif 'sumac' in cfg['columnas'][l2][l3] and len(ds0) > 0:
					sumaCol(ds0)
		elif 'suma' in l2:
			haySuma = True
			# Agrupa registros
			textoSuma = grSumas[l2][0]

	return ds0


def dataSetSQL(q, cfg):
#	reNO = QRegExp(cfg['filtroFilas']['fNO'])
#	reSI = QRegExp(cfg['filtroFilas']['fSI'])
	nCol = q.record().count()
	ds0 = []
	i = 0
	while q.next():
		v = []
		v.append(str(q.value(0) or "")) # la primera celda de la fila es texto
		for j in range(nCol - 1):
			vs_raw = q.value(j + 1)
			vs = str(vs_raw or "")
			try:
				vn = float(vs)
				v.append(vn)
			except (ValueError, TypeError):
				v.append(vs)
#		if cfg['filtroFilas']['fNO'] == '' or v[0].contains(reSI) or not v[0].contains(reNO) :
		ds0.append(v)
		i = i + 1
	return(ds0)

def uneColumnas(ds0, ds1):
	len_ds0 = len(ds0[0])
	len_ds1 = len(ds1[0])
	for i in range(len(ds1)):
		nuevo = True
		for j in range(len(ds0)):
			if ds1[i][0] == ds0[j][0]:
				nuevo = False
				ds0[j][len_ds0:] = ds1[i][1:len_ds1]
				break
		if nuevo:
			f = []
			f.append(ds1[i][0])
			f.extend([0]*(len_ds0 -1))
			f[len_ds0:] = ds1[i][1:len_ds1]
			ds0.append(f)
	for j in range(len(ds0)):
		if len(ds0[j]) < len_ds0 + len_ds1 -1:
			ds0[j][len_ds0:] = [0]*(len_ds1-1)
	return 0

def eliminaColumnas(ds0,lCol):
	ds1 = []
	rn = list(range(len(ds0[0])))
	rn.reverse()
	for i in range(len(ds0)):
		fila = []
		for j in rn:
			if str(j + 1) in lCol:
#				fila.append(ds0[i][j])
				ds0[i].pop(j)
#		ds1.append(fila)
	return ds0

def formatoNumero(f,ndec):
	d0 = round(math.modf(f)[0],ndec)
	d = str(d0).split('.')[1]	# parte decimal
	if (d0 == 1.0):
		f = f + 1
	e = str(math.floor(f)).split('.')[0]				# parte entera
	r = ''
	nsec = list(range(len(e)))
	nsec.reverse()
	j = 0
	for i in nsec:
		if j == 3:
			r = '.' + r
			j = 0
		j = j + 1
		r = e[i] + r
	if ndec > 0:
		r = r + ',' + d
	return r

def dosCifras(a):
	if a < 10:
		b = '0' + str(a)
	else:
		b = str(a)
	return b

def quitaFilasCero(ds):
	rn = list(range(len(ds)))
	rn.reverse()
	for i in rn:
		t = 0.0
		for j in range(len(ds[i]) - 1):
			t = t + ds[i][j + 1]
		if t == 0:
			ds.pop(i)


def sumaCol(ds0):
	len_ds0 = len(ds0[0])
	for i in range(len(ds0)):
		s = 0.0
		for j in range(len_ds0 - 1):
			s = s + ds0[i][j + 1]
		ds0[i].append(s)

def enPorcentaje(ds0):
	ds1 = []
	total = [0] * len(ds0)
	for i in range(len(ds0)):
		for j in range(len(ds0[0]) - 1):
			total[i] = total[i] + ds0[i][j + 1]

	lMenor1 = ''
	pMenor1 = 0
	lPop = []
	for i in range(len(ds0)):
		fila = []
		fila.append(ds0[i][0])
		for j in range(len(ds0[0]) - 1):
			porcentaje = (ds0[i][j + 1] * 100)/ total[i]
			fila.append(porcentaje)
		ds1.append(fila)
	return sorted(ds1, key=lambda d: d[0])


def dsColor(ds0, colores):
	j = 0
	jMax = len(colores)
	for i in range(len(ds0)):
		if j == jMax:
			j = 0
		formato = '\\rowcolor{' + colores[j] + '} ' + ds0[i][0]
		ds0[i][0] = formato
		j = j + 1

def grafPycha(nombreF, ds0, cfg):
	width, height = (500, 400)
	surface = cairo.PSSurface(str(nombreF), width, height)
	surface.set_eps(True)
	ds = (
		('data', [(i,l[1]) for i,l in enumerate(ds0)]),
		)
	c = miColor()
	numCols = len(ds0)
	xticksHide = False
	if 'barrasAc' in cfg['tipo']:
		numCols = len(cfg['encabezado'])
	if 'tarta' in cfg['tipo']:
		xticksHide = True
	options = {
			'legend': {'hide': False},
			'background': {'color': '#f0f0f0'},
		'axis': {
			'x': {
				'ticks': [dict(v=i, label=str(l[0])) for i, l in enumerate(ds0)],
				'label': cfg['nombreX'],
				'rotate': 25,
				'hide': xticksHide
			},
			'y': {
				'tickCount': 4,
				'rotate': 25,
				'label': cfg['nombreY'],
				'tickPrecision': 0
			}
		},
		'background': {
			'chartColor': '#ffeeff',
			'baseColor': '#ffffff',
			'lineColor': '#444444'
		},
		'colorScheme': {
			'name': 'fixed',
			'args': {
#					'initialColor': 'red',
				'colors': c.listaColor('lista2', numCols),
			},
		},
		'legend': {
#				'hide': True,
			'hide': False,
			'position': {'top': 5, 'left': 5},
			},
		'padding': {
			'left': 150,
			'bottom': 55,
		},
		'title': cfg['titulo']
	}

	if 'barrasAc' in cfg['tipo']:
		chart = pycha.stackedbar.StackedVerticalBarChart(surface, options)
		ds = [(str(cfg['encabezado'][j]),[(i,ds0[i][j + 1]) for i in range(len(ds0))])
										for j in range(len(cfg['encabezado']))]
	elif 'barras' in cfg['tipo']:
		chart = pycha.bar.VerticalBarChart(surface, options)
		ds = (
			('data', [(i,l[1]) for i,l in enumerate(ds0)]),
			)
	elif 'tarta' in cfg['tipo']:
		chart = pycha.pie.PieChart(surface, options)
		ds = [(str(l[0]), [[0, l[1]]]) for i,l in enumerate(ds0)]
	elif 'lineas' in cfg['tipo']:
		chart = pycha.line.LineChart(surface, options)
	chart.addDataset(ds)
	chart.render()

def grafPychart(nombreF, ds0, cfg):
	theme.output_file = str(nombreF)
	theme.use_color = True
	theme.default_font_size = 12
	theme.reinitialize()
	can = canvas.init()

#	for i in range(len(ds0)):
#		for j in range(len(ds0[i]) - 1):
#			ds0[i][j + 1] = eval(formatoNumero(ds0[i][j + 1] * eval(cfg['factorColumnas'][0]), cfg['decimales']) )

	if 'tarta' in cfg['tipo']:
		total = 0
		for i in range(len(ds0)):
			total = total + ds0[i][1]

		lMenor1 = ''
		pMenor1 = 0
		lPop = []
#		i_rng = range(len(ds0))
		for i in range(len(ds0)):
			porcentaje = (ds0[i][1] * 100)/ total
			ds0[i].append(porcentaje)
			if porcentaje <= cfg['valor_min']:
				lPop.append(i)
				continue
			if porcentaje < cfg['valor_min_grupo']:
				m = ds0[i]
				lPop.append(i)
				if lMenor1 == '':
					lMenor1 = m[0]
					dMenor1 = m[1]
					pMenor1 = porcentaje
				else:
					lMenor1 = lMenor1 + ' + ' + m[0]
					pMenor1 = pMenor1 + porcentaje
					dMenor1 = dMenor1 + m[1]
				continue
			ds0[i][0] = '%s (%.2f %%)' % (str(ds0[i][0]), porcentaje)
		if not lMenor1 == '':
			if pMenor1 < cfg['valor_min_grupo']:
				dMenor1 = total/150
		#	ds0.append(['%s (%.2f %%)' % (lMenor1, pMenor1), dMenor1, pMenor1])
			ds0.append(['%s (%.2f %%)' % ('Resto ', pMenor1), dMenor1, pMenor1])
		lPop.reverse()
		for i in lPop:
			ds0.pop(i)

		# Cambia el orden de los datos, según el porcentage. Alterna  los índices: 0,n,1,n-1,2,n-2
		ds1 = sorted(ds0, key=lambda d: d[2])
		if 'Alt' in cfg['orden']:
			ds = []
			while len(ds1) > 0:
				if cfg['orden'] == 'Asc':
					ds.append(ds1.pop(0))
				else:
					ds.append(ds1.pop())
				if len(ds1) > 0:
					if cfg['orden'] == 'Asc':
						ds.append(ds1.pop())
					else:
						ds.append(ds1.pop(0))
		elif 'Asc' in cfg['orden']:
			ds = ds1
		elif 'Des' in cfg['orden']:
			ds1.inverse()
			ds = ds1

		ar = area.T(size=(430,300), legend=None, #legend=legend.T(),
		x_grid_style = None, y_grid_style = None)

		plot = pie_plot.T(data=ds, arc_offsets=[5,25,5,25,5,25,5,25],
			shadow = (2, -2, fill_style.gray50),
			label_offset = 40,
#			label_line_style = line_style.black,
			start_angle = cfg['rotacion'],
			arrow_style = arrow.a1)
		ar.add_plot(plot)
		ar.draw(can)
		canvas.close()

	if 'barrasAc' in cfg['tipo']:
		ds = []

		ds1 = enPorcentaje(ds0)
		for i in range(len(ds1)):
			fila = []
			fila.append(str(ds1[i][0]))
			for j in range(len(ds1[0]) - 1):
				fila.append(ds1[i][j + 1])
			ds.append(fila)

		chart_object.set_defaults(area.T, size = (450, 350), y_range = (0, 100),
								  x_coord = category_coord.T(ds, 0))
		chart_object.set_defaults(bar_plot.T, data = ds)

		ar = area.T(legend = legend.T(),
			x_axis=axis.X(label=cfg['nombreX']),
			y_axis=axis.Y(label=cfg['nombreY'], tic_interval=25))
#		bar_plot.fill_styles.reset();
		plot = []
		plot.append(bar_plot.T(label=str(cfg['encabezado'][0]), width=20))
		ar.add_plot(plot[0])
		for i in range(len(cfg['encabezado']) - 1):
			plot.append(bar_plot.T(label=str(cfg['encabezado'][i + 1]), hcol= i + 2, stack_on = plot[i], width=20))
			ar.add_plot(plot[i + 1])
		ar.draw(can)
		canvas.close()

	if 'barrasGr' in cfg['tipo']:
		quitaFilasCero(ds0)
		for i in range(len(ds0)):
			for j in range(len(ds0[i]) - 1):
#				ds0[i][j + 1] = eval(formatoNumero(ds0[i][j + 1] * eval(cfg['factorColumnas'][0]), cfg['decimales']) )
				ds0[i][j + 1] = ds0[i][j + 1] * eval(cfg['factorColumnas'][0])
		ds = []
		nGr = len(cfg['encabezado'])
		ds1 = ds0
		for i in range(len(ds1)):
			fila = []
			fila.append(str(ds1[i][0]))
			for j in range(len(ds1[0]) - 1):
				fila.append(ds1[i][j + 1])
			ds.append(fila)

		chart_object.set_defaults(area.T, size = (450, 350), y_range = (0, None),
								  x_coord = category_coord.T(ds, 0))
		chart_object.set_defaults(bar_plot.T, data = ds)

		ar = area.T(legend = legend.T(),
			x_axis=axis.X(label=cfg['nombreX']),
			y_axis=axis.Y(label=cfg['nombreY'], format="%d"))
#		bar_plot.fill_styles.reset();
		plot = []
		plot.append(bar_plot.T(label=str(cfg['encabezado'][0]), cluster=(0,nGr), width=20))
		ar.add_plot(plot[0])
		for i in range(len(cfg['encabezado']) - 1):
			plot.append(bar_plot.T(label=str(cfg['encabezado'][i + 1]), hcol= i + 2, cluster=(i+1,nGr), width=20))
			ar.add_plot(plot[i + 1])
		ar.draw(can)
		canvas.close()
		pass


	if 'barrasS' in cfg['tipo']:
		quitaFilasCero(ds0)
		for i in range(len(ds0)):
			for j in range(len(ds0[i]) - 1):
				ds0[i][j + 1] = ds0[i][j + 1] * eval(cfg['factorColumnas'][0])
		ds = []
		nGr = len(cfg['encabezado'])
		ds1 = ds0
		for i in range(len(ds1)):
			fila = []
			fila.append(str(ds1[i][0]))
			for j in range(len(ds1[0]) - 1):
				fila.append(ds1[i][j + 1])
			ds.append(fila)

		chart_object.set_defaults(area.T, size = (450, 350), y_range = (0, None),
								  x_coord = category_coord.T(ds, 0))
		chart_object.set_defaults(bar_plot.T, data = ds)

		ar = area.T(legend = legend.T(),
			x_axis=axis.X(label=cfg['nombreX']),
			y_axis=axis.Y(label=cfg['nombreY'], format="%d"))
		plot = []
		plot.append(bar_plot.T(label=str('n'), width=20))
		ar.add_plot(plot[0])
		ar.draw(can)
		canvas.close()

# TABLAS

def principioTablaTex(cfg):
	tColor = ''
	if cfg['enColor']:
		tColor = '\\rowcolor{' + cfg['colorFilas'][0] + '} '

	nCol = len(cfg['encabezado'])
	if cfg['tipo'] == 'a1':
		t = '\\begin{landscape}\n\\begin{center} \\scriptsize\n'
		t = t + '\\topcaption{Emisiones por SNAP. Grupo %s}' % cfg['SNAP']
		t = t + '\\tablefirsthead{ \\toprule '+ encabezado(cfg['tipo'], cfg['encabezado']) + '\\\\ \\toprule}\n'
		t = t + u'\\tablehead{\\multicolumn{%s}{c}{ \\tablename  \\ \\thetable{} -- continúa de la página anterior} \\\\ \\toprule \n' % nCol
		t = t + encabezado(cfg['tipo'], cfg['encabezado']) +' \\\\ \\toprule} \n'
		t = t + u' \\tabletail{\\hline \\multicolumn{%s}{|r|}{{Continúa en la página siguiente}} \\\\ \\hline}\n' %nCol
		t = t + '\\xentrystretch{-.15}\n'
		t = t + ' \\begin{xtabular}{' + cfg['formato'] + '}\n'
#	elif cfg['tipo'] == 'a2':
#		t = '\\begin{center} \\footnotesize\n'
#		t = t + '\\topcaption{%s}' % cfg['descripcion']
#		t = t + '\\tablefirsthead{ \\toprule '+ encabezado(cfg['tipo'], cfg['encabezado']) + '\\\\ \\toprule}\n'
#		t = t + u'\\tablehead{\\multicolumn{%s}{c}{ \\tablename  \\ \\thetable{} -- continúa de la página anterior} \\\\ \\toprule \n' % nCol
#		t = t + encabezado(cfg['tipo'], cfg['encabezado']) +' \\\\ \\toprule} \n'
#		t = t + u' \\tabletail{\\hline \\multicolumn{%s}{|r|}{{Continúa en la página siguiente}} \\\\ \\hline}\n' %nCol
#		t = t + ' \\begin{xtabular}{' + cfg['formato'] + '}\n'
	elif cfg['tipo'] == '1l':
		t = '\\begin{center}\n'
		t = t + '  \\begin{tabulary}{' + cfg['ancho'] + '}{' + cfg['formato'] + '} \\hline\n'
		t = t + tColor + encabezado(cfg['tipo'], cfg['encabezado']) + ' \\\\ \\hline\n'
	else:
		t = '\\begin{center}\n'
		if cfg['tipo'] == 'a2':
			t = t + '\\scriptsize\n'
		t = t + '  \\begin{tabular}{' + cfg['formato'] + '} \\hline\n'
		if not cfg['encabezado'][0] == 'null':
			t = t + tColor + encabezado(cfg['tipo'], cfg['encabezado']) + ' \\\\ \\hline\n'
	return t

def encabezado(tipo, mEncabezadoList):
	mEncabezado = ''
	if tipo == '2':
		mEncabezado += ' \multicolumn{2}{l} '
	mEncabezado += ' { \\bfseries '
	mEncabezado += mEncabezadoList[0]
	mEncabezado += ' } '
	for i in range(len(mEncabezadoList)-1):
		mEncabezado += ' & \\bfseries '
		mEncabezado += mEncabezadoList[i+1]
	return mEncabezado
