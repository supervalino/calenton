/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: baseforeignkey.h 197 2010-03-01 01:04:10Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/data/baseforeignkey.h $
*****************************************************************************/

#ifndef BASEFOREIGNKEY_H
#define BASEFOREIGNKEY_H

#include <QString>
#include <QSqlDatabase>
#include <QVariant>

class SeqTableModel;

class BaseForeignKey {
public:
	BaseForeignKey() {}
	virtual ~BaseForeignKey() {}

	virtual bool acceptRole(int role) { return (role == Qt::DisplayRole); }
	virtual bool setterAcceptRole(int /* role */) { return false; }
	virtual bool setValue(const QVariant & /* value */, 
			int /* row */, int /* column */, 
			const SeqTableModel * /* m */) { return false; }
	virtual bool needsUpdateControl() { return false; }
        virtual void setColumn(int /* column */) {}
	virtual QVariant value(int row, int column, const SeqTableModel *m) = 0;
	virtual void clear() = 0;
	virtual void revertRow(int row) = 0;
	virtual void setDb(const QSqlDatabase &db) = 0;
	
	virtual void primeInsert(int /* row */, int /* column */, QSqlRecord & /* r */) {}
	virtual void beforeInsert(int /* column */, QSqlRecord & /* r */) {}
	virtual void beforeUpdate(int /* row */, int /* column */, QSqlRecord & /* r */) {}
	virtual void beforeDelete(int /* row */, int /* column */) {}
	virtual void afterInsert(int /* column */, QSqlRecord & /* r */) {}
	virtual void afterUpdate(int /* row */, int /* column */, QSqlRecord & /* r */) {}
	virtual void afterDelete(int /* row */, int /* column */, QSqlRecord & /* r */) {}
	};

#endif // BASEFOREIGNKEY_H


