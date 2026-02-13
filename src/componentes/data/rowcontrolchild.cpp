/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: rowcontrolchild.cpp 196 2010-02-26 12:56:17Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/data/rowcontrolchild.cpp $");

#include "rowcontrolchild.h"

RowControlChild::RowControlChild (
	RowControl	*parent
	) :
	_parent(parent),
	_index(-1)
	
{
	if (_parent != NULL)
		_parent->appendChild(this);
	}
	
RowControlChild::~RowControlChild()

{
	if (_parent != NULL)
		_parent->removeChild(this);
	}
