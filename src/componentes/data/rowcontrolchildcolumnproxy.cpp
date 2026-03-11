/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: rowcontrolchildcolumnproxy.cpp 196 2010-02-26 12:56:17Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/data/rowcontrolchildcolumnproxy.cpp $");

#include "rowcontrolchildcolumnproxy.h"
#include <SeqTableModel>

RowControlChildColumnProxy::RowControlChildColumnProxy (
	RowControl	*parent
	) :
	BaseForeignKey(),
	RowControlChild(parent),
	_column(-1)
	
{
	}
	
RowControlChildColumnProxy::~RowControlChildColumnProxy()

{
	if (parent() != nullptr) {
		SeqTableModel *t = parent()->table();
		if (t != nullptr)
			t->setForeignKey(_column, nullptr, false);
		}
	}
