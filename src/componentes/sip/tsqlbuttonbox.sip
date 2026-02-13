/*****************************************************************************
  TRUST COMPONENTS

  (C) Trustserver S. L., 2009

  Todos los derechos reservados.

  $Id: tcombobox.sip 156 2010-01-14 12:04:52Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/tcombobox.sip $
*****************************************************************************/

class TSqlButtonBox: QWidget {

%TypeHeaderCode
#include <TSqlButtonBox>
%End

public:
	enum Buttons { NoButton = 0, SaveButton = 1, DiscardButton = 2,
		       AddButton = 3, EditButton = 4, DeleteButton = 5 };
public:
	TSqlButtonBox(QWidget *parent /TransferThis/);

	~TSqlButtonBox();

	QPushButton	*button(Buttons b);

	bool isAddEnabled() const;
	bool isEditEnabled() const;
	bool isDeleteEnabled() const;
	bool isSaveEnabled() const;
	bool isDiscardEnabled() const;

	void setAddEnabled(bool enabled);
	void setEditEnabled(bool enabled);
	void setDeleteEnabled(bool enabled);
	void setSaveEnabled(bool enabled);
	void setDiscardEnabled(bool enabled);
signals:
	void clicked(int b, bool checked);
	void saveClicked(bool checked);
	void discardClicked(bool checked);
	void addClicked(bool checked);
	void editClicked(bool checked);
	void deleteClicked(bool checked);
	};

