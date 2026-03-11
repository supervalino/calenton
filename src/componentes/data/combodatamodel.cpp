/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: combodatamodel.cpp 208 2010-03-24 01:07:11Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/data/combodatamodel.cpp $");

#include "combodatamodel.h"
#include <QSqlQuery>
#include <QSqlQueryModel>

ComboDataModel::ComboDataModel (
	QObject		*parent,
	bool		nullValue,
	const QString	&nullMessage
	) :
	QAbstractListModel(parent),
	_sm(nullptr),
	_nullValue(nullValue),
	_nullMessage(nullMessage)
	
{
	}
	
ComboDataModel::ComboDataModel (
	QSqlQuery	&q, 
	QObject		*parent,
	bool		nullValue,
	const QString	&nullMessage
	) :
	QAbstractListModel(parent),
	_sm(nullptr),
	_nullValue(nullValue),
	_nullMessage(nullMessage)
	
{
	if (q.isValid())
		setQuery(q);
	}
	
ComboDataModel::~ComboDataModel()

{
	}

int ComboDataModel::rowCount (
	const QModelIndex & // parent
	) const

{
	int	n;

	if (_sm == nullptr)
		n = 0;
	else
		n = _sm->rowCount();
	if (_nullValue)
		n++;
	return n;
	}

QVariant ComboDataModel::data (
	const QModelIndex	&index,
	int			role
	) const

{
	if (!index.isValid())
		return QVariant();
	if (_sm == nullptr)
		return QVariant();
	int column;
	switch (role) {
		case Qt::DisplayRole:
		case Qt::EditRole:
			column = 1;
			break;
		case Qt::UserRole:
			column = 0;
			break;
		default:
			return QVariant();
		}
	int row = index.row();
	if (row < 0)
		return QVariant();
	if (_nullValue) {
		if (row == 0) {
			if (column == 0)
				return QVariant(QString());
			else
				return QVariant(_nullMessage);
			}
		else
			row--;
		}
	QModelIndex i = _sm->index(row, column);
	QVariant v = _sm->data(i, Qt::DisplayRole);
	return v;
	}

void ComboDataModel::setQuery (
	QSqlQuery	&q
	)
	
{
	int firstRow = _nullValue ? 1 : 0;
	if (_sm != nullptr) {
		beginRemoveRows(QModelIndex(), firstRow, _sm->rowCount() - 1 + firstRow);
		delete _sm;
		_sm = nullptr;
		endRemoveRows();
		}
	if (q.lastError().isValid()) {
		qDebug() << q.lastError();
		return;
		}
	if (!q.isActive())
		return;
	QSqlQueryModel *sm = new QSqlQueryModel(this);		 
	sm->setQuery(q);
	if (sm->lastError().isValid()) {
		qDebug() << sm->lastError();
		delete sm;
		return;
		}
	beginInsertRows(QModelIndex(), firstRow, sm->rowCount() - 1 + firstRow);
	_sm = sm;
	endInsertRows();
	}

void ComboDataModel::setQuery (
	const QString 	&sql,
	QSqlDatabase	db
	)
	
{
	QSqlQuery q(sql, db);
	
	this->setQuery(q);
	}

void ComboDataModel::setNullValue (
	bool nullValue
	)

{
	if (nullValue == _nullValue)
		return;
	if (nullValue) {
		beginInsertRows(QModelIndex(), 0, 0);
		_nullValue = true;
		endInsertRows();
		}
	else {
		beginRemoveRows(QModelIndex(), 0, 0);
		_nullValue = false;
		endRemoveRows();
		}
	}

void ComboDataModel::setNullMessage (
	const QString	&nullMessage
	)

{
	bool changed = (_nullMessage != nullMessage);

	_nullMessage = nullMessage;
	if (_nullValue && changed)
		emit dataChanged(index(0, 0), index(0, 0));
	}
