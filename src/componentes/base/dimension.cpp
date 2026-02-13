/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: dimension.cpp 131 2009-10-27 11:59:22Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/base/dimension.cpp $");

#include "dimension.h"

/*!
    \class Dimension dimension.h
    \brief Representa una dimensi�n que se puede medir (longitud, tiempo).

    Cada dimensión puede tener distintas unidades de medida,
    este objeto mantiene información de las distintas unidades
    para esta dimensión y permite convertir valores entre
    ellas.

    \sa Unit
 */

/*! Crea una dimensión con nombre \a name */

Dimension::Dimension (
	QString name,
	QString description
	) :
	_units(),
	_mainUnit(0),
	_name(name),
	_description(description)

{
	}

/*!
    Destruye el objeto y todos los elementos asociados.  Destruye todas las
    unidades de medida de esta dimensión, por lo que ya no podrán seguir
    utilizándose
 */

Dimension::~Dimension()

{
	for (UnitMap::const_iterator i = _units.begin(); i != _units.end(); ++i)
		delete i.value();
	_units.clear();
	_mainUnit = 0;
	}

/*!
    Añade una unidad a esta dimensión, con nombre \a name y definida
    respecto a la unidad principal por los parámetros \a ratio y \a
    offset.  Si \a main es true, entonces esta unidad será la
    principal
 */

void Dimension::addUnit (
	QString	name,
	double	ratio,
	double	offset,
	bool	main,
	int	prec
	)

{
	Unit *n = new Unit(this, name, ratio, offset, prec);
	_units.insert(name, n);
	if (main)
		_mainUnit = n;
	}

/*!
    Convierte el valor \a value expresado en la unidad \a from a la unidad
    \a to.  No se verifica que las dos unidades representen la misma
    unidad.
 */
 
double Dimension::convert (
	const Unit	*from,
	const Unit	*to,
	double		value
	) const

{
	double mainValue = from->from(value);
	return to->to(mainValue);
	}

/*!
    Convierte el valor \a value expresado en la unidad de medida de nombre
    \a from a la unidad de medida de nombre \a to
 */
 
double Dimension::convert (
	QString	from,
	QString	to,
	double	value
	) const

{
	Unit *f = _units.value(from, 0);
	Unit *t = _units.value(to, 0);
	if ((t != 0) && (f != 0))
		return convert(f, t, value);
	else
		return 0.0;
	}

/*!
    Convierte el valor \a value expresado en la unidad \a from a la unidad de
    medida de nombre \a to.  No se verifica que \a from represente a esta dimensión.
 */
double Dimension::convert (
	const Unit	*from,
	QString		to,
	double		value
	) const

{
	Unit *t = _units.value(to, 0);

	if (t != 0)
		return convert(from, t, value);
	else
		return 0.0;
	}
