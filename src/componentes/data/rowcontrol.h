/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: rowcontrol.h 196 2010-02-26 12:56:17Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/data/rowcontrol.h $
*****************************************************************************/

#ifndef ROWCONTROL_H
#define ROWCONTROL_H

#include <QString>
#include <QSqlDatabase>
#include <QList>
#include <SeqTableModel>

class RowControlChild;

class RowControl {
private:
	QMap<int, RowControlChild *>	_childs;
	int				_nextIndex;
protected:
	SeqTableModel			*_table;
	QSqlDatabase			_db;
public:
	RowControl();
	virtual ~RowControl();

	virtual void clearCache() {}
	virtual void revertRow(int /* row */) {}
	virtual void setDb(const QSqlDatabase &db) { _db = db; }
	QSqlDatabase db() const { return _db; }
	
	virtual void addToTable(SeqTableModel *table) { _table = table; this->setDb(_table->database()); }
	virtual void removeFromTable() { _table = NULL; }
	virtual SeqTableModel *table() { return _table; }
	
	virtual void primeInsert(int /* row */, QSqlRecord & /* r */) {}
	virtual void beforeInsert(QSqlRecord & /* r */) {}
	virtual void beforeUpdate(int /* row */, QSqlRecord & /* r */) {}
	virtual void beforeDelete(int /* row */) {}
	virtual void afterInsert(QSqlRecord & /* r */) {}
	virtual void afterUpdate(int /* row */, QSqlRecord & /* r */) {}
	virtual void afterDelete(int /* row */, QSqlRecord & /* r */) {}
	
	virtual void reloadMetadata() {}

	virtual int appendChild(RowControlChild *child);
	virtual void removeChild(RowControlChild *child);

	RowControlChild		*childByIndex(int n) const;
	int			childCount() const;
	const QMap<int, RowControlChild *>  &childs() const;

	int	nextIndex() { return _nextIndex++; }
	};

#endif // ROWCONTROL_H


