/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: relone2oneproxy.h 198 2010-03-01 02:41:05Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/data/relone2oneproxy.h $
*****************************************************************************/

#ifndef RELONE2ONEPROXY_H
#define RELONE2ONEPROXY_H

#include <BaseForeignKey>
#include <RelOne2One>
#include <RowControlChild>
#include <RowControlChildColumnProxy>

class RelOne2OneProxy : public RowControlChildColumnProxy {
public:
	RelOne2OneProxy(RelOne2One *rel);
	virtual ~RelOne2OneProxy();

	virtual bool acceptRole(int role) {
			return ((role == Qt::DisplayRole) ||
				(role == Qt::EditRole)); }
	virtual bool setterAcceptRole(int /* role */) { return true; }
	virtual bool setValue(const QVariant & value, int row, 
				int column, const SeqTableModel *m);
	virtual bool needsUpdateControl() { return true; }
	virtual QVariant value(int row, int column, const SeqTableModel *m);
	
	virtual RelOne2One *parent() { return dynamic_cast<RelOne2One *>(RowControlChildColumnProxy::parent()); }
	};

#endif // RELONE2ONEPROXY_H


