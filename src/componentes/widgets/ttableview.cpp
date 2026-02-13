/*****************************************************************************
  TRUST COMPONENTS

  (C) Trustserver S. L., 2009

  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: ttableview.cpp 221 2010-04-08 13:52:02Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/widgets/ttableview.cpp $");

#include "ttableview.h"

TTableView::TTableView (
	QWidget	*parent
	) :
	QTableView(parent)

{
	}

TTableView::~TTableView()

{
	}

void TTableView::setSelectionModel (
	QItemSelectionModel	*selectionModel
	)

{
	QItemSelectionModel *s = this->selectionModel();

	if (s != NULL)
		disconnect(s, SIGNAL(selectionChanged(const QItemSelection &, const QItemSelection &)),
			this, SLOT(internalSelectionChanged(const QItemSelection &, const QItemSelection)));

	QTableView::setSelectionModel(selectionModel);
	connect(selectionModel, SIGNAL(selectionChanged(const QItemSelection &, const QItemSelection &)),
		this, SLOT(internalSelectionChanged(const QItemSelection &, const QItemSelection &)));
	}

void TTableView::internalSelectionChanged (
	const QItemSelection	&selected,
	const QItemSelection	&deselected
	)

{
	emit selectionChanged(selected, deselected);
	}
