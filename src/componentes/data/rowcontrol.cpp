/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: rowcontrol.cpp 196 2010-02-26 12:56:17Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/data/rowcontrol.cpp $");

#include "rowcontrol.h"
#include <SeqTableModel>
#include <RowControlChild>

RowControl::RowControl() : 
	_childs(),
	_nextIndex(0)

{
	}
	
RowControl::~RowControl()

{
	this->removeFromTable();
	for (QMap<int, RowControlChild *>::iterator i = _childs.begin(); i != _childs.end(); i = _childs.erase(i)) {
		RowControlChild *c = i.value();
		delete c;
		}
	}

RowControlChild	*RowControl::childByIndex (
	int	n
	) const

{
	return _childs.value(n, NULL);
	}

int	RowControl::childCount() const

{
	return _childs.count();
	}

const QMap<int, RowControlChild *> &RowControl::childs() const

{
	return _childs;
	}

int	RowControl::appendChild (
	RowControlChild	*child
	)

{
	int index = nextIndex();
	_childs[index] = child;
	child->setIndex(index);
	return index;
	}

void	RowControl::removeChild (
	RowControlChild	*child
	)

{
	QList<int> l = _childs.keys(child);
	foreach (int i, l)
		_childs.remove(i);
	}

