/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: rowcontrol.sip 196 2010-02-26 12:56:17Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/rowcontrol.sip $
*****************************************************************************/

class RowControl /Supertype=sip.wrapper/ {

%TypeHeaderCode
#include <RowControl>
%End

public:
	RowControl();
	virtual ~RowControl();

	virtual void clearCache();
	virtual void revertRow(int row);
	virtual void setDb(const QSqlDatabase &db);
	QSqlDatabase db() const;
	
	virtual void addToTable(SeqTableModel *table);
	virtual void removeFromTable();
	virtual SeqTableModel *table();
	
	virtual void primeInsert(int row, QSqlRecord &r);
	virtual void beforeInsert(QSqlRecord &r);
	virtual void beforeUpdate(int row, QSqlRecord &r);
	virtual void beforeDelete(int row);
	virtual void afterInsert(QSqlRecord &r);
	virtual void afterUpdate(int row, QSqlRecord &r);
	virtual void afterDelete(int row, QSqlRecord &r);
	
	virtual void reloadMetadata();
	
	virtual int  appendChild(RowControlChild *child);
	virtual void removeChild(RowControlChild *child);

	RowControlChild		*childByIndex(int n) const;
	int			childCount() const;
	int			nextIndex();
	};
