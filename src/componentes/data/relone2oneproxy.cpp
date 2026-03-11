/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: relone2oneproxy.cpp 197 2010-03-01 01:04:10Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/data/relone2oneproxy.cpp $");

#include "relone2oneproxy.h"

RelOne2OneProxy::RelOne2OneProxy (
	RelOne2One	*rel
	) :
	RowControlChildColumnProxy(rel)

{
	}

RelOne2OneProxy::~RelOne2OneProxy()

{
	}

bool	RelOne2OneProxy::setValue (
	const QVariant		&value,
	int			row,
	int			column,
	const SeqTableModel	*m
	)

{
	RelOne2One *p = parent();

	return (p != nullptr) ? p->setValue(this, value, row, column, m) : false;
	}

QVariant RelOne2OneProxy::value (
	int			row,
	int			column,
	const SeqTableModel	*m
	)

{
	RelOne2One *p = parent();

	return (p != nullptr) ? p->value(this, row, column, m) : QVariant();
	}

