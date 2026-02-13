/*****************************************************************************
  TRUST COMPONENTS

  (C) Trustserver S. L., 2009

  Todos los derechos reservados.

  $Id: seqtablemodel.sip 207 2010-03-23 21:41:36Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/seqtablemodel.sip $
*****************************************************************************/


class TSqlTableNavigator: QWidget {

%TypeHeaderCode
#include <TSqlTableNavigator>
%End

public:

	class Delegate : QObject {

%TypeHeaderCode
#include <TSqlTableNavigator>
%End

	public:
		Delegate(QObject *parent /TransferThis/);
		virtual bool couldAdd(TSqlTableNavigator *nav);
		virtual DataDialog *createEditor(TSqlTableNavigator *nav) /Transfer/;
		virtual QSqlRecord newRecord(TSqlTableNavigator * /* nav */);
		};
public:
	TSqlTableNavigator(QWidget *parent /TransferThis/);

	~TSqlTableNavigator();

	bool isAutoResizeRows() const;
	bool isAutoResizeColumns() const;
	bool showButtons() const;
	QAbstractItemView::EditTriggers editTriggers() const;
	QAbstractItemView::SelectionMode selectionMode() const;
	QAbstractItemView::SelectionBehavior selectionBehavior() const;
	bool alternatingRowColors() const;

	void setAutoResizeRows(bool autoResizeRows);
	void setAutoResizeColumns(bool autoResizeColumns);
	void setShowButtons(bool showButtons);
	void setEditTriggers(QAbstractItemView::EditTriggers et);
	void setSelectionMode(QAbstractItemView::SelectionMode sm);
	void setSelectionBehavior(QAbstractItemView::SelectionBehavior sm);
	void setAlternatingRowColors(bool ac);

	SeqTableModel	*model();
	void		setModel(SeqTableModel *model);

	int	selectedId() const;

	Delegate	*delegate();
	void		setDelegate(Delegate *delegate /Transfer/);

	TTableView	*tableView();
	TSqlButtonBox	*buttonBox();
signals:
	void	idChanged(int newId);
	void	dirtyChanged(bool dirty);

public slots:
	void	setParentId(int id);
	void	setFilter(const QString &filter);
	};
