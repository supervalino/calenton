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
# $Id: clasitemdelegate.py 103 2010-02-15 10:28:45Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/widgets/clasitemdelegate.py $
#
##############################################################################

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from ts import FKItemDelegate
from ts import ComboDataModel

class Model (ComboDataModel):
	def __init__(self, db, parent = None):
		ComboDataModel.__init__(self, parent)
		self.db = db
		self.idFuente = -1

	def setIdFuente(self, idFuente):
		self.idFuente = idFuente
		sql = """
			select c.id, c.codigo
			from clasificacion c, fuenteclasificacion fc
			where c.id = fc.idclasificacion and
				fc.idfuente = %d
			group by c.id, c.codigo
			order by c.codigo
			""" % (self.idFuente)
		self.setQuery(sql, self.db)

class ClasItemDelegate (FKItemDelegate):
	def __init__(self, parent = None):
		FKItemDelegate.__init__(self, {}, parent)
		self.idFuente = -1

	def filteredModel(self, editor, model, index):
		m = Model(model.database(), editor)
		m.setIdFuente(self.idFuente)
		return m

	def setIdFuente(self, idFuente):
		self.idFuente = idFuente
