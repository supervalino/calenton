/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: seqtablemodel.sip 229 2010-04-23 16:20:45Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/seqtablemodel.sip $
*****************************************************************************/

class SeqTableModel : QSqlTableModel {

%TypeHeaderCode
#include <SeqTableModel>
%End

protected:
	QString	databaseErrorMessage(const QSqlError &error);
public:
	SeqTableModel(QObject *parent /TransferThis/ = 0, 
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
	
	static QSqlRecord	executeAndFetchFirst(QSqlQuery &q);
	static QSqlRecord	executeAndFetchFirst(const QString &sql, QSqlDatabase db);
	static bool		exists(QSqlDatabase db, const QString &table, const QString &condition);
	static int		nextVal(const QString &seqName, QSqlDatabase db);

	QSqlRecord	first(const QString &sql) const;
	virtual void	setParentId(int parentId);
	virtual void	setParentFilter(QString fieldName, int parentId);
	QVariant	getField(int row, QString fieldName);
	QVariant	data(const QModelIndex &item, int role = Qt::DisplayRole) const;
	bool		setData(const QModelIndex &index, const QVariant &value, int role = Qt::EditRole);
	virtual void	setForeignKey(int columnIndex, BaseForeignKey *fk /Transfer/, bool deleteOld = true);
	virtual void	setForeignKey(const QString &columnName, BaseForeignKey *fk /Transfer/, bool deleteOld = true);
	BaseForeignKey	*foreignKey(int columnIndex) const;
	BaseForeignKey	*foreignKey(const QString &columnName) const;
	virtual int	addVirtualColumn(const QString &columnName, BaseForeignKey *fk /Transfer/);
	virtual int	addVirtualColumn(const QSqlField &columnDesc, BaseForeignKey *fk /Transfer/);
	void		clearAllForeignKeys();
	void		clearAllRowControls();
	void		revertRowAllForeignKeys(int row);
	void		revertRowAllRowControls(int row);
	virtual void	addRowControl(RowControl *control /Transfer/);
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
public slots:
	virtual void	calcSeq(QSqlRecord &newRecord);
	virtual void	slotDataChanged(const QModelIndex &topLeft, const QModelIndex &bottomRight);
	virtual void	revertAll();
	virtual void	revert();
	virtual bool	submitAll();
protected:
	virtual void installControlHandlers();
	virtual bool deleteRowFromTable(int row);
	virtual bool insertRowIntoTable(const QSqlRecord & values);
	virtual bool updateRowInTable(int row, const QSqlRecord & values);
	};
	
