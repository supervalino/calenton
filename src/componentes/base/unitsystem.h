/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: unitsystem.h 139 2009-11-06 10:20:33Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/base/unitsystem.h $
*****************************************************************************/

#ifndef UNITSYSTEM_H
#define UNITSYSTEM_H

#include <QMap>
#include <QString>
#include <QDomDocument>
#include <QDomElement>
#include <QStringList>

class Dimension;
class UnitCollection;
class Unit;

class UnitSystem {
public:
	typedef QMap<QString, Dimension *> DimensionMap;
	typedef QMap<QString, UnitCollection *> UnitCollectionMap;
private:
	static UnitSystem	*_defaultUnitSystem;
	
	DimensionMap		_dimensions;
	UnitCollectionMap	_collections;
	UnitCollection		*_defaultCollection;
public:
	UnitSystem();
	UnitSystem(QString configFile);
	~UnitSystem();

	Dimension *getDimension(QString name);

	void		addDimension(Dimension *dimension);
	bool		setDefaultUnitCollection(QString name);
	UnitCollection	*defaultUnitCollection();
	const Unit	*unit(QString dimension, QString unitName = QString()) const;
	QStringList	getAllUnitCollections();
	DimensionMap	getAllDimensions() { return _dimensions; }
	QStringList	getAllDimensionsList() { return _dimensions.keys(); }
	
	static void		setDefaultUnitSystem(UnitSystem *unitSystem) { _defaultUnitSystem = unitSystem; }
	static UnitSystem	*defaultUnitSystem() { return _defaultUnitSystem; }
private:
	void		addDimension(QDomElement &el);
	void		addUnitCollection(QDomElement &el);
	void		addXml(QDomDocument &doc);
	};
	
#endif // UNITSYSTEM_H
