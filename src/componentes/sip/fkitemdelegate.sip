/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: dimensionedit.sip 133 2009-10-27 14:22:39Z bruno $
  $URL: http://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/dimensionedit.sip $
*****************************************************************************/

class FKItemDelegate : QItemDelegate {

%TypeHeaderCode
#include <FKItemDelegate>
%End

public:
	FKItemDelegate(const QMap<QString, QVariant> &filters,
			QObject *parent /TransferThis/ = 0,
			const QString &nullMessage = QString());
	
	virtual QWidget *createEditor(QWidget *parent /TransferThis/, 
			const QStyleOptionViewItem &option, 
			const QModelIndex &index) const /Factory/;
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

