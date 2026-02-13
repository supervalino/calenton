/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: tcombobox.sip 156 2010-01-14 12:04:52Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/tcombobox.sip $
*****************************************************************************/

class TComboBox : QComboBox {

%TypeHeaderCode
#include <TComboBox>
%End

public:
	TComboBox(QWidget *parent /TransferThis/ = 0);
	~TComboBox();
	
	QVariant	currentItemData(int role = Qt::UserRole) const;
	void		setCurrentItemData(QVariant currentItemData);
	};
