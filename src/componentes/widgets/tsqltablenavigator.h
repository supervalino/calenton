/*****************************************************************************
  TRUST COMPONENTS

  (C) Trustserver S. L., 2009

  Todos los derechos reservados.

  $Id: tsqltablenavigator.h 228 2010-04-21 15:36:53Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/widgets/tsqltablenavigator.h $
*****************************************************************************/

#ifndef TSQLTABLENAVIGATOR_H
#define TSQLTABLENAVIGATOR_H

#include "ui_tsqltablenavigator.h"
#include <QPointer>
#include <QSqlRecord>

class SeqTableModel;
class DataDialog;

class TSqlTableNavigator: public QWidget, private Ui::TSqlTableNavigator {
	Q_OBJECT
	Q_PROPERTY(bool autoResizeRows READ isAutoResizeRows WRITE setAutoResizeRows)
	Q_PROPERTY(bool autoResizeColumns READ isAutoResizeColumns WRITE setAutoResizeColumns)
	Q_PROPERTY(bool showButtons READ showButtons WRITE setShowButtons)
	Q_PROPERTY(QAbstractItemView::EditTriggers editTriggers READ editTriggers WRITE setEditTriggers)
	Q_PROPERTY(bool alternatingRowColors READ alternatingRowColors WRITE setAlternatingRowColors)
	Q_PROPERTY(QAbstractItemView::SelectionMode selectionMode READ selectionMode WRITE setSelectionMode)
	Q_PROPERTY(QAbstractItemView::SelectionBehavior selectionBehavior READ selectionBehavior WRITE setSelectionBehavior)
public:
	class Delegate : public QObject {
	public:
		Delegate(QObject *parent) : QObject(parent) {}
		virtual bool couldAdd(TSqlTableNavigator * /* nav */ ) { return true; };
		virtual DataDialog *createEditor(TSqlTableNavigator * /* nav */) { return NULL; }
		virtual QSqlRecord newRecord(TSqlTableNavigator * /* nav */) { return QSqlRecord(); }
		};
private:
	bool			_autoResizeRows;
	bool			_autoResizeColumns;
	bool			_showButtons;
	int			_selectedId;
	bool			_modelDirty;
	SeqTableModel		*_model;
	QPointer<Delegate>	_delegate;
public:
	TSqlTableNavigator(QWidget *parent);

	~TSqlTableNavigator();

	bool isAutoResizeRows() const { return _autoResizeRows; }
	bool isAutoResizeColumns() const { return _autoResizeColumns; }
	bool showButtons() const { return _showButtons; }
	QAbstractItemView::EditTriggers editTriggers() const {
		return uiTableView ? uiTableView->editTriggers() : QAbstractItemView::NoEditTriggers; }
	QAbstractItemView::SelectionMode selectionMode() const {
		return uiTableView ? uiTableView->selectionMode() : QAbstractItemView::NoSelection; }
	QAbstractItemView::SelectionBehavior selectionBehavior() const {
		return uiTableView ? uiTableView->selectionBehavior() : QAbstractItemView::SelectItems; }
	bool alternatingRowColors() const { return uiTableView ? uiTableView->alternatingRowColors() : false; }

	void setAutoResizeRows(bool autoResizeRows) { _autoResizeRows = autoResizeRows; }
	void setAutoResizeColumns(bool autoResizeColumns) { _autoResizeColumns = autoResizeColumns; }
	void setShowButtons(bool showButtons);
	void setEditTriggers(QAbstractItemView::EditTriggers et) { if (uiTableView) uiTableView->setEditTriggers(et); }
	void setSelectionMode(QAbstractItemView::SelectionMode sm) { if (uiTableView) uiTableView->setSelectionMode(sm); }
	void setSelectionBehavior(QAbstractItemView::SelectionBehavior sm) { if (uiTableView) uiTableView->setSelectionBehavior(sm); }
	void setAlternatingRowColors(bool ac) { if (uiTableView) uiTableView->setAlternatingRowColors(ac); }

	SeqTableModel	*model() { return _model; }
	void		setModel(SeqTableModel *model);

	int	selectedId() const { return _selectedId; }

	Delegate	*delegate() { return _delegate; }
	void		setDelegate(Delegate *delegate);

	TTableView	*tableView() { return uiTableView; }
	TSqlButtonBox	*buttonBox() { return uiButtonBox; }
signals:
	void	idChanged(int newId);
	void	dirtyChanged(bool dirty);

public slots:
	void	setParentId(int id);
	void	setFilter(const QString &filter);

private slots:
	void	on_uiTableView_selectionChanged(const QItemSelection &selected, const QItemSelection &deselected);
	void	on_uiTableView_doubleClicked(const QModelIndex &index);
	void	on_uiButtonBox_addClicked(bool checked);
	void	on_uiButtonBox_deleteClicked(bool checked);
	void	on_uiButtonBox_discardClicked(bool checked);
	void	on_uiButtonBox_editClicked(bool checked);
	void	on_uiButtonBox_saveClicked(bool checked);

private:
	void		updateContent();
	bool		couldAdd();
	DataDialog	*createEditor();
	void		resizeIfNeeded();
	QSqlRecord	newRecord();
	};

#endif // TSQLTABLENAVIGATOR_H
