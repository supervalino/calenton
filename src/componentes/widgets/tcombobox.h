/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: tcombobox.h 156 2010-01-14 12:04:52Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/widgets/tcombobox.h $
*****************************************************************************/

#ifndef TCOMBOBOX_H
#define TCOMBOBOX_H

#include <QComboBox>

class TComboBox : public QComboBox {
	Q_OBJECT
	Q_PROPERTY(QVariant currentItemData READ currentItemData WRITE setCurrentItemData)
public:
	TComboBox(QWidget *parent = 0): QComboBox(parent) {}
	~TComboBox() {}
	
	QVariant	currentItemData(int role = Qt::UserRole) const { return itemData(currentIndex(), role); }
	void		setCurrentItemData(QVariant currentItemData);
	};
	
#endif // TCOMBOBOX_H
