/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: fkitemdelegate.cpp 210 2010-03-29 09:34:02Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/widgets/fkitemdelegate.cpp $");

#include "fkitemdelegate.h"
#include <SeqTableModel>
#include <TComboBox>
#include <ForeignKey>

FKItemDelegate::FKItemDelegate (
	const QMap<QString, QVariant>	&filters,
	QObject				*parent,
	const QString			&nullMessage
	) :
	QItemDelegate(parent),
	_filters(filters),
	_nullMessage(nullMessage)
		
{
	}
	
QWidget	*FKItemDelegate::createEditor (
	QWidget				*parent,
	const QStyleOptionViewItem	&, // option,
	const QModelIndex		& // index
	) const
	
{
	TComboBox *e = new TComboBox(parent);
	e->setEditable(false);
	e->installEventFilter(const_cast<FKItemDelegate *>(this));
	return e;
	}

QMap<QString, QVariant> FKItemDelegate::getFilters (
	const QSqlTableModel	*model,
	const QModelIndex	&index
	) const
	
{
	QMap<QString, QVariant> res(_filters);
	
	QSqlRecord r = model->record(index.row());
	for (auto i = res.begin(); i != res.end(); ++i) {
		if (i.value().typeId() == QMetaType::UnknownType) {
			QString name = i.key();
			QVariant v = r.value(name);
			i.value() = v;
			}
		}
	return res;
	}
		
QAbstractItemModel	*FKItemDelegate::filteredModel (
	QWidget				*, // editor,
	const QAbstractItemModel	*model,
	const QModelIndex		&index
	) const
	
{
	const SeqTableModel *tm = dynamic_cast<const SeqTableModel *>(model);
	if (tm == nullptr)
		return nullptr;
	ForeignKey *fk = dynamic_cast<ForeignKey *>(tm->foreignKey(index.column()));
	if (fk == nullptr)
		return nullptr;
	QSqlField::RequiredStatus s = tm->record().field(index.column()).requiredStatus();
	bool nullValue = (s == QSqlField::Optional);
	FKModel *m = fk->model(getFilters(tm, index), nullValue, _nullMessage);
	return m;
	}
	
void	FKItemDelegate::setEditorData (
	QWidget			*editor,
	const QModelIndex	&index
	) const
	
{
	TComboBox *e = dynamic_cast<TComboBox *>(editor);
	if (e == nullptr)
		return;
	e->clear();

	if (!index.isValid())
		return;

	const QAbstractItemModel *tm = index.model();
	QAbstractItemModel *m = this->filteredModel(editor, tm, index);
	if (m == nullptr)
		return;
	e->setModel(m);
	bool g;
	QVariant v = tm->data(index, Qt::EditRole);
	int nv = v.toInt(&g);
	if (!g) {
		return;
		}
	e->setCurrentItemData(nv);
	}
	
void	FKItemDelegate::setModelData (
	QWidget			*editor,
	QAbstractItemModel	*model,
	const QModelIndex	&index
	) const
	
{
	TComboBox *e = dynamic_cast<TComboBox *>(editor);
	if (e == nullptr)
		return;
	QVariant v = e->currentItemData();
	bool g;
	int nv = v.toInt(&g);
	if (!g)
		return;
	int nvo = model->data(index, Qt::EditRole).toInt(&g);
	if (g)
		if (nv == nvo)
			return;
	model->setData(index, nv);
	}

void	FKItemDelegate::updateEditorGeometry (
	QWidget				*editor,
	const QStyleOptionViewItem	&option,
	const QModelIndex		& // index
	) const

{
	editor->setGeometry(option.rect);
	}
	
void	FKItemDelegate::setFilterValue (
	const QString	&key,
	const QVariant	&value
	)
	
{
	if (_filters.contains(key))
		_filters[key] = value;
	}

