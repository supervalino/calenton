/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: rowcontrolchild.h 196 2010-02-26 12:56:17Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/data/rowcontrolchild.h $
*****************************************************************************/

#ifndef ROWCONTROLCHILD_H
#define ROWCONTROLCHILD_H

#include <RowControl>

class RowControlChild {
private:
	RowControl	*_parent;
	int		_index;
	
	RowControlChild() {}
public:
	RowControlChild(RowControl *parent);
	virtual ~RowControlChild();
	
	RowControl	*parent() const { return _parent; }
	int		index() const { return _index; }
	void		setIndex(int index) { _index = index; }
	};

#endif // ROWCONTROLCHILD_H


