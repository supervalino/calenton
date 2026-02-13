/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: relone2one.h 199 2010-03-01 16:51:33Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/data/relone2one.h $
*****************************************************************************/

#ifndef RELONE2ONE_H
#define RELONE2ONE_H

#include <RowControl>
#include <QSqlField>

class RelOne2OneProxy;

class RelOne2One : public RowControl {
private:
	struct ColumnData {
		bool		userColumn;
		QString		origName;
		QString		destName;
		RelOne2OneProxy	*p;
		};

	QMap<int, QSqlRecord>	_cache;
	QString			_relTable;
	int			_idColumn;
	QString			_idColumnName;
	QSqlRecord		_rec;
	QSqlRecord		_tableRec;
	QList<ColumnData>	_columns;
	QMap<QString, int>	_internalColumnNumber;
	QMap<int, int>		_index2InternalColumn;
public:
	RelOne2One(QString idColumnName, QString relTable);
	virtual ~RelOne2One();

	QString	relTable() const { return _relTable; }
	QString idColumnName() const { return _idColumnName; }

	virtual void clearCache();
	virtual void revertRow(int row);
	virtual void addColumn(const QString &fieldName,
			       const QString &destName);
	
	virtual void addToTable(SeqTableModel *table);
	
	virtual bool setValue(const RelOne2OneProxy *p,
				const QVariant &value, int row,
				int column, const SeqTableModel *m);
	virtual QVariant value(const RelOne2OneProxy *p,
			       int row, int column,
			       const SeqTableModel *m);

	virtual void primeInsert(int row, QSqlRecord &r);
	virtual void beforeInsert(QSqlRecord &r);
	virtual void afterUpdate(int row, QSqlRecord &r);
	virtual void afterDelete(int row, QSqlRecord &r);

	virtual void reloadMetadata();
protected:
	int	internalColumn(const QString &origColumnName);
	bool	setCacheValue(int row, int myColumnNumber,
				   const QVariant &value);
	void	addColumnData(const QString &origName, const QString &destName,
			      bool userColumn);
	int	encodeRowInId(int row);
	int	decodeRowFromId(int falseId);
private:
	void	initMetadata();
	void	addColumnToTable(int n);
	bool	ensureLineInCache(int row, int id);
	bool	ensureLineInCache(int row, const SeqTableModel *m);
	QStringList columnNames() const;
	int	insertRowInTable(int row);
	void	deleteRowFromTable(int id);
	bool	updateRowInTable(int row);

	int	getNextId() const;
	};

#endif // RELONE2ONE_H


