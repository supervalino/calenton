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
# $Id: datalist.py 349 2010-11-03 13:01:09Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/widgets/datalist.py $
#
##############################################################################

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from xml.dom import minidom
from subwindow import SubWindowBase
import types
import tidy

class DataListBase (SubWindowBase):
	def copyDataToClipboard(self, data):
		html = self.dataToHtml(data)
		clip = QApplication.clipboard()
		mimeData = QMimeData()
		mimeData.setHtml(html)
		clip.setMimeData(mimeData)
		
	def findActiveTable(self):
		tab = self.findChild(QTabWidget)
		table = None
		if tab is not None:
			act = tab.currentWidget()
			if act is not None:
				table = act.findChild(QTableView)
		if table is None:
			table = self.findChild(QTableView)
		return table
		
	def dataToHtml(self, data):
		impl = minidom.getDOMImplementation()
		dt = impl.createDocumentType('html', 
				'-//W3C//DTD XHTML 1.0 Strict//EN', 
				'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd')
		doc = impl.createDocument(None, 'html', dt)
		h = doc.documentElement
#		hh = doc.createElement('head')
#		h.appendChild(hh)
#		m = doc.createElement('meta')
#		m.setAttribute('http-equiv', 'Content-Type')
#		m.setAttribute('content', 'text/html; charset=utf-8')
#		hh.appendChild(m)
		b = doc.createElement('body')
		h.appendChild(b)
		t = doc.createElement('table')
		b.appendChild(t)
		tb = doc.createElement('tbody')
		t.appendChild(tb)
		for l in data:
			tr = doc.createElement('tr')
			tb.appendChild(tr)
			for i in l:
				td = doc.createElement('td')
				tr.appendChild(td)
				text = doc.createTextNode(unicode(i))
				td.appendChild(text)
		html = doc.toxml()
		pos = html.find('?>')
		return html[pos + 2:]
		
	@pyqtSlot()
	def copy(self):
		table = self.findActiveTable()
		if table is None:
			return
		model = table.model()
		if model is None:
			return
		sm = table.selectionModel()
		if not sm.hasSelection():
			return
		l = sm.selectedIndexes()
		min_row = 1000000
		max_row = -1
		min_col = 1000000
		max_col = -1
		for i in range(len(l)):
			r = l[i].row()
			c = l[i].column()
			min_row = min(r,  min_row)
			max_row = max(r,  max_row)
			min_col = min(c,  min_col)
			max_col = max(c,  max_col)
		d = []
		for i in range(min_row,  max_row + 1):
			dc = []
			for j in range(min_col,  max_col + 1):
				v = model.data(model.index(i, j))
				if v.type() == QVariant.Double:
					vv = unicode(QString("%L1").arg(v.toDouble()[0], 0, 'f'))
				else:
					vv = unicode(v.toString())
				dc.append(vv)
			d.append(dc)
		self.copyDataToClipboard(d)
		
	def canCopy(self):
		return True
	
class DataList (QWidget, DataListBase):
	def __init__(self, parent = None, flags = Qt.WindowFlags()):
		QWidget.__init__(self, parent, flags)
		
	def askAndRemoveRows(self, view, model):
		l = view.selectionModel().selectedIndexes()
		
		if not model.eraseActive(l):
			return
		res = QMessageBox.question(self, self.tr("¿Está seguro?"),
				self.tr("¿Desea eliminar los registros seleccionados?\n" +
					"Esta operación es permanente e irreversible"),
				QMessageBox.Yes | QMessageBox.Escape,
				QMessageBox.No | QMessageBox.Default)
		if res != QMessageBox.Yes:
			return
			
		if not model.eraseRows(l):
			QMessageBox.warning(self, self.tr("Error al borrar"), 
					self.tr("Se produjo un error: %1").arg(model.lastError().text()),
					QMessageBox.Ok)

	def askAndAddRow(self, r, model):
		model.calcSeq(r)
		if not model.insertRecord(-1, r):
			return 1
		model.submitTrans()
		return 0
			
	def putCombobox(self, combo, model, columna, columna2=''):
		for i in range(model.rowCount()):
			t=model.record(i).value(columna).toString()
			if not columna2=='':
				t = t + " - " + model.record(i).value(columna2).toString()
			n=model.record(i).value('id').toInt()[0]
			combo.addItem(t, n)
		
	def cambiaEncabezado(self, model, lista):
		i=1
		for nombre in lista:
			model.setHeaderData(i, Qt.Horizontal, self.tr(nombre))
			i=i+1
		return
	
	def listActions(self, tabla):
		l = self.children()
		r = []
		for i in l:
			if i.inherits('QAction'):
				r.append(i)
		return r
		
	@pyqtSlot("const QPoint &")
	def showContextMenu(self, point):
		menu = QMenu(self)
		sender = self.sender()
		if sender is None:
			return
		if not sender.inherits('QObject'):
			return
		nombre = unicode(sender.objectName())
		method = nombre + '_contextualMenuActions'
		d = self.__class__.__dict__
		if method in d and type(d[method]) is types.FunctionType:
			l = d[method](self)
		else:
			l = self.listActions(sender)
		if l is None or len(l) == 0:
			return
		for i in l:
			menu.addAction(i)
		if sender.inherits('QAbstractScrollArea'):
			pos = sender.viewport().mapToGlobal(point)
		elif sender.inherits('QWidget'):
			pos = sender.mapToGlobal(point)
		else:
			pos = point
		menu.exec_(pos)
	
	def getDataFromClipboard(self, checked, insertData):
		clip = QApplication.clipboard()
		mimeData = clip.mimeData()
		if (mimeData.hasHtml()):
			html = unicode(mimeData.html())
			data = self.dataFromHtml(html)
			try:
				insertData(data)
			except Exception, e:
				QMessageBox.critical(self, self.tr('Error en insercion'), unicode(e), QMessageBox.Ok)

	@pyqtSlot("bool")
	def dataFromClipboard(self, checked):
		self.getDataFromClipboard(self, checked, self.insertData)
		
	def insertData(self, data):
		pass
	
	def htmlGetEncoding(self, doc):
		l = doc.getElementsByTagName('meta')
		for i in l:
			if i.hasAttribute('http-equiv'):
				if i.getAttribute('http-equiv').upper() == 'CONTENT-TYPE':
					v = i.getAttribute('content')
					p = v.find('charset=')
					if p > 0:
						p = p + 8
						return v[p:].lower()
					break
		return 'ascii'
	
	def elementText(self, el):
		t = u''
		el.normalize()
		n = el.firstChild
		while n is not None:
			if n.nodeType == n.TEXT_NODE:
				t = t + n.wholeText
			elif n.nodeType == n.ELEMENT_NODE:
				t = t + self.elementText(n)
			n = n.nextSibling
		t = unicode(t.encode('iso8859-1', 'ignore'), 'iso8859-1')
		return t
		
	def dataFromHtml(self, html):
		options = dict(output_xhtml=1, add_xml_decl=1, indent=1, tidy_mark=0, char_encoding='utf8')
		html_good = str(tidy.parseString(html.encode('utf8'), **options))
		doc = minidom.parseString(html_good)
		enc = self.htmlGetEncoding(doc)
		if enc != 'utf8' and enc != 'utf-8':
			doc.unlink()
			options = dict(output_xhtml=1, add_xml_decl=1, indent=1, 
						tidy_mark=0, input_encoding=enc, output_enconding='utf8')
			html_good = str(tidy.parseString(html.encode('utf8'), **options))
			doc = minidom.parseString(html_good)
		l = doc.getElementsByTagName('table')
		if len(l) != 1:
			doc.unlink()
			return []
		table = l[0]
		l = table.getElementsByTagName('tbody')
		if len(l) != 1:
			doc.unlink()
			return []
		tbody = l[0]
		r = []
		l = tbody.getElementsByTagName('tr')
		for i in l:
			r1 = []
			l2 = i.getElementsByTagName('td')
			for j in l2:
				j.normalize()
				r1.append(self.elementText(j).strip())
			r.append(r1)
		doc.unlink()
		return r
		
