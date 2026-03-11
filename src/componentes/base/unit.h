/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: unit.h 131 2009-10-27 11:59:22Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/base/unit.h $
*****************************************************************************/

#ifndef UNIT_H
#define UNIT_H

#include <QString>

class Dimension;

/*!
    \brief Representa una unidad de medida.

    Un objeto \a Unit representa una unidad de medida (por
    ejemplo metros, kilogramos, segundos o culombios) de
    una dimensi�n representada por un objeto \link Dimension
    Dimension \endlink (por ejemplo longitud, masa, tiempo
    o carga eléctrica).

    Cada dimensión tiene una unidad principal y el resto de
    las unidades de medida se relacionan con la principal mediante
    \a ratio y \a offset.

    \code
      valor en unidad principal = (valor - offset) / ratio
      valor = ratio * valor en unidad principal + offset
    \endcode
    
    La conversión entre la unidad principal y la representada por
    el objeto se hace con los métodos
    \link Unit::to() to() \endlink que convierte de la principal
    a esta unidad y \link Unit::from() from() \endlink que convierte
    de esta unidad a la principal.

    Una magnitud medida junto con la unidad de medida utilizada
    se representa mediante un objeto \link Magnitude Magnitude
    \endlink.

    Un conjunto de unidades de medida forma un sistema de medida
    y se representa mediante un objeto \link UnitCollection
    UnitCollection \endlink.  El conjunto de todas las unidades
    de medida soportadas por el sistema se representa mediante
    un objeto \link UnitSystem UnitSystem \endlink

    Las unidades se describen en un fichero unidades.xml que debe
    estar en el directorio de configuración de la aplicación.  El
    formato de este fichero se describe en \link UnitSystem
    UnitSystem \endlink.
    
    \sa Dimension Magnitude UnitCollection UnitSystem
 */
 
class Unit {
private:
	Dimension	*_dimension;
	QString		_name;
	double		_ratio;
	double		_offset;
	double		_invRatio;
	int		_prec;		
public:
        /*! Crea una unidad para medir la \a dimension, con nombre \a name.  La
            relación con la dimensión principal se define por \a ratio y
            \a offset */
	Unit(Dimension *dimension, QString name, double ratio, double offset, int prec) :
		_dimension(dimension), _name(name), _ratio(ratio), _offset(offset),
		_invRatio(1.0 / ratio), _prec(prec) {}

	/*! Destruye la unidad de medida. */
	~Unit() {}

	/*! Convierte el valor \a n medido en la unidad principal a esta
	    unidad de medida */
	double to(double n) const { return (n  * _ratio + _offset); }

	/*! Convierte el valor \a n medido en esta unidad de medida
	    a la unidad de medida principal */
	double from(double n) const { return (n - _offset) * _invRatio; }

	/*! Devuelve el nombre de la unidad de medida */
	QString name() const { return _name; }
	
	/*! Devuelve la precisión preferida para esta unidad */
	int prec() const { return _prec; }

	/*! Devuelve la dimensión que mide esta unidad */
	const Dimension *dimension() const { return _dimension; }

	/*! Convierte el valor \a value medido en esta unidad
	    de medida a la unidad de medida \a unit.  Si estas dos
	    unidades no miden la misma dimensión el resultado no tendrá
	    ningún significado físico */
	double convert(double value, const Unit *unit) const { return (unit != nullptr) ? unit->to(this->from(value)) : 0.0; }
	};
	
#endif // UNIT_H
