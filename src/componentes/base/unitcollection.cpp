/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: unitcollection.cpp 131 2009-10-27 11:59:22Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/base/unitcollection.cpp $");

#include "unitcollection.h"

/*!
    \class UnitCollection unitcollection.h
    \brief Describe un sistema métrico (SI, británico...).

    Permite definir que unidades de medida se utilizan para las
    distintas dimensiones en un sistemas métrico y proporciona
    técnicas de enumeración de éstas.

    \sa UnitSystem, Dimension, Unit
 */

/*! Crea un nuevo sistema métrico de nombre \a name */

UnitCollection::UnitCollection (
	QString	name
	) :
	_units(),
	_name(name)

{
	}

/*! Destruye el objeto.  Las unidades asociadas a este
    sistema métrico no se destruyen. */
    
UnitCollection::~UnitCollection()

{
	}

/*! Aade la unidad \a unit al sistema métrico como unidad por
    defecto de la dimension de nombre \a dimension */
    
void UnitCollection::addUnit (
	QString		dimension,
	const Unit	*unit
	)

{
	_units.insert(dimension, unit);
	}

/*! Devuelve la unidad por defecto para la dimension de nombre
    \a dimension */
    
const Unit *UnitCollection::getUnit (
	QString dimension
	)

{
	return _units.value(dimension, 0);
	}
