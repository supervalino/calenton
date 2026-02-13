/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include "hdr.h"

ID_ID("$Id: tcombobox.cpp 156 2010-01-14 12:04:52Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/widgets/tcombobox.cpp $");

#include <TComboBox>

void TComboBox::setCurrentItemData (
	QVariant	currentItemData
	)
	
{
	int	i;
	
	for (i = 0; i < count(); i++) {
		QVariant d = itemData(i);
		if (currentItemData == d) {
			setCurrentIndex(i);
			break;
			}
		}
	}

