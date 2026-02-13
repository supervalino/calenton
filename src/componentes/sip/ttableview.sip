/*****************************************************************************
  TRUST COMPONENTS

  (C) Trustserver S. L., 2009

  Todos los derechos reservados.

  $Id: tcombobox.sip 156 2010-01-14 12:04:52Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/tcombobox.sip $
*****************************************************************************/

class TTableView: QTableView {

%TypeHeaderCode
#include <TTableView>
%End

public:
	TTableView(QWidget *parent /TransferThis/ = 0);
	~TTableView();

	virtual void	setSelectionModel(QItemSelectionModel *selectionModel /KeepReference/);

signals:
	void selectionChanged(const QItemSelection &selected, const QItemSelection &deselected);
	};

