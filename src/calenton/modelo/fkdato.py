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
# $Id: fkdato.py 226 2010-04-28 12:02:28Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/fkdato.py $
#
##############################################################################

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ts import ForeignKey

class FKDato (ForeignKey):
	def __init__(self, tabla, columna):
		ForeignKey.__init__(self, tabla, columna)
		
	def constructWhere(self, filters):
		key = QString(u'idclasificacion')
		if not filters.has_key(key):
			return ForeignKey.constructWhere(self, filters)
		(idclas, g) = filters[key].toInt()
		if not g:
			return ForeignKey.constructWhere(self, filters)
		f2 = filters.copy()
		del f2[key]
		cond = "idclasificacion in (select * from jerarquia_clasificacion(:idclasificacion))"
		parte = ForeignKey.constructWhere(self, f2)
		if parte.isEmpty():
			return "where " + cond
		return parte + " and " + cond

