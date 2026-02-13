/*****************************************************************************
  TRUST COMPONENTS

  (C) Trustserver S. L., 2009

  Todos los derechos reservados.
*****************************************************************************/
#include "hdr.h"

ID_ID("$Id: tsqlbuttonbox.cpp 214 2010-04-06 08:24:03Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/widgets/tsqlbuttonbox.cpp $");

#include <TSqlButtonBox>

TSqlButtonBox::TSqlButtonBox (
	QWidget	*parent
	) :
	QWidget(parent)

{
	setupUi(this);
	}

TSqlButtonBox::~TSqlButtonBox()

{
	}

QPushButton	*TSqlButtonBox::button (
	Buttons	b
	)

{
	switch (b) {
		case SaveButton: return saveButton;
		case DiscardButton: return discardButton;
		case AddButton: return addButton;
		case EditButton: return editButton;
		case DeleteButton: return deleteButton;
		default: return NULL;
		}
	}

void TSqlButtonBox::on_saveButton_clicked (
	bool checked
	)

{
	emit clicked(SaveButton, checked);
	emit saveClicked(checked);
	}

void TSqlButtonBox::on_discardButton_clicked (
	bool checked
	)

{
	emit clicked(DiscardButton, checked);
	emit discardClicked(checked);
	}

void TSqlButtonBox::on_addButton_clicked (
	bool checked
	)

{
	emit clicked(AddButton, checked);
	emit addClicked(checked);
	}

void TSqlButtonBox::on_editButton_clicked (
	bool checked
	)

{
	emit clicked(EditButton, checked);
	emit editClicked(checked);
	}

void TSqlButtonBox::on_deleteButton_clicked (
	bool checked
	)

{
	emit clicked(DeleteButton, checked);
	emit deleteClicked(checked);
	}

