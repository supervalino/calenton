/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: fkitemdelegate.h 203 2010-03-23 13:36:16Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/widgets/fkitemdelegate.h $
*****************************************************************************/

#ifndef FKITEMDELEGATE_H
#define FKITEMDELEGATE_H

#include <QItemDelegate>
#include <QAbstractItemModel>

class QSqlTableModel;

class FKItemDelegate : public QItemDelegate {
	Q_OBJECT
private:
	QMap<QString, QVariant>	_filters;
	QString			_nullMessage;
	
	QMap<QString, QVariant> getFilters(const QSqlTableModel *model, 
					const QModelIndex &index) const;
public:
	FKItemDelegate(const QMap<QString, QVariant> &filters,
			QObject *parent = nullptr,
			const QString &nullMessage = QString());
	
	virtual QWidget *createEditor(QWidget *parent, 
			const QStyleOptionViewItem &option, 
			const QModelIndex &index) const;
	virtual void	setEditorData(QWidget *editor, const QModelIndex &index) const;
	virtual void	setModelData(QWidget *editor, QAbstractItemModel *model,
			const QModelIndex &index) const;
	virtual void	updateEditorGeometry(QWidget *editor, 
			const QStyleOptionViewItem &option,
			const QModelIndex &index) const;
	virtual void	setFilterValue(const QString &key, const QVariant &value);
	virtual QAbstractItemModel *filteredModel(QWidget *editor,
			const QAbstractItemModel *model, 
			const QModelIndex &index) const;
	};
	

#endif // FKITEMDELEGATE_H
