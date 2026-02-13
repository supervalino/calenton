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
# $Id: mapas.py 363 2010-12-01 18:30:27Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/calculo/mapas.py $
#
##############################################################################

from PyQt4.QtSql import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSvg import *
from qgis.core import *

class Layer:
	def __init__(self, layer, tabla, renderer = None):
		self.layer = layer
		self.tabla = tabla
		self.renderer = renderer
		
	def clear(self):
		self.renderer = None
		self.layer = None
		self.tabla = None
		
	def setRenderer(self, renderer):
		self.layer.setRendererV2(renderer)
		self.layer.setUsingRendererV2(True)
		self.renderer = renderer
		
class Legend:
	def __init__(self, layer):
		self.layer = layer
		self.text = None
		
	def creaText(self):
		if self.text is not None:
			return self.text
		self.text = QTextDocument()
		f = QFont("sans", 8)
		self.text.setDefaultFont(f)
		t = '''
			table { border-style: none }
			tbody { border-style: none }
			tr { border-style: none }
			'''
		self.text.setDefaultStyleSheet(t)
		cursor = QTextCursor(self.text)
		cursor.movePosition(QTextCursor.End)
		ls = self.layer.renderer.legendSymbologyItems(QSize(15, 15))
		tf = QTextTableFormat()
		tf.setBorderStyle(QTextFrameFormat.BorderStyle_None)
		table = cursor.insertTable(len(ls), 2, tf)
		for i in range(len(ls)):
			cell = table.cellAt(i, 0)
			c2 = cell.firstCursorPosition()
			c2.insertImage(ls[i][1].toImage())
			cell = table.cellAt(i, 1)
			c2 = cell.firstCursorPosition()
			c2.insertText(ls[i][0])
		return self.text
		
	def paint(self, painter):
		myHeight = painter.device().height()
		myWidth = painter.device().width()
		text = self.creaText()
		size = text.size()
		myYOffset = myHeight - (size.height() + 5)
		myXOffset = 5
		wm = painter.worldMatrix()
		painter.translate(myXOffset, myYOffset)
		painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
		painter.drawRect(-1, -1, size.width()+2, size.height()+2)
		text.drawContents(painter)
		painter.setWorldMatrix(wm)
	
class Mapas:
	def __init__(self, db, tablaTemporal):
		self.tt = tablaTemporal
		self.db = db
		
	def creaLayer(self, sql, nombre, idnivelzona):
		sql2 = """select z.id as z_id, 
				z.nombre as nombre, 
				m.the_geom as the_geom, 
				coalesce(t.value, 0.0) as value
			from zona z
				inner join mapas m using (id) 
				left outer join	(%s) as t(id, value) using (id)
			where z.idnivelzona = %d
			""" % (sql, idnivelzona)
		t = self.tt.tablaMapa(sql2)
		tp = t.split('.')
		if len(tp) == 1:
			esquema = 'public'
			tabla = tp[0]
		else:
			esquema = tp[0]
			tabla = tp[1]
		uri = QgsDataSourceURI()
		port = "%d" % (self.db.port())
		uri.setConnection(self.db.hostName(), port, self.db.databaseName(), 
				self.db.userName(), self.db.password())
		uri.setDataSource(esquema, tabla, "the_geom")
		layer = QgsVectorLayer(uri.uri(), nombre, "postgres")
		QgsMapLayerRegistry.instance().addMapLayer(layer)
		return Layer(layer, t)
		
	def eliminaLayer(self, layer):
		QgsMapLayerRegistry.instance().removeMapLayer(layer.layer.getLayerID())
		self.tt.quitaTabla(layer.tabla)
		layer.clear()
		
	def consigueBarraColor(self, color):
		if color is None:
			color = 'red-yellow'
		style = QgsStyleV2.defaultStyle()
		colorRamp = style.colorRamp(color)
		return colorRamp
			
	def consigueRenderer(self, layer, color):
		colorRamp = self.consigueBarraColor(color)
		style = QgsStyleV2.defaultStyle()
		numCuantiles = min(10, layer.layer.featureCount())
		if numCuantiles > 1:
			graduatedSymbol = QgsSymbolV2.defaultSymbol(layer.layer.geometryType())
			if numCuantiles > 5:
				mode = QgsGraduatedSymbolRendererV2.Quantile
			else:
				mode = QgsGraduatedSymbolRendererV2.EqualInterval
			renderer = QgsGraduatedSymbolRendererV2.createRenderer(
					layer.layer, 'value', numCuantiles, 
					mode, graduatedSymbol, colorRamp)
		else:
			renderer = None
		return renderer
	
	def layerConfigurada(self, sql, nombre, idNivelZona, color):
		layer = self.creaLayer(sql, nombre, idNivelZona)
		if layer is None:
			return layer
		renderer = self.consigueRenderer(layer, color)
		layer.setRenderer(renderer)
		return layer
		
	def dibujaLayer(self, layer, painter):
		r = QgsMapRenderer()
		r.setLayerSet([ layer.layer.getLayerID() ])
		rect = QgsRect(render.fullExtent())
		rect.scale(1.1)
		render.setExtent(rect)

		render.setOutputSize(img.size(), float(img.size().width()) / 8.0)
		render.render(p)
	
	def dibujaLayerSvg(self, layer, fichero):
		generator = QSvgGenerator()
		generator.setFileName(fichero)
		generator.setSize(QSize(800, 800))
		generator.setViewBox(QRect(0, 0, 800, 800))
		generator.setTitle(tr("SVG Generator Example Drawing"))
		p = QPainter()
		p.begin(generator)
		self.dibujaLayer(layer, p)
		p.end()
	
