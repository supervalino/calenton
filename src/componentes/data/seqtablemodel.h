/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: seqtablemodel.h 229 2010-04-23 16:20:45Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/data/seqtablemodel.h $
*****************************************************************************/

#ifndef SEQTABLEMODEL_H
#define SEQTABLEMODEL_H

#include <QSqlRelationalTableModel>
#include <QSqlRecord>
#include <QList>
#include <QStringList>
#include <QSqlField>

#include <BaseForeignKey>

class RowControl;

class SeqTableModel : public QSqlTableModel {
	Q_OBJECT
private:
	struct VirtualColumn {
		QSqlField	field;
		BaseForeignKey	*fk;
		};
	QString				_parentIdField;
	QList<BaseForeignKey *>		_fks;
	QMap<QString, BaseForeignKey *>	_normalFks;
	QList<VirtualColumn>		_virtualColumns;
	bool				_dirty;
	bool				_needsOpControl;
	QList<RowControl *>		_rowControls;
	QSqlRecord			_rec;

	void	applyNormalFK(const QString &name);
	void	applyVirtualColumn(int n);
	void	initialAcceptFK(BaseForeignKey *fk);
	void	setFK(int column, BaseForeignKey *fk);
	void	reapplyFK();
	void	deleteAllRowControls();
	void	deleteAllNormalFK();
	void	deleteAllFK();
	void	reloadMetadataAllControls();
protected:
	QString	databaseErrorMessage(const QSqlError &error);
public:
	static const int OriginalDataRole = Qt::UserRole + 1111;

	SeqTableModel(QObject *parent = nullptr,
		QSqlDatabase db = QSqlDatabase(),
		QString parentIdField = QString());
	virtual ~SeqTableModel();
	
	int	nextVal();
	int	denseNextVal(const QString &table, 
				const QString &column, 
				const QString &condition);
	bool	submitTrans();
	bool	pendingChanges() const;
	
	virtual bool	canErase(int id);
	virtual bool	eraseActive(const QModelIndexList &l);
	
	QList<int>	selectedRows(const QModelIndexList &l);
	QList<int>	getIds(const QModelIndexList &l);
	QList<int>	getIds(const QList<int> &rows);
	int		getId(int row);
	int		getId(const QModelIndexList &l);
	virtual bool	eraseRows(const QModelIndexList &l);
	virtual bool	eraseOneRow(int id, QSqlDatabase db);
	
	QSqlRecord	first(const QString &sql) const;
	virtual void	setParentId(int parentId);
	virtual void	setParentFilter(QString fieldName, int parentId);
	QVariant	getField(int row, QString fieldName);
	QVariant	data(const QModelIndex &item, int role = Qt::DisplayRole) const;
	bool		setData(const QModelIndex &index, const QVariant &value, int role = Qt::EditRole);
	virtual void	setForeignKey(int columnIndex, BaseForeignKey *fk, bool deleteOld = true);
	virtual void	setForeignKey(const QString &columnName, BaseForeignKey *fk, bool deleteOld = true);
	BaseForeignKey	*foreignKey(int columnIndex) const;
	BaseForeignKey	*foreignKey(const QString &columnName) const;
	virtual int	addVirtualColumn(const QString &columnName, BaseForeignKey *fk);
	virtual int	addVirtualColumn(const QSqlField &columnDesc, BaseForeignKey *fk);
	void		clearAllForeignKeys();
	void		clearAllRowControls();
	void		revertRowAllForeignKeys(int row);
	void		revertRowAllRowControls(int row);
	virtual void	addRowControl(RowControl *control);
	const QList<RowControl *> &rowControls() const;
	virtual bool	select();
	virtual void	revertRow(int row);
	virtual void	setTable(const QString &tableName);
	virtual bool	removeRows(int row, int count, const QModelIndex &parent = QModelIndex());

	QSqlRecord	record() const;
	QSqlRecord	record(int row) const;
	bool		setRecord(int row, const QSqlRecord &record);
	bool		insertRecord(int row, const QSqlRecord &record);
	
	virtual QSqlRecord	findRecord(int id);

	static QSqlRecord	executeAndFetchFirst(QSqlQuery &q);
	static QSqlRecord	executeAndFetchFirst(const QString &sql, QSqlDatabase db);
	static bool		exists(QSqlDatabase db, const QString &table, const QString &condition);
	static int		nextVal(const QString &seqName, QSqlDatabase db);
public slots:
	virtual void	calcSeq(QSqlRecord &newRecord);
	virtual void	slotDataChanged(const QModelIndex & topLeft, const QModelIndex & bottomRight);
	virtual void	slotRowsInserted(const QModelIndex &parent, int start, int end);
	virtual void	slotRowsRemoved(const QModelIndex &parent, int start, int end);
	virtual void	revertAll();
	virtual void	revert();
	virtual bool	submitAll();
private slots:	
	void primeInsert(int row, QSqlRecord &record);
	void beforeDelete(int row);
	void beforeInsert(QSqlRecord &record);
	void beforeUpdate(int row, QSqlRecord &record);
protected:
	virtual void installControlHandlers();
	virtual bool deleteRowFromTable(int row);
	virtual bool insertRowIntoTable(const QSqlRecord & values);
	virtual bool updateRowInTable(int row, const QSqlRecord & values);
	};
	
#endif // SEQTABLEMODEL_H
