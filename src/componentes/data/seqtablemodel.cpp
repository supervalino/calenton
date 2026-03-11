/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: seqtablemodel.cpp 229 2010-04-23 16:20:45Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/data/seqtablemodel.cpp $");

#include "seqtablemodel.h"
#include <QtSql>
#include <RowControl>

/*!
    \class SeqTableModel seqtablemodel.h
    \brief Modelo de datos básico para todas las tablas maestras.

    Encapsula la funcionalidad común necesaria para el manejo de todas las
    tablas, tiene en cuenta algunos criterios que se han utilizado en
    el diseño de todo el modelo de datos.

    \list

    \li La clave primaria está siempre en una columna con nombre "id".
    
    \li Cada tabla con nombre tabla tiene asociada una secuencia con
        nombre seq_tabla.  La secuencia se representa con un sequence
        en PostgreSQL y una columna de una tabla en SQLite.

    \li Existe una única tabla maestra.

    \endlist
 */

/*!
    Construye el modelo de una tabla con padre \a parent, en la base de datos
    \a db y relacionado con la tabla maestra mediante la columna
    \a parentIdField
 */
 
SeqTableModel::SeqTableModel(
	QObject		*parent,
	QSqlDatabase	db,
	QString		parentIdField
	) :
	QSqlTableModel(parent, db),
	_parentIdField(parentIdField),
	_fks(),
	_normalFks(),
	_virtualColumns(),
	_dirty(false),
	_needsOpControl(false),
	_rowControls(),
	_rec()
	
{
	_rec = QSqlTableModel::record();
	connect(this, &SeqTableModel::beforeInsert, this, &SeqTableModel::calcSeq);
	connect(this, &SeqTableModel::dataChanged,
			this, &SeqTableModel::slotDataChanged);
	connect(this, &SeqTableModel::rowsInserted,
			this, &SeqTableModel::slotRowsInserted);
	connect(this, &SeqTableModel::rowsRemoved,
			this, &SeqTableModel::slotRowsRemoved);
	}

/*! Destruye el modelo y libera todos los recursos */

SeqTableModel::~SeqTableModel() 

{
	deleteAllFK();
	}

/*! Calcula el siguiente valor para la clave primaria */

int SeqTableModel::nextVal (
	const QString	&seqName,
	QSqlDatabase	db
	)

{
	QString	sql = QString("select nextval('%1')").arg(seqName);
	QSqlQuery q(sql, db);
	int res = -1;
	
	if (q.next())
		res = q.value(0).toInt();
	return res;
	}

int SeqTableModel::nextVal()

{
	return nextVal(QString("seq_%1").arg(tableName()), database());
	}

/*!
    Slot para ser invocado en cada nuevo registro.  Pone el siguiente
    valor de la secuencia en la clave primaria.

    En clases derivadas se puede reimplementar para poner otros valores
    por defecto.

 */

void SeqTableModel::calcSeq (
	QSqlRecord	&newRecord
	)
	
{
	if (newRecord.value("id").isNull())
		newRecord.setValue("id", nextVal());
	}
	
/*!
    Crea una cadena de texto con los mensajes de error tanto del driver
    como del motor de base de datos
 */
 
QString SeqTableModel::databaseErrorMessage (
	const QSqlError	&error
	)
	
{
	if (!error.isValid()) {
		qWarning("Error incorrecto en databaseErrorMessage\n");
		return QString();
		}
	QString db = error.databaseText();
	QString dr = error.driverText();
	
	QString res = QString(tr("Error de base de datos: %1, %2").
			arg(error.driverText()).arg(error.databaseText()));
	qWarning("%s\n", res.toLocal8Bit().data());
	return res;
	}
	
/*!
    Envía a la base de datos los cambios realizados en el modelo utilizando
    una transacción para asegurar que entren todos los cambios o ninguno.
 */
 
bool SeqTableModel::submitTrans()

{
	QSqlDatabase db = database();
	
	db.transaction();
	if (submitAll()) {
		db.commit();
		return true;
		}
	else {
		db.rollback();
		qWarning() << databaseErrorMessage(lastError());
		return false;
		}
	}

bool SeqTableModel::submitAll()

{
	if (QSqlTableModel::submitAll()) {
		_dirty = false;
		return true;
		}
	return false;
	}

void SeqTableModel::revertAll()

{
	QSqlTableModel::revertAll();
	_dirty = false;
	}

bool SeqTableModel::pendingChanges() const

{
	return _dirty;
	}

bool SeqTableModel::removeRows (
	int			row,
	int			count,
	const QModelIndex	&parent
	)

{
	_dirty = true;
	return QSqlTableModel::removeRows(row, count, parent);
	}

void SeqTableModel::slotDataChanged (
	const QModelIndex	&, // topLeft, 
	const QModelIndex	& //bottomRight
	)

{
	_dirty = true;
	}

void SeqTableModel::slotRowsInserted (
	const QModelIndex	&, // parent,
	int			, // start,
	int			// end
	)

{
	_dirty = true;
	}

void SeqTableModel::slotRowsRemoved (
	const QModelIndex	&, // parent,
	int			, // start,
	int			// end
	)

{
	_dirty = true;
	}

/*!
    Devuelve true si el registro con clave primaria \a id se puede
    borrar y false si no.  Se utiliza para activar o desactivar el
    botón de "Borrar"
 */
 
bool SeqTableModel::canErase (
	int
	)
	
{
	return true;
	}

/*!
    Devuelve un conjunto con las filas seleccionadas que indica \a l.
    En el conjunto devuelto cada número de fila
    aparece una sóla vez.
 */
 
QList<int>	SeqTableModel::selectedRows (
	const QModelIndexList	&l
	)
	
{
	QSet<int>	res;
	
	for (const auto &idx : l)
		res.insert(idx.row());
	return QList<int>(res.begin(), res.end());
	}

/*!
    Borra todas las filas indicados por \a l.  No guarda los cambios en la
    base de datos, por lo que será necesario llamar luego a \link
    SeqTableModel::submitTrans submitTrans() \endlink o submitAll().
 */
 
bool SeqTableModel::eraseActive (
	const QModelIndexList	&l
	)
	
{
	if (l.empty())
		return false;
	QList<int> l2 = getIds(l);
	for (const auto &i : l2)
		if (!this->canErase(i))
			return false;
	return true;
	}

/*!
    Busca las claves primarias de las filas indicadas por \a rows
 */
 
QList<int>	SeqTableModel::getIds (
	const QList<int> &rows
	)
	
{
	QSet<int>	res;
	
	for (const auto &i : rows)
		res.insert(this->record(i).value("id").toInt());
	return QList<int>(res.begin(), res.end());
	}

/*!
    Busca las claves primarias de las filas indicadas por \a l.
    Garantiza que en el conjunto devuelto no se repite ningún valor.
 */
 
QList<int>	SeqTableModel::getIds (
	const QModelIndexList	&l
	)
	
{
	return getIds(selectedRows(l));
	}
	
/*!
    Obtiene la clave primaria de la fila número \a row.
 */
 
int SeqTableModel::getId (
	int	row
	)
	
{
	return this->record(row).value("id").toInt();
	}
	
/*!
    Si \a l tiene un sólo elemento, devuelve la clave primaria
    de la fila indicada, si no devuelve -1.
 */
 
int SeqTableModel::getId (
	const QModelIndexList	&l
	)
	
{
	QList<int>	rows;
	
	rows = selectedRows(l);
	if (rows.count() != 1)
		return -1;
	else
		return getId(l.at(0).row());
	}

/*!
    Borra las filas indicadas por \a l.
    Los cambios se guardan en la base de datos mediante una transacción,
    o se borran todas o ninguna.
 */
 
bool SeqTableModel::eraseRows (
	const QModelIndexList	&l
	)
	
{
	if (l.empty())
		return true;
	QList<int> l3 = getIds(l);
	QSqlDatabase db = database();
	db.transaction();
	for (const auto &i : l3)
		if (!this->eraseOneRow(i, db)) {
			db.rollback();
			return false;
			}
	db.commit();
	select();
	return true;
	}

/*! Borra una fila de la base de datos de clave primaria \a id.
    Ni abre ni cierra transacción */

bool SeqTableModel::eraseOneRow (
	int		id,
	QSqlDatabase	db
	)
	
{
	QString sql = QString("delete from %1 where id = %2").arg(tableName()).arg(id);
	QSqlQuery q(db);
	
	bool res = q.exec(sql);
	if (!res)
		qWarning() << q.lastError().text();
	return res;
	}

/*! Ejecuta el query \a q y devuelve la primera fila del
    resultado */
    
QSqlRecord	SeqTableModel::executeAndFetchFirst (
	QSqlQuery	&q
	)
	
{
	if (q.next())
		return q.record();
	else
		return QSqlRecord();
	}

/*! Ejecuta el query \a sql sobre la conexión a base de datos
    \a db y devuelve la primera fila del resultado */
    
QSqlRecord	SeqTableModel::executeAndFetchFirst (
	const QString	&sql,
	QSqlDatabase	db
	)
	
{
	QSqlQuery q(sql, db);
	return executeAndFetchFirst(q);
	}
	
/*! Consulta si en la base de datos indicada por \a db, en la tabla
    \a table existe alguna fila que verifique la condición \a condition.
    Si existe devuelve \a true, si no \a false. */
     
bool	SeqTableModel::exists (
	QSqlDatabase	db,
	const QString	&table,
	const QString	&condition
	)
	
{
	QString sql = QString("select count(*) from %1 where %2").arg(table).arg(condition);
	QSqlRecord r = executeAndFetchFirst(sql, db);
	int n = r.value(0).toInt();
	return (n > 0);
	}
	
/*! Ejecuta la orden \a sql en la base de datos asociada al modelo
    y devuelve la primera fila. */
    
QSqlRecord	SeqTableModel::first (
	const QString	&sql
	) const
	
{
	QSqlQuery q(sql, database());
	return executeAndFetchFirst(q);
	}
	
/*! Filtra los registros de la tabla asociada al modelo con la condici�n
    \a fieldName = \a parentId */
    
void	SeqTableModel::setParentFilter (
	QString	fieldName,
	int	parentId
	)
	
{
	QString condition = QString("%1 = %2").arg(fieldName).arg(parentId);
	setFilter(condition);
	select();
	}

/*! Filtra los registros a aquellos que tengan padre \a parentId */

void	SeqTableModel::setParentId (
	int	parentId
	)
	
{
	if (!_parentIdField.isEmpty())
		setParentFilter(_parentIdField, parentId);
	}
	
/*! Devuelve el valor del campo de nombre \a fieldName en la fila
    \a row */
    
QVariant	SeqTableModel::getField (
	int	row,
	QString	fieldName
	)
	
{
	QSqlRecord r = this->record(row);
	if (r.isEmpty())
		return QVariant();
	else
		return r.value(fieldName);
	}

/*!
    Calcula el próximo valor de una secuencia compacta.  La secuencia
    se encuentra en la tabla \a table, en el campo de nombre \a column
    y la fila se puede localizar de forma única con la condición
    \a condition.  Este método ni abre ni cierra transacción.
 */
 
int	SeqTableModel::denseNextVal (
	const QString	&table,
	const QString	&column,
	const QString	&condition
	)
	
{
	QString sql = QString("select %1 from %2 where %3 for update").
				arg(column).
				arg(table).
				arg(condition);
	QSqlDatabase db = database();
	QSqlQuery q(sql, db);
	QSqlRecord r = executeAndFetchFirst(q);
	
	int res = r.value(0).toInt();
	sql = QString("update %1 set %2 = %3 where %4").
		arg(table).arg(column).arg(res + 1).arg(condition);
	db.exec(sql);
	return res;
	}

/*! Localiza el registro con clave primaria \a id */

QSqlRecord	SeqTableModel::findRecord (
	int	id
	)
	
{
	QString sql = QString("select * from %1 where id = %2").arg(tableName()).arg(id);
	return first(sql);
	}

/*!
    Sobrecarga la función QSqlTableModel::data(), para \a role =
    Qt::DisplayRole devuelve el campo asociado mediante el método \link
    SeqTableModel::setForeignKey() setForeignKey() \endlink.  Si \a role
    tiene otro valor, o no hay un ForeignKey asociado invoca a la función
    sobrecargada.

    \sa ForeignKey
 */

QVariant	SeqTableModel::data (
	const QModelIndex	&item,
	int			role
	) const

{
	BaseForeignKey *fk = foreignKey(item.column());

	if ((role != OriginalDataRole) && (fk != nullptr)) {
		bool accept = fk->acceptRole(role);
		if (accept) {
			int r = item.row();
			int c = item.column();
			QVariant v = fk->value(r, c, this);
			return v;
			}
		}
	if (role == OriginalDataRole)
		role = Qt::EditRole;
	return QSqlTableModel::data(item, role);
	}
	
bool	SeqTableModel::setData (
	const QModelIndex	&index, 
	const QVariant		&value, 
	int			role
	)
	
{
	BaseForeignKey *fk = foreignKey(index.column());

	if ((fk != nullptr) && fk->setterAcceptRole(role))
		return fk->setValue(value, index.row(), index.column(), this);
	return QSqlTableModel::setData(index, value, role);
	}

/*! Devuelve el \link ForeignKey ForeignKey \endlink asociado a
    la columna número \a columnIndex */
    
BaseForeignKey	*SeqTableModel::foreignKey (
	int	columnIndex
	) const

{
	if ((columnIndex >= 0) && (columnIndex < _fks.size()))
		return _fks.at(columnIndex);
	else
		return nullptr;
	}

BaseForeignKey	*SeqTableModel::foreignKey (
	const QString	&columnName
	) const

{
	return foreignKey(fieldIndex(columnName));
	}

/*!
    Fija para la columna número \a columnIndex la relación descrita
    por el \link ForeignKey ForeignKey \endlink \a fk
 
    El objeto \a fk pasa a ser propiedad del SeqTableModel y será borrado
    por éste en el destructor o cuando se fije otro ForeignKey a la
    misma columna.
 */

void	SeqTableModel::setForeignKey (
	int		columnIndex,
	BaseForeignKey	*fk,
	bool		deleteOld
	)

{
	QString columnName = _rec.fieldName(columnIndex);
	if (columnName.isEmpty()) {
		delete fk;
		return;
		}
	setForeignKey(columnName, fk, deleteOld);
	}
	
void	SeqTableModel::setForeignKey (
	const QString	&columnName,
	BaseForeignKey	*fk,
	bool		deleteOld
	)

{
	if (_normalFks.contains(columnName) && deleteOld)
		delete _normalFks.value(columnName, nullptr);
	_normalFks[columnName] = fk;
	if (fk == nullptr)
		return;
	initialAcceptFK(fk);
	applyNormalFK(columnName);
	}

void	SeqTableModel::applyNormalFK (
	const QString	&name
	)

{
	int n = QSqlTableModel::fieldIndex(name);
	if (n == -1)
		return;
	BaseForeignKey *fk = _normalFks.value(name, nullptr);
	if (fk == nullptr)
		return;
	setFK(n, fk);
	}

void	SeqTableModel::initialAcceptFK (
	BaseForeignKey	*fk
	)

{
	fk->setDb(database());
	if (fk->needsUpdateControl())
		this->installControlHandlers();
	}

void	SeqTableModel::setFK (
	int		column,
	BaseForeignKey	*fk
	)

{
	while (_fks.count() <= column)
		_fks.append(nullptr);
	_fks[column] = fk;
	fk->setColumn(column);
	}

void	SeqTableModel::addRowControl (
	RowControl *control
	)
	
{
	if (control == nullptr)
		return;
	control->addToTable(this);
	_rowControls.append(control);
	this->installControlHandlers();
	}
	
const QList<RowControl *> &SeqTableModel::rowControls() const

{
	return _rowControls;
	}
	
void	SeqTableModel::deleteAllRowControls()

{
	while (!_rowControls.isEmpty()) {
		RowControl *r = _rowControls.takeLast();
		r->removeFromTable();
		delete r;
		}
	}

void	SeqTableModel::deleteAllNormalFK()

{
	for (const auto &fk : _normalFks.values())
		if (fk != nullptr)
			delete fk;
	_normalFks.clear();
	}

void	SeqTableModel::deleteAllFK()

{
	_fks.clear();
	deleteAllRowControls();
	deleteAllNormalFK();
	}

void	SeqTableModel::installControlHandlers()

{
	if (_needsOpControl)
		return;
	_needsOpControl = true;
	connect(this, &SeqTableModel::primeInsert, this, &SeqTableModel::primeInsert);
	connect(this, &SeqTableModel::beforeDelete, this, &SeqTableModel::beforeDelete);
	connect(this, &SeqTableModel::beforeUpdate, this, &SeqTableModel::beforeUpdate);
	connect(this, &SeqTableModel::beforeInsert, this, &SeqTableModel::beforeInsert);
	}

int	SeqTableModel::addVirtualColumn (
	const QSqlField	&columnDesc,
	BaseForeignKey	*fk
	)

{
	VirtualColumn vc;

	vc.field = columnDesc;
	vc.field.setGenerated(false);
	vc.fk = fk;
	int n = _virtualColumns.count();
	_virtualColumns.append(vc);
	initialAcceptFK(fk);
	applyVirtualColumn(n);
	return n;
	}

void	SeqTableModel::applyVirtualColumn (
	int	n
	)

{
	int c = _rec.count();
	_rec.append(_virtualColumns.at(n).field);
	setFK(c, _virtualColumns.at(n).fk);
	insertColumns(c, 1, QModelIndex());
	}

int	SeqTableModel::addVirtualColumn (
	const QString	&columnName, 
	BaseForeignKey	*fk
	)

{
	QSqlField f(columnName);
	return this->addVirtualColumn(f, fk);
	}
	
QSqlRecord	SeqTableModel::record() const

{
	return _rec;
	}

QSqlRecord	SeqTableModel::record (
	int	row
	) const
	
{
	QSqlRecord res = _rec;
	for (int i = 0; i < res.count(); i++) {
		QModelIndex index = this->index(row, i, QModelIndex());
		QVariant v = this->data(index, Qt::EditRole);
		res.setValue(i, v);
		}
	return res;
	}
	
void	SeqTableModel::primeInsert (
	int		row,
	QSqlRecord	&r
	)
	
{
	if (!_needsOpControl)
		return;
	for (const auto &c : _rowControls)
		c->primeInsert(row, r);
	for (int i = 0; i < _fks.count(); i++) {
		BaseForeignKey *fk = _fks.at(i);
		if ((fk != nullptr) && fk->needsUpdateControl())
			fk->primeInsert(row, i, r);
		}
	}
	
void	SeqTableModel::beforeDelete (
	int	row
	)
	
{
	if (!_needsOpControl)
		return;
	for (const auto &c : _rowControls)
		c->beforeDelete(row);
	for (int i = 0; i < _fks.count(); i++) {
		BaseForeignKey *fk = _fks.at(i);
		if ((fk != nullptr) && fk->needsUpdateControl())
			fk->beforeDelete(row, i);
		}
	}
	
void	SeqTableModel::beforeUpdate (
	int		row,
	QSqlRecord	&r
	)
	
{
	if (!_needsOpControl)
		return;
	for (const auto &c : _rowControls)
		c->beforeUpdate(row, r);
	for (int i = 0; i < _fks.count(); i++) {
		BaseForeignKey *fk = _fks.at(i);
		if ((fk != nullptr) && fk->needsUpdateControl())
			fk->beforeUpdate(row, i, r);
		}
	}

void	SeqTableModel::beforeInsert (
	QSqlRecord	&r
	)
	
{
	if (!_needsOpControl)
		return;
	for (const auto &c : _rowControls)
		c->beforeInsert(r);
	for (int i = 0; i < _fks.count(); i++) {
		BaseForeignKey *fk = _fks.at(i);
		if ((fk != nullptr) && fk->needsUpdateControl())
			fk->beforeInsert(i, r);
		}
	}
		
bool	SeqTableModel::deleteRowFromTable (
	int	row
	)
	
{
	QSqlRecord r;
	
	if (_needsOpControl)
		r = this->record(row);
	bool res = QSqlTableModel::deleteRowFromTable(row);
	if (!_needsOpControl)
		return res;
	for (const auto &c : _rowControls)
		c->afterDelete(row, r);
	for (int i = 0; i < _fks.count(); i++) {
		BaseForeignKey *fk = _fks.at(i);
		if ((fk != nullptr) && fk->needsUpdateControl())
			fk->afterDelete(row, i, r);
		}
	return res;
	}

bool	SeqTableModel::insertRowIntoTable (
	const QSqlRecord	&values
	)
	
{
	QSqlRecord r = values;
	
	bool res = QSqlTableModel::insertRowIntoTable(values);
	if (!_needsOpControl)
		return res;
	for (const auto &c : _rowControls)
		c->afterInsert(r);
	for (int i = 0; i < _fks.count(); i++) {
		BaseForeignKey *fk = _fks.at(i);
		if ((fk != nullptr) && fk->needsUpdateControl())
			fk->afterInsert(i, r);
		}
	return res;
	}
	
bool	SeqTableModel::updateRowInTable (
	int			row, 
	const QSqlRecord	&values
	)
	
{
	QSqlRecord r = values;
	
	bool res = QSqlTableModel::updateRowInTable(row, values);
	if (!_needsOpControl)
		return res;
	for (const auto &c : _rowControls)
		c->afterUpdate(row, r);
	for (int i = 0; i < _fks.count(); i++) {
		BaseForeignKey *fk = _fks.at(i);
		if ((fk != nullptr) && fk->needsUpdateControl())
			fk->afterUpdate(row, i, r);
		}
	return res;
	}

/*! Elimina la caché  de todas las relaciones asociadas */

void SeqTableModel::clearAllForeignKeys()

{
	for (const auto &fk : _fks)
		if (fk != nullptr)
			fk->clear();
	}

void SeqTableModel::revertRowAllForeignKeys (
	int	row
	)

{
	for (const auto &fk : _fks)
		if (fk != nullptr)
			fk->revertRow(row);
	}

void SeqTableModel::clearAllRowControls()

{
	for (const auto &c : _rowControls)
		c->clearCache();
	}

void SeqTableModel::reloadMetadataAllControls()

{
	for (const auto &c : _rowControls)
		c->reloadMetadata();
	}

void SeqTableModel::revertRowAllRowControls (
	int	row
	)

{
	for (const auto &c : _rowControls)
		c->revertRow(row);
	}

void SeqTableModel::reapplyFK()

{
	_fks.clear();
	_rec = QSqlTableModel::record();
	for (int i = 0; i < _rec.count(); i++)
		_fks.append(nullptr);
	for (const auto &name : _normalFks.keys())
		applyNormalFK(name);
	for (int i = 0; i < _virtualColumns.count(); i++)
		applyVirtualColumn(i);
	}

/*!
    Sobrecarga de QSqlTableModel::select(), invoca al método
    sobrecargado después de limpiar las caché de todos los
    \link ForeignKey ForeignKey \endlink.
 */
 
bool SeqTableModel::select()

{
	clearAllForeignKeys();
	clearAllRowControls();
	bool res = QSqlTableModel::select();
	if (res) {
		reapplyFK();
		reloadMetadataAllControls();
		}
	_dirty = false;
	return res;
	}

void SeqTableModel::revert()

{
	QSqlTableModel::revert();
	}

void SeqTableModel::revertRow (
	int	row
	)

{
	revertRowAllForeignKeys(row);
	revertRowAllRowControls(row);
	QSqlTableModel::revertRow(row);
	}

void SeqTableModel::setTable (
	const QString	&tableName
	)

{
	deleteAllFK();
	QSqlTableModel::setTable(tableName);
	reapplyFK();
	}

bool	SeqTableModel::setRecord (
	int			row,
	const QSqlRecord	&record
	)

{
	QSqlRecord r;
	QSqlRecord r2 = QSqlTableModel::record();
	QList<int> v;

	for (int i = 0; i < record.count(); i++)  {
		if (r2.indexOf(record.fieldName(i)) == -1)
			v.append(i);
		else
			r.append(record.field(i));
		}
	if (!QSqlTableModel::setRecord(row, r))
		return false;
	_dirty = true;
	for (const auto &i : v) {
		int n = _rec.indexOf(record.fieldName(i));
		QModelIndex idx = this->index(row, n, QModelIndex());
		QVariant v = record.value(i);
		bool res = this->setData(idx, v, Qt::EditRole);
		if (!res)
			return false;
		}
	return true;
	}

bool	SeqTableModel::insertRecord (
	int			row,
	const QSqlRecord	&record
	)

{
	QSqlRecord r = record;
	if (row < 0)
		row = rowCount();
	if (!insertRow(row, QModelIndex()))
		return false;
	primeInsert(row, r);
	if (!setRecord(row, r))
		return false;
	if (editStrategy() == OnFieldChange || editStrategy() == OnRowChange)
		return submit();
	return true;
	}

