/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: fkmodel.cpp 208 2010-03-24 01:07:11Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/data/fkmodel.cpp $");

#include "fkmodel.h"

FKModel::FKModel (
	QSqlDatabase			&db,
	const QString 			&table,
	const QString			&column,
	const QString			&where,
	const QMap<QString, QVariant>	&filters,
	bool				nullValue,
	const QString			&nullMessage
	) :
	ComboDataModel(nullptr, nullValue, nullMessage),
	_table(table),
	_column(column),
	_db(db)

{
	setWhere(where, filters);
	}
	

void FKModel::setFilters (
	const QMap<QString, QVariant>	&filters
	)

{
	if (_sql.isEmpty())
		return;
	QSqlQuery q(_db);
	q.prepare(_sql);
	if (q.lastError().isValid()) {
		qDebug() << "FKModel::setFilters" << q.lastError();
		return;
		}
	for (auto i = filters.constBegin(); i != filters.constEnd(); ++i) {
		QString n = QString(":%1").arg(i.key());
		q.bindValue(n, i.value());
		}
	q.exec();
	if (q.lastError().isValid()) {
		qDebug() << "FKModel::setFilters" << q.lastError();
		return;
		}
	this->setQuery(q);
	}

void FKModel::setWhere (
	const QString			&where,
	const QMap<QString, QVariant>	&filters
	)
	
{
	_sql = QString("select id, %1 from %2 %3 order by 2").
			arg(_column).arg(_table).arg(where);
	setFilters(filters);
	}
	
FKModel::~FKModel()

{
	}

