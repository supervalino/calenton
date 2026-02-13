/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: foreignkey.h 234 2010-04-28 12:01:05Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/data/foreignkey.h $
*****************************************************************************/

#ifndef FOREIGNKEY_H
#define FOREIGNKEY_H

#include <BaseForeignKey>
#include <FKModel>

class ForeignKey : public  BaseForeignKey {
private:
	QString			_table;
	QString 		_column;
	QMap<int, QString>	_map;
	QMap<QString, int>	_inverseMap;
	FKModel			*_model;
	QSqlQuery		*_q;
	QSqlDatabase		_db;
	QString			_lastWhere;
public:
	ForeignKey(QString table, QString column);
	virtual ~ForeignKey();

	QString		value(int id);
	QVariant	value(int row, int column, const SeqTableModel *m);
	int		inverseMap(const QString &v, const QMap<QString, QVariant> &filters);
	FKModel		*model(const QMap<QString, QVariant> &filters,
				bool nullValue = false,
				const QString &nullMessage = QString());
	void		setDb(const QSqlDatabase &db);
	void		clear();
	void		revertRow(int /* row */) {}
protected:
	virtual QString	constructWhere(const QMap<QString, QVariant> &filters) const;
	virtual QString	constructKey(const QMap<QString, QVariant> &filters) const;
private:
	void	bindValues(const QMap<QString, QVariant> &filters);
	QString	getNewValue(int id);
	int	getNewInverseMap(const QString &key, const QMap<QString, QVariant> &all);
	};

#endif // FOREIGNKEY_H

