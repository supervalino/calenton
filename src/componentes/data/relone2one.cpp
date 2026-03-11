/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: relone2one.cpp 199 2010-03-01 16:51:33Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/data/relone2one.cpp $");

#include "relone2one.h"
#include <RelOne2OneProxy>
#include <QSqlQuery>
#include <QSqlRecord>

RelOne2One::RelOne2One (
	QString	idColumnName,
	QString	relTable
	) :
	RowControl(),
	_relTable(relTable),
	_idColumn(-1),
	_idColumnName(idColumnName),
	_rec(),
	_tableRec(),
	_columns(),
	_internalColumnNumber(),
	_index2InternalColumn()

{
	addColumnData("id", QString(), false);
	}

RelOne2One::~RelOne2One()

{
	}

void	RelOne2One::clearCache()

{
	_cache.clear();
	}

void	RelOne2One::addToTable (
	SeqTableModel	*table
	)

{
	RowControl::addToTable(table);
	initMetadata();
	}

void	RelOne2One::addColumnToTable (
	int	n
	)

{
	QSqlField f(_rec.field(n));
	f.setName(_columns[n].destName);
	RelOne2OneProxy *p = new RelOne2OneProxy(this);
	int c = table()->addVirtualColumn(f, p);
	_columns[n].p = p;
	p->setColumn(c);
	_index2InternalColumn[p->index()] = n;
	}

void	RelOne2One::initMetadata()

{
	_cache.clear();
	_tableRec = db().record(_relTable);
	_idColumn = table()->record().indexOf(_idColumnName);
	for (const auto &d : _columns) {
		_rec.append(_tableRec.field(d.origName));
		if (d.userColumn)
			addColumnToTable(_rec.count() - 1);
		}
	}

void	RelOne2One::reloadMetadata()

{
	_cache.clear();
	_idColumn = table()->record().indexOf(_idColumnName);
	_index2InternalColumn.clear();
	for (int i = 0; i < _columns.count(); i++)
		if (_columns[i].p != nullptr)
			_index2InternalColumn[_columns[i].p->index()] = i;
	}

void	RelOne2One::addColumn (
	const QString	&fieldName,
	const QString	&destName
	)

{
	addColumnData(fieldName, destName, true);
	}

void	RelOne2One::addColumnData (
	const QString	&origName,
	const QString	&destName,
	bool		userColumn
	)

{
	QString fn = origName.toLower();
	if (_internalColumnNumber.contains(fn)) {
		int idx = _internalColumnNumber[fn];
		if (userColumn && (!_columns[idx].userColumn)) {
			_columns[idx].userColumn = true;
			_columns[idx].destName = destName.toLower();
			if (_idColumn > -1)
				addColumnToTable(idx);
			}
		return;
		}
	ColumnData d;
	d.userColumn = userColumn;
	d.origName = fn;
	d.destName = destName.toLower();
	d.p = nullptr;
	_internalColumnNumber[fn] = _columns.count();
	_columns.append(d);
	if (_idColumn > -1) {
		_rec.append(_tableRec.field(fn));
		if (userColumn)
			addColumnToTable(_rec.count() - 1);
		}
	clearCache();
	}

int	RelOne2One::internalColumn (
	const QString	&origColumnName
	)

{
	return _internalColumnNumber.value(origColumnName, -1);
	}

bool	RelOne2One::setCacheValue (
	int		row,
	int		myColumnNumber,
	const QVariant	&value
	)

{
	if (!_cache.contains(row))
		return false;
	if ((myColumnNumber < 0) || (myColumnNumber >= _rec.count()))
		return false;
	_cache[row].setValue(myColumnNumber, value);
	return true;
	}

QStringList RelOne2One::columnNames() const

{
	QStringList res;

	for (int i = 0; i < _columns.count(); i++)
		res.append(_columns.at(i).origName);
	return res;
	}

bool	RelOne2One::ensureLineInCache (
	int	row,
	int	id
	)

{
	if (_cache.contains(row))
		return true;

	QString l = columnNames().join(",");
	QString sql = QString("select %1 from %2 where id = %3").
				arg(l).arg(_relTable).arg(id);
	QSqlQuery q(sql, db());
	if (q.lastError().isValid()) {
		qDebug() << q.lastError().text();
		_cache[row] = _rec;
		return false;
		}
	q.first();
	if (!q.isValid()) {
		_cache[row] = _rec;
		return false;
		}
	_cache[row] = q.record();
	return true;
	}

bool	RelOne2One::ensureLineInCache (
	int			row,
	const SeqTableModel	*m
	)

{
	bool good;
	int id = m->data(m->index(row, _idColumn, QModelIndex()), SeqTableModel::OriginalDataRole)
			.toInt(&good);
	if (!good || (id <= 0))
		return false;
	return ensureLineInCache(row, id);
	}

QVariant RelOne2One::value (
	const RelOne2OneProxy	*p,
	int			row,
	int			column,
	const SeqTableModel	*m
	)

{
	Q_UNUSED(column)

	int mc = _index2InternalColumn.value(p->index(), -1);
	if (mc == -1)
		return QVariant();
	if (!_cache.contains(row))
		ensureLineInCache(row, m);
	return _cache[row].value(mc);
	}

bool RelOne2One::setValue (
	const RelOne2OneProxy	*p,
	const QVariant		&value,
	int			row,
	int			column,
	const SeqTableModel	*m
	)

{
	Q_UNUSED(column)

	int mc = _index2InternalColumn.value(p->index(), -1);
	if (mc == -1)
		return false;
	if (!_cache.contains(row))
		ensureLineInCache(row, m);
	_cache[row].setValue(mc, value);
	return true;
	}

int	RelOne2One::encodeRowInId (
	int	row
	)

{
	return -row - 1;
	}

int	RelOne2One::decodeRowFromId (
	int	falseId
	)

{
	return -falseId - 1;
	}

void RelOne2One::primeInsert (
	int		row,
	QSqlRecord	&r
	)

{
	r.setValue(_idColumn, encodeRowInId(row));
	_cache[row] = _rec;
	}

int RelOne2One::getNextId() const

{
	QString sql = QString("select nextval('seq_%1')").arg(_relTable);
	QSqlQuery q(sql, db());
	if (q.lastError().isValid())
		return -1;
	q.first();
	if (!q.isValid())
		return -1;
	bool good;
	int id = q.value(0).toInt(&good);
	if (!good)
		return -1;
	return id;
	}

int	RelOne2One::insertRowInTable (
	int row
	)

{
	QString		fields, values;
	QStringList	fl, vl;

	if (!_cache.contains(row))
		return -1;
	for (int i = 0; i < _rec.count(); i++) {
		QString n = _rec.field(i).name();
		fl.append(n);
		vl.append(QString(":%1").arg(n));
		}
	fields = fl.join(",");
	values = vl.join(",");
	QString sql = QString("insert into %1 (%2) values (%3)").
				arg(_relTable).arg(fields).arg(values);
	QSqlQuery q(db());
	if (!q.prepare(sql)) {
		qDebug() << q.lastError().text();
		return -1;
		}
	int id = getNextId();
	_cache[row].setValue("id", id);
	for (int i = 0; i < fl.count(); i++)
		q.bindValue(vl[i], _cache[row].value(fl[i]));
	if (!q.exec()) {
		qDebug() << q.lastError().text();
		return -1;
		}
	return id;
	}

void RelOne2One::beforeInsert (
	QSqlRecord	&r
	)

{
	bool good;
	int row = r.value(_idColumn).toInt(&good);

	if (!good || (row >= 0))
		return;
	row = decodeRowFromId(row);
	int id = insertRowInTable(row);
	if (id > 0)
		r.setValue(_idColumn, id);
	else
		r.setValue(_idColumn, QVariant());
	}

void RelOne2One::deleteRowFromTable (
	int	id
	)

{
	QString sql = QString("delete from %1 where id = %2").
				arg(_relTable).arg(id);
	QSqlQuery q(sql, db());
	if (q.lastError().isValid())
		qDebug() << q.lastError().text();
	}

void RelOne2One::afterDelete (
	int		row,
	QSqlRecord	&r
	)

{
	bool good;
	int id = r.value(_idColumn).toInt(&good);
	if (_cache.contains(row))
		_cache.remove(row);
	if (!good || (id <= 0))
		deleteRowFromTable(id);
	}

bool RelOne2One::updateRowInTable (
	int	row
	)

{
	QString		assign;
	QStringList	fl, vl, al;

	if (!_cache.contains(row))
		return false;
	for (int i = 0; i < _rec.count(); i++) {
		QString n = _rec.field(i).name();
		fl.append(n);
		vl.append(QString(":%1").arg(n));
		al.append(QString("%1 = :%1").arg(n));
		}
	assign = al.join(",");
	bool good;
	int id = _cache[row].value("id").toInt(&good);
	if (!good || (id <= 0))
		return false;
	QString sql = QString("update %1 set %2 where id = %3").
				arg(_relTable).arg(assign).arg(id);
	QSqlQuery q(db());
	if (!q.prepare(sql)) {
		qDebug() << q.lastError().text();
		return false;
		}
	for (int i = 0; i < fl.count(); i++)
		q.bindValue(vl[i], _cache[row].value(fl[i]));
	if (!q.exec()) {
		qDebug() << q.lastError().text();
		return false;
		}
	return true;
	}

void RelOne2One::afterUpdate (
	int		row,
	QSqlRecord	&r
	)

{
	bool good;
	int id = r.value(_idColumn).toInt(&good);
	if (good && (id > 0))
		updateRowInTable(row);
	}

void RelOne2One::revertRow (
	int	row
	)

{
	_cache.remove(row);
	}
