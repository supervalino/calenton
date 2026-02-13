/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: combodatamodel.h 203 2010-03-23 13:36:16Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/data/combodatamodel.h $
*****************************************************************************/

#ifndef COMBODATAMODEL_H
#define COMBODATAMODEL_H

#include <QAbstractListModel>
#include <QString>
#include <QSqlDatabase>

class QSqlQueryModel;
class QSqlQuery;

class ComboDataModel : public QAbstractListModel {
	Q_OBJECT
private:
	QSqlQueryModel	*_sm;
	bool		_nullValue;
	QString		_nullMessage;
public:
	ComboDataModel(QObject *parent = NULL,
		       bool nullValue = false,
		       const QString &nullMessage = QString());
	ComboDataModel(QSqlQuery &q, QObject *parent = NULL,
		       bool nullValue = false,
		       const QString &nullMessage = QString());
	~ComboDataModel();

	virtual int rowCount(const QModelIndex &parent = QModelIndex()) const;
	virtual QVariant data(const QModelIndex &index, int role) const;
	
	virtual void	setQuery(QSqlQuery &q);
	void		setQuery(const QString &sql, QSqlDatabase db);

	void	setNullValue(bool nullValue);
	bool	nullValue() const  { return _nullValue; }

	void	setNullMessage(const QString &nullMessage);
	QString	nullMessage() const { return _nullMessage; }
	};

#endif // COMBODATAMODEL_H
