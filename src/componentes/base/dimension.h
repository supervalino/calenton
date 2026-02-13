/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: dimension.h 139 2009-11-06 10:20:33Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/base/dimension.h $
*****************************************************************************/

#ifndef DIMENSION_H
#define DIMENSION_H

#include <Unit>
#include <QString>
#include <QMap>
#include <QStringList>

class Dimension {
public:
	/*! Tipo de datos para el QMap que relaciona el nombre
	    de una unidad de medida con el objeto que la representa */
	typedef QMap<QString, Unit *> UnitMap;
private:
	UnitMap		_units;
	Unit		*_mainUnit;
	const Unit	*_defaultUnit;
	QString		_name;
	QString		_description;
public:
	Dimension(QString name, QString description);
	~Dimension();

	/*! Devuelve el nombre de la dimension */
	QString name() const { return _name; }
	/*! Devuelve la descripción de la dimension */
	QString description() const { return _description; }
	void addUnit(QString name, double ratio, double offset, bool main, int prec);
	double convert(QString from, QString to, double value) const;
	double convert(const Unit *from, const Unit *to, double value) const;
	double convert(const Unit *from, QString to, double value) const;

	/*! Devuelve la unidad de medida de esta dimensión que tiene
	    nombre \a name */
	const Unit *unit(const QString &name) const { return _units.value(name, 0); }
	
	const Unit *defaultUnit() const { return _defaultUnit; }
	void	setDefaultUnit(const Unit *defaultUnit) { _defaultUnit = defaultUnit; }

	/*! Devuelve el QMap<QString, Unit *> con todas las unidades de medida de esta
	    dimensión.  El QMap va indexado por el nombre de la unidad */
	const UnitMap &units() const { return _units; }
	
	QStringList	unitNames() const { return _units.keys(); }

	/*! Devuelve la unidad principal de esta dimensión */
	const Unit *mainUnit() const { return _mainUnit; }
	};
	
#endif // DIMENSION_H
