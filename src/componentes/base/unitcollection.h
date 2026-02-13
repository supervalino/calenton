/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: unitcollection.h 131 2009-10-27 11:59:22Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/base/unitcollection.h $
*****************************************************************************/

#ifndef UNITCOLLECTION_H
#define UNITCOLLECTION_H

#include <QMap>
#include <QString>

class Unit;

class UnitCollection {
public:
	typedef QMap<QString, const Unit *> UnitMap;
private:
	UnitMap	_units;
	QString	_name;

	UnitCollection();
public:
	UnitCollection(QString name);
	~UnitCollection();

	void		addUnit(QString dimension, const Unit *unit);
	const Unit	*getUnit(QString dimension);
	const QString	&name() { return _name; }
	};
	
#endif // UNITCOLLECTION_H
