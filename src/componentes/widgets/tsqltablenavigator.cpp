/*****************************************************************************
  TRUST COMPONENTS

  (C) Trustserver S. L., 2009

  Todos los derechos reservados.
*****************************************************************************/
#include "hdr.h"

ID_ID("$Id: tsqltablenavigator.cpp 223 2010-04-09 11:55:37Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/widgets/tsqltablenavigator.cpp $");

#include <TSqlTableNavigator>
#include <SeqTableModel>
#include <DataDialog>

TSqlTableNavigator::TSqlTableNavigator (
	QWidget	*parent
	) :
	QWidget(parent),
	_autoResizeRows(false),
	_autoResizeColumns(false),
	_showButtons(true),
	_selectedId(-1),
	_modelDirty(),
	_model(NULL),
	_delegate(NULL)

{
	setupUi(this);
	}

TSqlTableNavigator::~TSqlTableNavigator()

{
	}

void TSqlTableNavigator::setModel (
	SeqTableModel	*model
	)

{
	_model = model;
	uiTableView->setModel(model);
	updateContent();
	}

void TSqlTableNavigator::on_uiTableView_selectionChanged (
	const QItemSelection	&, // selected,
	const QItemSelection	& // deselected
	)

{
	if (_model == NULL)
		return;

	QModelIndexList l = uiTableView->selectionModel()->selectedIndexes();
	int newId = _model->getId(l);
	if (newId != _selectedId) {
		_selectedId = newId;
		emit idChanged(_selectedId);
		}
	uiButtonBox->button(TSqlButtonBox::DeleteButton)->setEnabled(_model->eraseActive(l));
	uiButtonBox->button(TSqlButtonBox::SaveButton)->setEnabled(_model->pendingChanges());
	uiButtonBox->button(TSqlButtonBox::DiscardButton)->setEnabled(_model->pendingChanges());
	uiButtonBox->button(TSqlButtonBox::EditButton)->setEnabled(_selectedId > 0);
	uiButtonBox->button(TSqlButtonBox::AddButton)->setEnabled(couldAdd());
	}

void TSqlTableNavigator::updateContent()

{
	resizeIfNeeded();
	on_uiTableView_selectionChanged(QItemSelection(), QItemSelection());
	}

void TSqlTableNavigator::resizeIfNeeded()

{
	if (_autoResizeColumns)
		uiTableView->resizeColumnsToContents();
	if (_autoResizeRows)
		uiTableView->resizeRowsToContents();
	}

void TSqlTableNavigator::setParentId (
	int	id
	)

{
	if (!_model)
		return;
	_model->setParentId(id);
	updateContent();
	}

void TSqlTableNavigator::setFilter (
	const QString	&filter
	)

{
	if (!_model)
		return;
	_model->setFilter(filter);
	updateContent();
	}

void TSqlTableNavigator::setDelegate (
	Delegate	*delegate
	)

{
	_delegate = QPointer<Delegate>(delegate);
	on_uiTableView_selectionChanged(QItemSelection(), QItemSelection());
	}

bool TSqlTableNavigator::couldAdd()

{
	return (_delegate) ? _delegate->couldAdd(this) : true;
	}

DataDialog *TSqlTableNavigator::createEditor()

{
	return (_delegate) ? _delegate->createEditor(this) : NULL;
	}

void TSqlTableNavigator::on_uiButtonBox_addClicked (
	bool	// checked
	)

{
	if (!_model)
		return;

	DataDialog *e = createEditor();

	if (e) {
		e->add();
		delete e;
		on_uiTableView_selectionChanged(QItemSelection(), QItemSelection());
		}
	else {
		int row = _model->rowCount();
		QSqlRecord r = newRecord();
		_model->insertRecord(row, r);
		QModelIndex idx = _model->index(row, 1);
		resizeIfNeeded();
		uiTableView->setCurrentIndex(idx);
		uiTableView->edit(idx);
		}
	}

void TSqlTableNavigator::on_uiTableView_doubleClicked (
	const QModelIndex	&index
	)

{
	if (!_model)
		return;

	DataDialog *e = createEditor();

	if (e) {
		e->edit(index.row());
		delete e;
		on_uiTableView_selectionChanged(QItemSelection(), QItemSelection());
		}
	}

void TSqlTableNavigator::on_uiButtonBox_editClicked (
	bool	// checked
	)

{
	if (!_model)
		return;

	QModelIndexList l = uiTableView->selectionModel()->selectedIndexes();
	QList<int> l2 = _model->selectedRows(l);
	if (l2.count() == 1)
		on_uiTableView_doubleClicked(l[0]);
	}

void TSqlTableNavigator::on_uiButtonBox_discardClicked (
	bool	// checked
	)

{
	if (!_model)
		return;

	_model->select();
	updateContent();
	}

void TSqlTableNavigator::on_uiButtonBox_saveClicked (
	bool	// checked
	)

{
	if (!_model)
		return;

	_model->submitTrans();
	updateContent();
	}

void TSqlTableNavigator::on_uiButtonBox_deleteClicked (
	bool	// checked
	)

{
	if (!_model)
		return;

	QItemSelection l = uiTableView->selectionModel()->selection();
	while (l.count() > 0) {
		QItemSelectionRange r = l.at(0);
		if ((r.left() == 0) and (r.right() == (uiTableView->horizontalHeader()->count() - 1))) {
			int top = r.top();
			int height = r.height();
			QModelIndex parent = r.parent();

			QItemSelection s = QItemSelection(r.topLeft(), r.bottomRight());
			uiTableView->selectionModel()->select(s, QItemSelectionModel::Deselect);
			_model->removeRows(top, height, parent);
			on_uiTableView_selectionChanged(QItemSelection(), QItemSelection());
			}
		else {
			QModelIndexList idxs = r.indexes();
			foreach(QModelIndex idx, idxs)
				if (idx.column() > 1)
					_model->setData(idx, QVariant(), Qt::EditRole);
			QItemSelection s = QItemSelection(r.topLeft(), r.bottomRight());
			uiTableView->selectionModel()->select(s, QItemSelectionModel::Deselect);
			}
		l = uiTableView->selectionModel()->selection();
		}
	}

void TSqlTableNavigator::setShowButtons (
	bool	showButtons
	)

{
	if (showButtons != _showButtons) {
		uiButtonBox->setVisible(showButtons);
		_showButtons = showButtons;
		}
	}

QSqlRecord TSqlTableNavigator::newRecord()

{
	QSqlRecord r;

	if (_delegate)
		r = _delegate->newRecord(this);
	if (r.isEmpty() && _model)
		r = _model->record();
	return r;
	}
