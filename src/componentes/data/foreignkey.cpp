/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: foreignkey.cpp 208 2010-03-24 01:07:11Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/data/foreignkey.cpp $");

#include "foreignkey.h"
#include <SeqTableModel>

/*!
    \class ForeignKey seqtablemodel.h
    \brief Representa una relación de una columna con otra tabla, y
           la columna que la representará

    Clase auxiliar para \link SeqTableModel SeqTableModel \endlink, permite
    representar las relaciones con otras tablas y que cuando se saca la
    tabla en pantalla aparezca un campo descriptivo en lugar de la clave
    primaria de la tabla relacionada.

    \sa SeqTableModel
 */

/*!
    Crea una relación con la tabla indicada por \a table.  La columna indicada
    por \a column debe indicar una representación adecuada del registro y tener
    formato texto (por ejemplo un nombre).

    ForeignKey conserva una caché de valores de la tabla maestra, para no
    tener que consultar varias veces la base de datos, esta caché tiene un
    número máximo de entradas y cuando la caché alcanza el número máximo
    descarta una entrada cualquiera.
 */
 
ForeignKey::ForeignKey (
	QString	table,
	QString	column
	) :
	_table(table),
	_column(column),
	_map(),
	_inverseMap(),
	_model(nullptr),
	_q(nullptr),
	_db(),
	_lastWhere()

{
	}

/*! Destruye el objeto */

ForeignKey::~ForeignKey()

{
	if (_model != nullptr)
		delete _model;
	if (_q != nullptr)
		delete _q;
	}

/*! Si la clave primaria está en la caché, devuelve el valor de la caché
    si no lo busca en la base de datos y lo guarda en la caché */
    
QString	ForeignKey::value (
	int	id
	)

{
	if (_map.contains(id))
		return _map.value(id);
	else
		return getNewValue(id);
	}

QVariant ForeignKey::value (
	int			row,
	int			column,
	const SeqTableModel	*m
	)
	
{
	bool good;
	QVariant v = m->data(m->index(row, column, QModelIndex()), SeqTableModel::OriginalDataRole);
	if (!v.isValid() || v.isNull())
		return QVariant(QString());
	int id = v.toInt(&good);
	if (! good)
		return QVariant();
	return QVariant(this->value(id));
	}
	
/*! Va a buscar un valor a la base de datos y lo guarda en la caché */

QString ForeignKey::getNewValue (
	int	id
	)

{
	QString sql = QString("select %1 from %2 where id = %3").
			arg(_column).arg(_table).arg(id);
	QSqlQuery q(sql, _db);
	QString res;
	if (q.first())
		res = q.value(0).toString();
	else
		res = QString("%1").arg(id);
	_map.insert(id, res);
	return res;
	}

QString ForeignKey::constructWhere (
	const QMap<QString, QVariant> &all
	) const

{
	if (all.isEmpty())
		return QString();
	QString res;
	QStringList cond;
	for (auto i = all.constBegin(); i != all.constEnd(); ++i)
		if (i.value().isValid())
			cond.append(QString("%1 = :%1").arg(i.key()));
	if (cond.count() > 0)
		res = " where " + cond.join(" and ");
	return res;
	}

QString ForeignKey::constructKey (
	const QMap<QString, QVariant> &all
	) const
	
{
	QStringList r;
	
	for (auto i = all.constBegin(); i != all.constEnd(); ++i)
		if (i.value().isValid())
			r.append(QString("%1=%2").arg(i.key()).arg(i.value().toString()));
	QString res = r.join(",");
	return res;
	}
	
int ForeignKey::inverseMap (
	const QString			&value,
	const QMap<QString, QVariant>	&filters
	)

{
	QMap<QString, QVariant> all(filters);
	
	all.insert(_column, QVariant(value));
	QString key = constructKey(all);
	if (_inverseMap.contains(key))
		return _inverseMap.value(key);
	else
		return getNewInverseMap(key, all);
	}

void ForeignKey::bindValues (
	const QMap<QString, QVariant>	&all
	)
	
{
	for (QMap<QString, QVariant>::const_iterator i = all.constBegin(); i != all.constEnd(); ++i) {
		QString n = QString(":%1").arg(i.key());
		_q->bindValue(n, i.value());
		}
	}
	
int ForeignKey::getNewInverseMap (
	const QString			&key,
	const QMap<QString, QVariant>	&all
	)

{
	QString where = constructWhere(all);
	if ((_lastWhere != where) || (_q == nullptr)) {
		QString sql = QString("select id from %1 %2").arg(_table).arg(where);
		if (_q == nullptr)
			_q = new QSqlQuery(_db);
		_q->prepare(sql);
		_lastWhere = where;
		}
	bindValues(all);
	if (!_q->exec())
		return -1;
	if (!_q->next())
		return -1;
	bool good;
	int id = -1;
	id = _q->value(0).toInt(&good);
	if (!good)
		return -1;
	_inverseMap.insert(key, id);
	return id;
	}

void	ForeignKey::setDb (
	const QSqlDatabase	&db
	)
	
{
	_db = db;
	clear();
	}
	
/*! Elimina todos los valores de la caché */

void	ForeignKey::clear()

{
	_map.clear();
	_inverseMap.clear();
	_lastWhere = QString();
	if (_q != nullptr)
		delete _q;
	_q = nullptr;
	}

/*! Devuelve un modelo adaptado a la generación de ComboBox */

FKModel	*ForeignKey::model (
	const QMap<QString, QVariant>	&filters,
	bool				nullValue,
	const QString			&nullMessage
	)

{
	QString w = constructWhere(filters);
	if (_model != nullptr) {
		_model->setWhere(w, filters);
		_model->setNullValue(nullValue);
		_model->setNullMessage(nullMessage);
		return _model;
		}
	_model = new FKModel(_db, _table, _column, w, filters,
			     nullValue, nullMessage);
	return _model;
	}

