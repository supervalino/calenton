/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: fkmodel.h 206 2010-03-23 16:53:36Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/data/fkmodel.h $
*****************************************************************************/

#ifndef FKMODEL_H
#define FKMODEL_H

#include <ComboDataModel>

class FKModel : public ComboDataModel {
	Q_OBJECT
private:
	QString		_table;
	QString		_column;
	QSqlDatabase	_db;
	QString		_sql;

	FKModel() : ComboDataModel() {}
public:
	FKModel(QSqlDatabase &db, const QString &table, 
		const QString &column, const QString &where,
		const QMap<QString, QVariant> &filters,
		bool nullValue = false,
		const QString &nullMessage = QString());
	~FKModel();

	void	setWhere(const QString &where, const QMap<QString, QVariant> &filters);
	void	setFilters(const QMap<QString, QVariant> &filters);
	};

#endif // FKMODEL_H
