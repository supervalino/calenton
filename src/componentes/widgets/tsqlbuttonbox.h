/*****************************************************************************
  TRUST COMPONENTS

  (C) Trustserver S. L., 2009

  Todos los derechos reservados.

  $Id: tsqlbuttonbox.h 221 2010-04-08 13:52:02Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/widgets/tsqlbuttonbox.h $
*****************************************************************************/

#ifndef TSQLBUTTONBOX_H
#define TSQLBUTTONBOX_H

#include "ui_tsqlbuttonbox.h"

class TSqlButtonBox: public QWidget, private Ui::TSqlButtonBox {
	Q_OBJECT
	Q_PROPERTY(bool addEnabled READ isAddEnabled WRITE setAddEnabled)
	Q_PROPERTY(bool editEnabled READ isEditEnabled WRITE setEditEnabled)
	Q_PROPERTY(bool deleteEnabled READ isDeleteEnabled WRITE setDeleteEnabled)
	Q_PROPERTY(bool saveEnabled READ isSaveEnabled WRITE setSaveEnabled)
	Q_PROPERTY(bool discardEnabled READ isDiscardEnabled WRITE setDiscardEnabled)
public:
	enum Buttons { NoButton = 0, SaveButton = 1, DiscardButton = 2,
		       AddButton = 3, EditButton = 4, DeleteButton = 5 };
public:
	TSqlButtonBox(QWidget *parent);

	~TSqlButtonBox();

	QPushButton	*button(Buttons b);

	bool isAddEnabled() const { return addButton->isEnabled(); }
	bool isEditEnabled() const { return editButton->isEnabled(); }
	bool isDeleteEnabled() const { return deleteButton->isEnabled(); }
	bool isSaveEnabled() const { return saveButton->isEnabled(); }
	bool isDiscardEnabled() const { return discardButton->isEnabled(); }

	void setAddEnabled(bool enabled) { addButton->setEnabled(enabled); }
	void setEditEnabled(bool enabled) { editButton->setEnabled(enabled); }
	void setDeleteEnabled(bool enabled) { deleteButton->setEnabled(enabled); }
	void setSaveEnabled(bool enabled) { saveButton->setEnabled(enabled); }
	void setDiscardEnabled(bool enabled) { discardButton->setEnabled(enabled); }

signals:
	void clicked(int b, bool checked);
	void saveClicked(bool checked);
	void discardClicked(bool checked);
	void addClicked(bool checked);
	void editClicked(bool checked);
	void deleteClicked(bool checked);
private slots:
	void on_saveButton_clicked(bool checked);
	void on_discardButton_clicked(bool checked);
	void on_addButton_clicked(bool checked);
	void on_editButton_clicked(bool checked);
	void on_deleteButton_clicked(bool checked);
	};

#endif // TSQLBUTTONBOX_H
