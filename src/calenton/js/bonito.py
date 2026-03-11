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
# $Id: bonito.py 237 2010-04-30 10:33:47Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/js/bonito.py $
#
##############################################################################

from subprocess import *

def ponBonito(entrada):
	p = Popen("indent", shell = True, stdin = PIPE, stdout = PIPE)
	ec = entrada.encode('utf-8')
	(salida, error) = p.communicate(input = ec)
	p.stdin.close()
	p.wait
	return salida.decode('utf-8')
