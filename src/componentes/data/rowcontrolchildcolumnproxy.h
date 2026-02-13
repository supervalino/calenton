/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: rowcontrolchildcolumnproxy.h 196 2010-02-26 12:56:17Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/data/rowcontrolchildcolumnproxy.h $
*****************************************************************************/

#ifndef ROWCONTROLCHILDCOLUMNPROXY_H
#define ROWCONTROLCHILDCOLUMNPROXY_H

#include <RowControlChild>
#include <BaseForeignKey>

class RowControlChildColumnProxy : public  BaseForeignKey, public RowControlChild {
private:
	int		_column;
public:
	RowControlChildColumnProxy(RowControl *parent);
	virtual ~RowControlChildColumnProxy();

	virtual void clear() {}
	virtual void revertRow(int /* row */) {}
	virtual void setDb(const QSqlDatabase & /* db */) {}

	virtual int column() const { return _column; }
	virtual void setColumn(int column) { _column = column; }
	};

#endif // ROWCONTROLCHILDCOLUMNPROXY_H


