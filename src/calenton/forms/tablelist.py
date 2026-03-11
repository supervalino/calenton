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
# $Id: tablelist.py 355 2010-11-17 17:21:58Z picazo $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/tablelist.py $
#
##############################################################################

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtSql import *
from .ui.Ui_tablelist import *
from .tabledlg import TableDlg
from ..widgets.datalist import DataList
from ts import ComboDataModel
from ..informe.funciones import *
#import re
#import cairo
#import pycha.bar
#import pycha.stackedbar
#import pycha.pie
#import pycha.line

from configobj import ConfigObj

#from ts import FKItemDelegate

class TableList (DataList, Ui_TableListClass):
	def __init__(self, parent = None):
		DataList.__init__(self, parent)
		self.setupUi(self)
		self.tabla.selectionModel().selectionChanged.connect(self.tabla_selectionChanged)
		self.work = QSqlDatabase.database('work')
#		self.cambiosSinGuardar = 0
		self.idEscenario = -1
		self.mEscenario = ComboDataModel(self)
		self.mEscenario.setQuery("select id, nombre from escenario order by id", self.work)
		self.escenario.setModel(self.mEscenario)

		self.cargaTabla()

	def cargaTabla(self):
		app = QApplication.instance()
		self.dir = QDir("reports/%s" % (app.informeActivo()))
		self.dir.setNameFilters(["t_*.dat"])
		self.listaF = self.dir.entryList()
		self.n = len(self.listaF)
		self.tabla.setRowCount(self.n)
		self.tabla.setColumnCount(1)
		encabezado = [self.tr("Fichero")]
		#[self.tr("Descripción"), self.tr("SQL")]
		self.tabla.setHorizontalHeaderLabels(encabezado)
		if self.n==0 :
			return
		for i in range(0,self.n):
			nombre=self.listaF[i].split(".")[0]
			self.tabla.setItem(i, 0, QTableWidgetItem(self.listaF[i]))
		self.tabla.resizeColumnsToContents()
		self.tabla.resizeRowsToContents()
		self.elimina.setEnabled(False)
		self.edita.setEnabled(False)
		self.crear.setEnabled(False)
		self.anade.setEnabled(False) # quitar cuando este hecho el dialogo editar

	def filasSeleccionadas(self):
		filas = []
		i = -1
		for g in self.tabla.selectedIndexes():
			filas.append(g.row())
		ln = list(dict.fromkeys(filas))
		ln.sort()
		return ln

	def creaTablaTex(self, i):
		nombre=self.tabla.item(i, 0).text().split(".")[0]
		nombreF=self.dir.filePath(nombre) + ".tex"
		nombreDat=self.dir.filePath(nombre) + ".dat"
		textoF = QFile(nombreF)
		if ( not textoF.open(QIODevice.WriteOnly | QIODevice.Text)):
			return

		config = ConfigObj(str(nombreDat), encoding='UTF8')
		cfg = leeConf(nombreDat, 't')

		if cfg['tipo'] == 'a1':
			cfg['sql'],cfg['filas'] = self.sqlTipoA1(cfg['SNAP'], cfg['contaminantes'])
			cfg['fontSize'] = '\\footnotesize'
			sql_cls2 = "select descripcion from clasificacion where codigo='%s'" % cfg['SNAP']
			q = QSqlQuery(sql_cls2, self.work)
			q.next()
			tbNombreGrupoSnap = str(q.value(0) or "")
			cfg['encabezado'][0] = tbNombreGrupoSnap
		elif cfg['tipo'] == 'a2':
			if cfg['IPCC'] == '0':
				cfg['sql'],cfg['filas'] = self.sqlTipoB(cfg['contaminantes'], cfg['provincia'])
			else:
				sql_cls2 = "select codigo from clasificacion where idtipoclas=4 and codigo~'^%s' order by codigo" % cfg['IPCC']
				q = QSqlQuery(sql_cls2, self.work)
				lista_ipcc = []
				while q.next():
					lista_ipcc.append(str(q.value(0) or ""))
				cfg['sql'],cfg['filas'] = self.sqlTipoB_listaIPCC(lista_ipcc, cfg['contaminantes'], cfg['provincia'])

			cfg['fontSize'] = '\\footnotesize'
#			sql_cls2 = "select descripcion from clasificacion where codigo='%s'" % cfg['SNAP']
#			q = QSqlQuery(sql_cls2, self.work)
#			q.next()
#			tbNombreGrupoSnap = str(q.value(0) or "")
#			cfg['encabezado'][0] = 'Categorías de actividad'
		ds = []
		filaSuma = []
		filasSuma = []
		textoStream=QTextStream(textoF)
		textoStream.setRealNumberNotation(QTextStream.SmartNotation)
		textoStream.setRealNumberPrecision(cfg['decimales'])
		textoStream << principioTablaTex(cfg)
		for k1,  l1 in cfg['filas'].items():
			ds0 = []
			dsGrupos = {}
			haySuma = False
			for l2 in l1:
				if 'sql' in l2:
					ds1 = dataSetSQL(QSqlQuery(cfg['sql'][l2].replace('_ESCENARIO_', str(self.idEscenario)), self.work), cfg)
					if len(ds1) > 0:
						ds0.extend(ds1)
					textoSuma = ''
				if 'gcol' in l2:
					for l3 in range(len(cfg['columnas'][l2])):
						if 'sql' in cfg['columnas'][l2][l3]:
							ds1 = dataSetSQL(QSqlQuery(cfg['sql'][cfg['columnas'][l2][l3]].replace('_ESCENARIO_', str(self.idEscenario)), self.work), cfg)
							if len(ds1) > 0:
								self.uneColumnas(ds0, ds1)
							else:
								for i in range(len(ds0)):
									ds0[i].append(0)
						elif 'sumac' in cfg['columnas'][l2][l3] and len(ds0) > 0:
							sumaCol(ds0)
				elif 'suma' in l2:
					haySuma = True
					textoSuma = cfg['sumas'][l2][0]
			if len(ds0) == 0:
				continue

			if not len(cfg['columnasNo']) == 0:
				eliminaColumnas(ds0,cfg['columnasNo'])

			if cfg['tipo'] == '1' or cfg['tipo'] == '1l' or cfg['tipo'] == '1sc' or cfg['tipo'] == '1f': # Tabla estandar o estandar larga
				if cfg['tipo'] == '1f':
					ds.extend(self.agrupoRegistrosFiltrando(ds0, cfg['grupos']))
				else:
					ds.extend(self.agrupoRegistros(ds0, cfg['grupos']))
				if cfg['enColor']:
					lColor = [cfg['colorFilas'][1], cfg['colorFilas'][2]]
				else:
					lColor = []
				if cfg['orden'] > 0:
					ds1 = sorted(ds, key=lambda d: d[cfg['orden'] -1 ])
					if cfg['orden'] > 1:
						ds1.reverse()
				else:
					ds1 = ds

				self.filasATex(textoStream, ds1, cfg, lColor)
				if haySuma:
					if cfg['enColor']:
						lColor = [cfg['colorFilas'][0]]
					else:
						lColor = []
					textoStream << 	'\\hline\n'
					self.filasATex(textoStream,[self.filaSuma(ds1, textoSuma)], cfg, lColor)
			elif cfg['tipo'] =='2': # Tabla multifila
				ds = (self.agrupoRegistros2(ds0, cfg['grupos'], dsGrupos))
				dsMf = []
				sumaTotal = [0] * len(ds[0])
				g = 0
				for kmf, lmf in cfg['mFila'].items():
					dsMf0 = []
					i = 0
					texto1 = lmf[0]
					nombreGrupo = lmf[2]
					for kgr, lgr in dsGrupos[nombreGrupo].items():
						if i == 0:
							if g != 0:
								txt0 = '\\bottomrule '
							else:
								txt0 = ''
							txt = '%s \multirow{%d}*{%s} & %s' % (txt0, len(dsGrupos[nombreGrupo].keys())
									, texto1
									, lgr[0])
						else:
							txt = ' & %s' % lgr[0]
						lgr[0] = txt
						dsMf0.append(lgr)
						i = i + 1
					g = g + 1
					# suma de subgrupo
					if len(dsMf0) > 1:
						c0 = ''
						if cfg['enColor']:
							c0 = '\\rowcolor{%s} ' % cfg['colorFilas'][1]
						fSuma = self.filaSuma(dsMf0, '\midrule %s Total & %s' % (c0,texto1))
						dsMf0.append(fSuma)
					else:
						fSuma = dsMf0[0]
					dsMf.extend(dsMf0)
					for i_s in range(len(ds[0]) - 1):
						sumaTotal[i_s + 1] = sumaTotal[i_s + 1] + fSuma[i_s + 1]

				self.filasATex(textoStream, dsMf, cfg, [])
				if haySuma:
					textoSumaMf = ' \multicolumn{2}{l}{%s} ' % textoSuma
					textoStream << 	'\\bottomrule\n'
					#self.filasATex(textoStream,[self.filaSuma(dsMf,textoSumaMf, 0.5)], cfg, [])
					sumaTotal[0] = textoSumaMf
					self.filasATex(textoStream,[sumaTotal], cfg, [])
			elif cfg['tipo'] == 'a1': # Tabla anexo A
				ds.extend(ds0)
				# Añade sombreado a las filas cabecera de subgrupo
				import re
				for i in range(len(ds)):
					a = ds[i][0]
					re1 = re.compile(r'^\d\d')
					re2 = re.compile(r'^\d\d \d\d')
					re3 = re.compile(r'^\d\d \d\d \d\d')
					if re3.search(a):
						pass
					elif re2.search(a):
						ds[i][0] = '\\rowcolor{lightgray} ' + ds[i][0]
					else:
						ds[i][0] = '\\rowcolor{gray} ' + ds[i][0]
				self.filasATex(textoStream, ds, cfg, [])
				if haySuma:
					textoStream << 	'\\bottomrule\n'
					self.filasATex(textoStream,[self.filaSuma(ds, textoSuma)], cfg, [])

			elif cfg['tipo'] == 'a2': # Tabla anexo B
				ds.extend(ds0)
				sumaCol(ds)
				nCtes = len(ds[0]) - 1

				# suma ipcc XXX
				sumaN1 = nCtes * [0]
				sumaN2 = nCtes * [0]
				sumaN3 = nCtes * [0]
				rn = list(range(len(ds)))
				rn.reverse()
				import re
				for i in rn:
					a = ds[i][0]
					re1 = re.compile(r'^\d')
					re2 = re.compile(r'^\d[a-z] ')
					re3 = re.compile(r'^\d[a-z]\d ')
					if re3.search(a): # es un grupo nivel 3
						ds[i][0] = '\\hspace{10mm} ' + ds[i][0]
						for j in range(nCtes):
							sumaN3[j] =  sumaN3[j] + ds[i][j + 1]
					elif re2.search(a): # es un grupo nivel 2
						ds[i][0] = '\\hspace{5mm} ' + ds[i][0]
						for j in range(nCtes):
							sumaN2[j] =  sumaN2[j] + ds[i][j + 1] + sumaN3[j]
							ds[i][j + 1] = ds[i][j + 1] + sumaN3[j]
							sumaN3[j] = 0
					else: # grupo nivel 1
						for j in range(nCtes):
							ds[i][j + 1] = ds[i][j + 1] + sumaN2[j]
							sumaN1[j] =  sumaN1[j] + ds[i][j + 1]
							sumaN2[j] = 0
							sumaN3[j] = 0
				if cfg['IPCC'] == '0':
					v = ['\\bottomrule Total']
					for j in range(nCtes):
						v.append(sumaN1[j])
					ds.append(v)
				self.filasATex(textoStream, ds, cfg, [])
				if haySuma:
					textoStream << 	'\\bottomrule\n'
					self.filasATex(textoStream,[self.filaSuma(ds, textoSuma)], cfg, [])

		if 'a1' in cfg['tipo']:
			textoStream << 	'\\bottomrule\n' << '  \\end{xtabular}\n' << '	\\end{center}\n\\end{landscape}\n'
#		elif 'a2' in cfg['tipo']:
#			textoStream << 	'\\bottomrule\n' << '  \\end{xtabular}\n' << '	\\end{center}\n'
		elif cfg['tipo'] == '1l':
			textoStream << 	'\\hline\n' << '  \\end{tabulary}\n' << '	\\end{center}\n'
		else:
			textoStream << 	'\\hline\n' << '  \\end{tabular}\n' << '	\\end{center}\n'


	def filasATex(self, textoStream, ds, cfg, color):
		if cfg['enColor'] and not cfg['tipo'] == '2' :
			dsColor(ds, color)
#		ds = sorted(ds0, key=lambda d: d[cfg['orden']])
		for i in range(len(ds)):
			fila = ds[i]
			textoStream << fila[0]
			for j in range(len(fila)-1):
				valorCelda = formatoNumero(fila[j+1] * eval(cfg['factorColumnas'][j]),cfg['decimales'])
				if cfg['noCero']:
					if fila[j+1] == 0:
						valorCelda = '-'
				textoStream << ' & ' << valorCelda
			textoStream << ' \\\\\n'
		return True

# Agrupa los registros que están definidos en los grupos (sumando los valores), el resto los deja igual
	def agrupoRegistros(self, ds0, grupos):
		ds = {}
		n_l = 0
		for i in range(len(ds0)):
			esGrupo=0
			ds[str(ds0[i][0])] = ds0[i]
			for k0, l0 in grupos.items(): # Recorre todos los grupos
				if esGrupo == 1:
					break
				for i_l in range(len(l0)): # Recorre un grupo
					import re
					re1 = re.compile(l0[i_l])
					if re1.search(ds0[i][0]):
						esGrupo=1
						l1 = [0]*len(ds0[i])
						l1[0] = l0[0]
						for j in range(len(ds0[i]) - 1): # suma los valores de las columnas
							if k0 in ds.keys():
								l1[j+1] = ds[k0][j+1] + ds0[i][j+1]
							else:
								l1[j+1] = ds0[i][j+1]
						ds[k0] = l1
						ds.pop(str(ds0[i][0]))
						break

		# Pasa dict a lista
		ds1 = []
		for i in ds.keys():
			ds1.append(ds[i])
#		ds2 = sorted(ds1, key=lambda d: d[0])
		return ds1

# Agrupa los registros que están definidos en los grupos (sumando los valores), el resto los borra
	def agrupoRegistrosFiltrando(self, ds0, grupos):
		ds = {}
		gKeys = []
		n_l = 0
		for i in range(len(ds0)):
			esGrupo=0
			ds[str(ds0[i][0])] = ds0[i]
			for k0, l0 in grupos.items(): # Recorre todos los grupos
				if esGrupo == 1:
					break
				for i_l in range(len(l0)): # Recorre un grupo
					import re
					re1 = re.compile(l0[i_l])
					if re1.search(ds0[i][0]):
						if not k0 in gKeys:
							gKeys.append(k0)
						esGrupo=1
						l1 = [0]*len(ds0[i])
						l1[0] = l0[0]
						for j in range(len(ds0[i]) - 1): # suma los valores de las columnas
							if k0 in ds.keys():
								l1[j+1] = ds[k0][j+1] + ds0[i][j+1]
							else:
								l1[j+1] = ds0[i][j+1]
						ds[k0] = l1
						ds.pop(str(ds0[i][0]))
						break

		# Pasa dict a lista
		ds1 = []
		for i in gKeys:
			ds1.append(ds[i])
#		ds2 = sorted(ds1, key=lambda d: d[0])
		return ds1

# Agrupa los registros que están definidos en los grupos (sumando los valores), y los que pertenecen
# a un grupo multifila los agrupa en multifila el resto los deja igual
	def agrupoRegistros2(self, ds0, grupos, dsGrupos):
		# dsGrupos = dict del dataset con la estructura de los grupos.
		#			para tipo 2
		ds = {}
		n_l = 0
		for i in range(len(ds0)):
			esGrupo=0
			ds[str(ds0[i][0])] = ds0[i]
			for k0, l0 in grupos.items(): # Recorre todos los grupos
#				dsGrupo = {}
				for k, l in grupos[k0].items():
					if esGrupo == 1:
						break
					for i_l in range(len(l)): # Recorre un grupo
						if ds0[i][0].upper().find(l[i_l].upper()) >= 0:
							esGrupo=1
							l1 = list(range(len(ds0[i])))
							l1[0] = l[0]
							for j in range(len(ds0[i]) - 1): # suma los valores de las columnas
								if k in ds.keys():
									l1[j+1] = ds[k][j+1] + ds0[i][j+1]
								else:
									l1[j+1] = ds0[i][j+1]
							ds[k] = l1
							if not k0 in dsGrupos.keys():
								dsGrupos[k0]={}
							dsGrupos[k0][k] = l1
							ds.pop(str(ds0[i][0]))
							break

		# Pasa dict a lista
		ds1 = []
		for i in sorted(ds.keys()):
			ds1.append(ds[i])
#		ds2 = sorted(ds1, key=lambda d: d[0])
		return ds1

	def filaSuma(self, ds1, nombreSuma, factor=1):
		fSuma = [0]*len(ds1[0])
		for k1 in range(len(ds1)):
			for j_s in range(len(ds1[0])-1):
				fSuma[j_s + 1] = fSuma[j_s + 1] + (ds1[k1][j_s + 1] * factor)
		fSuma[0] = str(nombreSuma)
#		ds1.append(fSuma)
		return fSuma

#
	def uneColumnas(self, ds0, ds1):
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

	def escribeDat(self, d):
		nombre = d.nombre.text().strip()
		nombreDat=self.dir.filePath(nombre) + ".dat"
		config = ConfigObj(str(nombreDat))
		config['titulo'] = d.titulo.text().strip()
		config['nombreX'] = self.tr(d.nombreX.text().strip())
		config['nombreY'] = self.tr(d.nombreY.text().strip())
		if d.barras.isChecked():
			tipo = self.tr("barras")
		elif d.barrasAc.isChecked():
			tipo = self.tr("barrasAc")
		elif d.tarta.isChecked():
			tipo = self.tr("tarta")
		elif d.lineas.isChecked():
			tipo = self.tr("lineas")
		else:
			tipo = barras
		config['tipo'] = tipo
		config['descripcion'] = self.tr(d.descripcion.toPlainText().strip())
		config['sql'] = self.tr(d.sql.toPlainText().strip())
		config.write()
		self.cargaTabla()

	def sqlTipoA1(self, snap, contaminantes):
		sql_cls2 = "select codigo from clasificacion where codigo~'^%s' order by codigo" % snap
		q = QSqlQuery(sql_cls2, self.work)
		snap_v = []
		while q.next():
			snap_v.append(str(q.value(0) or ""))
		fila = []
		filas = {}
		sql_lista = {}
		n=0
		for i in snap_v:
			sqln = 'sql'+ dosCifras(n)
			n = n + 1
			snap_fila = i
			sql_cte = ''
			for cte in contaminantes:
				sql_cte = sql_cte + ''',(select sum(cz.valor)
						FROM contaminantezona cz, contaminante cte, clasificacion cl
						where cz.idfuente in (select id from fuente where idescenario = _ESCENARIO_)
							and cte.id=cz.idcontaminante
							and cl.codigo~'^%s'
							and cl.id=cz.idclasificacion
							and cte.nombre='%s'
						group by cte.nombre)''' % (snap_fila, cte)
			vars()[sqln] = '''select (select codigo || ' ' || descripcion from clasificacion
						where idtipoclas=3
						and codigo='%s') %s
						''' % (snap_fila, sql_cte)
			sql_lista[sqln]= vars()[sqln]
			fila.append(sqln)

		filas['fila1'] = fila
		return sql_lista, filas

	def sqlTipoB(self, contaminantes, lProvincia):
		sql_cls2 = "select codigo from clasificacion where idtipoclas=4 order by codigo"
		q = QSqlQuery(sql_cls2, self.work)
		lista_ipcc = []
		while q.next():
			lista_ipcc.append(str(q.value(0) or ""))
		if len(lProvincia) == 0:
			sql_lista, filas = self.sqlTipoB_listaIPCC(lista_ipcc, contaminantes, [])
		else:
			sql_lista, filas = self.sqlTipoB_listaIPCC_provincia(lista_ipcc, contaminantes, lProvincia[0])
		return sql_lista, filas

	def sqlTipoB_listaIPCC(self, lista_ipcc, contaminantes, lProvincia):
		fila = []
		filas = {}
		sql_lista = {}
		n=0
		if not len(lProvincia) == 0:
			sql_cte = ''' cte.nombre='%s' ''' % contaminantes.pop(0)
			for cte in contaminantes:
				sql_cte = sql_cte + ''' or cte.nombre='%s' ''' % cte
		for i in lista_ipcc:
			sql = ''
			sqln = 'sql'+ dosCifras(n)
			n = n + 1
			ipcc_fila = i
			if not len(lProvincia) == 0:
				for j in lProvincia:
					sql = sql + ''',(select sum(cz.valor * coalesce(ec.p, 0.0))
								FROM contaminantezona cz, contaminante cte, clasificacion cl, equivcontaminante ec
								where cz.idfuente in (select id from fuente where idescenario = _ESCENARIO_)
									and cz.idzona in
										(select idzona from relzona,zona z where
											idzonapadre=z.id and z.nombre='PROVINCIA DE %s')
									and cte.id=cz.idcontaminante
									and ec.idescenario = _ESCENARIO_
									and ec.idcontaminante = cte.id
									and cl.id=cz.idclasificacion
									and cl.id in (select cl.id from clasificacion cl, clasificacion clo, equivclasificacion ecl
													where clo.codigo = '%s'
													and cl.id = ecl.idclasorig
													and clo.id = ecl.idclasmap)
									and (%s) )''' % (j, ipcc_fila, sql_cte)
			else:
				sql_cte = ''
				for cte in contaminantes:
					sql = sql + ''',(select sum(cz.valor * coalesce(ec.p, 0.0))
								FROM contaminantezona cz, contaminante cte, clasificacion cl, equivcontaminante ec
								where cz.idfuente in (select id from fuente where idescenario = _ESCENARIO_)
									and cte.id=cz.idcontaminante
									and ec.idescenario = _ESCENARIO_
									and ec.idcontaminante = cte.id
									and cl.id=cz.idclasificacion
									and cl.id in (select cl.id from clasificacion cl, clasificacion clo, equivclasificacion ecl
													where clo.codigo = '%s'
													and cl.id = ecl.idclasorig
													and clo.id = ecl.idclasmap)
									and cte.nombre='%s' )''' % (ipcc_fila, cte)
			vars()[sqln] = '''select (select codigo || ' ' || descripcion from clasificacion
						where idtipoclas=4
						and codigo='%s') %s
						''' % (ipcc_fila, sql)
			sql_lista[sqln]= vars()[sqln]
			fila.append(sqln)

		filas['fila1'] = fila
		return sql_lista, filas

	def sqlTipoB_listaIPCC_provincia(self, lista_ipcc, contaminantes, provincia):
		fila = []
		filas = {}
		sql_lista = {}
		n=0
		for i in lista_ipcc:
			sql = ''
			sqln = 'sql'+ dosCifras(n)
			n = n + 1
			ipcc_fila = i
			sql_cte = ''
			for cte in contaminantes:
				sql = sql + ''',(select sum(cz.valor * coalesce(ec.p, 0.0))
							FROM contaminantezona cz, contaminante cte, clasificacion cl, equivcontaminante ec
							where cz.idfuente in (select id from fuente where idescenario = _ESCENARIO_)
								and cz.idzona in
									(select idzona from relzona,zona z where
										idzonapadre=z.id and z.nombre='PROVINCIA DE %s')
								and cte.id=cz.idcontaminante
								and ec.idescenario = _ESCENARIO_
								and ec.idcontaminante = cte.id
								and cl.id=cz.idclasificacion
								and cl.id in (select cl.id from clasificacion cl, clasificacion clo, equivclasificacion ecl
												where clo.codigo = '%s'
												and cl.id = ecl.idclasorig
												and clo.id = ecl.idclasmap)
								and cte.nombre='%s' )''' % (provincia, ipcc_fila, cte)
			vars()[sqln] = '''select (select codigo || ' ' || descripcion from clasificacion
						where idtipoclas=4
						and codigo='%s') %s
						''' % (ipcc_fila, sql)
			sql_lista[sqln]= vars()[sqln]
			fila.append(sqln)

		filas['fila1'] = fila
		return sql_lista, filas

	@pyqtSlot(int)
	def on_escenario_activated(self, index):
		self.idEscenario = -1
		ide = self.escenario.currentItemData()
		if ide is not None:
			try:
				self.idEscenario = int(ide)
			except (ValueError, TypeError):
				self.idEscenario = -1

	@pyqtSlot(bool)
	def on_anade_clicked(self, checked):
		d = TableDlg(self)
		if d.exec():
			nombre = d.nombre.text().strip()
			nombreF=self.dir.filePath(nombre) + ".tex"
			nombreDat=self.dir.filePath(nombre) + ".dat"
			F=QFile(nombreF)
			F.open(QFile.WriteOnly)
			F.close()
			self.escribeDat(d)
			self.cargaTabla()

	@pyqtSlot(bool)
	def on_elimina_clicked(self, checked):
		res = QMessageBox.question(self, self.tr("¿Está seguro?"),
				self.tr("¿Desea eliminar los gráficos seleccionados?\n" +
					"Esta operación es permanente e irreversible"),
				QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Escape,
				QMessageBox.StandardButton.No)
		if res != QMessageBox.StandardButton.Yes:
			return
		for i in self.filasSeleccionadas():
			nombre=self.tabla.item(i, 0).text().split(".")[0]
			nombreF=self.dir.filePath(nombre) + ".tex"
			F = QFile(nombreF)
			if not F.remove(nombreF):
				self.cargaTabla()
				return
		self.cargaTabla()


	@pyqtSlot(bool)
	def on_crear_clicked(self, checked):
		if self.idEscenario == -1:
			QMessageBox.warning(None, self.tr("Falta escenario"),
					self.tr("Es necesario primero elegir un escenario"),
					QMessageBox.StandardButton.Ok)
			return False
		for i in self.filasSeleccionadas():
			self.creaTablaTex(i)

	@pyqtSlot(bool)
	def on_crearTodas_clicked(self, checked):
		if self.idEscenario == -1:
			QMessageBox.warning(None, self.tr("Falta escenario"),
					self.tr("Es necesario primero elegir un escenario"),
					QMessageBox.StandardButton.Ok)
			return False
		for i in range(self.n):
			self.creaTablaTex(i)

	@pyqtSlot(QModelIndex)
	def on_tabla_doubleClicked(self, index):
		True
#		i = index.row()
#		nombreBase0 = self.tabla.item(i, 0).text().split(".")[0]
#		nombreDat=self.dir.filePath(nombreBase0) + ".dat"
#		config = ConfigObj(str(nombreDat))
#		d = TableDlg(self)
#		d.nombre.setText(nombreBase0)
#		d.descripcion.setText(config['descripcion'])
#		d.sql.setText(config['sql'])
#		d.titulo.setText(config['titulo'])
#		d.nombreX.setText(config['nombreX'])
#		d.nombreY.setText(config['nombreY'])
#		tipo = config['tipo']
#		if tipo == "barras":
#			d.barras.setChecked(True)
#		if tipo == "barrasAc":
#			d.barrasAc.setChecked(True)
#		if tipo == "tarta":
#			d.tarta.setChecked(True)
#		if tipo == "lineas":
#			d.lineas.setChecked(True)
#		if d.exec():
#			nombreBase = d.nombre.text().strip()
#			nombreF=self.dirGrap.filePath(nombreBase0) + ".tex"
#			nombreDat=self.dirGrap.filePath(nombreBase0) + ".dat"
#			F=QFile(nombreF)
#			F.rename(self.dirGrap.filePath(nombreBase) + ".tex")
#			self.escribeDat(d)
#			self.cargaTabla()

	@pyqtSlot(bool)
	def on_edita_clicked(self, checked):
		l = self.tabla.selectedIndexes()
		if len(self.filasSeleccionadas()) == 1:
			self.on_tabla_doubleClicked(l[0])

	@pyqtSlot(bool)
	def on_recarga_clicked(self, checked):
		self.cargaTabla()

	@pyqtSlot(QItemSelection, QItemSelection)
	def tabla_selectionChanged(self, after, before):
		l = self.filasSeleccionadas()
# descomentar cuando este hecho el dialogo de editar
#		self.elimina.setEnabled(len(l) > 0)
#		self.edita.setEnabled(len(l) == 1)
		self.crear.setEnabled(len(l) > 0)
