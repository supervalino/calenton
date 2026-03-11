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

from PyQt6.QtSql import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtSvg import *
from qgis.core import QgsApplication, QgsProject, QgsVectorLayer, QgsDataSourceUri, QgsStyle, QgsSymbol, QgsGraduatedSymbolRenderer, QgsRectangle

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
		self.layer.setRenderer(renderer)
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
		cursor.movePosition(QTextCursor.MoveOperation.End)
		ls = self.layer.renderer().legendSymbolItems()
		tf = QTextTableFormat()
		tf.setBorderStyle(QTextFrameFormat.BorderStyle_None)
		table = cursor.insertTable(len(ls), 2, tf)
		for i in range(len(ls)):
			cell = table.cellAt(i, 0)
			c2 = cell.firstCursorPosition()
			c2.insertImage(ls[i].symbol().asImage(QSize(15, 15)))
			cell = table.cellAt(i, 1)
			c2 = cell.firstCursorPosition()
			c2.insertText(ls[i].label())
		return self.text

	def paint(self, painter):
		myHeight = painter.device().height()
		myWidth = painter.device().width()
		text = self.creaText()
		size = text.size()
		myYOffset = myHeight - (size.height() + 5)
		myXOffset = 5
		wm = painter.worldTransform()
		painter.translate(myXOffset, myYOffset)
		painter.setBrush(QBrush(Qt.GlobalColor.white, Qt.BrushStyle.SolidPattern))
		painter.drawRect(-1, -1, size.width()+2, size.height()+2)
		text.drawContents(painter)
		painter.setWorldTransform(wm)

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
		uri = QgsDataSourceUri()
		port = "%d" % (self.db.port())
		uri.setConnection(self.db.hostName(), port, self.db.databaseName(),
				self.db.userName(), self.db.password())
		uri.setDataSource(esquema, tabla, "the_geom")
		layer = QgsVectorLayer(uri.uri(), nombre, "postgres")
		QgsProject.instance().addMapLayer(layer)
		return Layer(layer, t)

	def eliminaLayer(self, layer):
		QgsProject.instance().removeMapLayer(layer.layer.id())
		self.tt.quitaTabla(layer.tabla)
		layer.clear()

	def consigueBarraColor(self, color):
		if color is None:
			color = 'red-yellow'
		style = QgsStyle.defaultStyle()
		colorRamp = style.colorRamp(color)
		return colorRamp

	def consigueRenderer(self, layer, color):
		colorRamp = self.consigueBarraColor(color)
		style = QgsStyle.defaultStyle()
		numCuantiles = min(10, layer.layer.featureCount())
		if numCuantiles > 1:
			graduatedSymbol = QgsSymbol.defaultSymbol(layer.layer.geometryType())
			if numCuantiles > 5:
				mode = QgsGraduatedSymbolRenderer.Mode.Quantile
			else:
				mode = QgsGraduatedSymbolRenderer.Mode.EqualInterval
			renderer = QgsGraduatedSymbolRenderer.createRenderer(
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
		from qgis.core import QgsMapSettings, QgsMapRendererParallelJob
		settings = QgsMapSettings()
		settings.setLayers([layer.layer])
		rect = QgsRectangle(layer.layer.extent())
		rect.scale(1.1)
		settings.setExtent(rect)
		settings.setOutputSize(painter.device().size())
		job = QgsMapRendererParallelJob(settings)
		job.start()
		job.waitForFinished()
		img = job.renderedImage()
		painter.drawImage(0, 0, img)

	def dibujaLayerSvg(self, layer, fichero):
		generator = QSvgGenerator()
		generator.setFileName(fichero)
		generator.setSize(QSize(800, 800))
		generator.setViewBox(QRect(0, 0, 800, 800))
		generator.setTitle(self.tr("SVG Generator Example Drawing"))
		p = QPainter()
		p.begin(generator)
		self.dibujaLayer(layer, p)
		p.end()

