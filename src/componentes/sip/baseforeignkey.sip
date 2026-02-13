/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: seqtablemodel.sip 187 2010-02-15 09:41:40Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/seqtablemodel.sip $
*****************************************************************************/

class BaseForeignKey /Supertype=sip.wrapper/ {

%TypeHeaderCode
#include <BaseForeignKey>
%End

public:
	BaseForeignKey();
	virtual ~BaseForeignKey();

	virtual bool acceptRole(int role);
	virtual bool setterAcceptRole(int role);
	virtual bool setValue(const QVariant &value, 
			int row, int column , const SeqTableModel *m);
	virtual bool needsUpdateControl();
	virtual QVariant value(int row, int column, const SeqTableModel *m) = 0;
	virtual void clear() = 0;
	virtual void revertRow(int row) = 0;
	virtual void setDb(const QSqlDatabase &db) = 0;
	
	virtual void primeInsert(int row, int column, QSqlRecord &r);
	virtual void beforeInsert(int column, QSqlRecord &r);
	virtual void beforeUpdate(int row, int column, QSqlRecord &r);
	virtual void beforeDelete(int row, int column);
	virtual void afterInsert(int column, QSqlRecord &r);
	virtual void afterUpdate(int row, int column, QSqlRecord &r);
	virtual void afterDelete(int row, int column, QSqlRecord &r);
	};


