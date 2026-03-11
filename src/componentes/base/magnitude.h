/*****************************************************************************
  TRUST COMPONENTS

  (C) Trustserver S. L., 2009

  Todos los derechos reservados.

  $Id: magnitude.h 136 2009-10-27 14:33:46Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/base/magnitude.h $
*****************************************************************************/

#ifndef MAGNITUDE_H
#define MAGNITUDE_H

#include <Unit>
#include <Dimension>
#include <QMetaType>
#include <QVariant>

class UnitSystem;

/*!
    \brief Representa un valor con dimensiones.

    Representa una medida de una dimensión.  Cada medida se representan
    mediante un valor y una unidad de medida.
 */

class Magnitude {
private:
	static int		_typeId;

	double		_value;
	const Unit	*_unit;
	bool		_empty;
	bool		_correct;
	bool		_corrupt;
public:
	/*! Crea una magnitud incorrecta (sin unidades) */
	Magnitude() :
		_value(0.0), _unit(nullptr), _empty(true), _correct(false), _corrupt(true) {}

	/*! Crea una magnitud medida en la unidad \a unit, pero sin valor */
	Magnitude(const Unit *unit) :
		_value(0.0), _unit(unit), _empty(true), _correct(unit != nullptr), _corrupt(unit == nullptr) {}

	/*! Crea una magnitud con valor \a value y unidad de medida \a unit */
	Magnitude(double value, const Unit *unit) :
		_value(value), _unit(unit), _empty(unit == nullptr), _correct(unit != nullptr), _corrupt(unit == nullptr) {}

	/*! Copia la magnitud */
	Magnitude(const Magnitude &m) :
		_value(m._value), _unit(m._unit), _empty(m._empty), _correct(m._correct), _corrupt(m._corrupt) {}

	Magnitude(const QString &dimension, const QString &unit, double value);

	Magnitude(const QString &s);

	/*! Destruye el objeto */
	~Magnitude() {}

	/*! Devuelve el valor de la magnitud */
	double value() const { return _value; }

	/*! Devuelve cierto si no tiene valor */
	bool empty() const { return _empty; }

	/*! Deja la magnitud sin valor */
	void clean() { _empty = true; _corrupt = (_unit == nullptr); _correct = !_corrupt; }

	void allClean() { _value = 0.0; _unit = nullptr; _empty = true; _correct = false; _corrupt = true; }

	/*! Fija la unidad de la magnitud */
	void setUnit(const Unit *unit) { _unit = unit; _empty = true; _corrupt = (_unit == nullptr); _correct = !_corrupt; }

	void setUnit(const QString &unitName);

	/*! Devuelve cierto si la unidad de medida asociada es correcta y el valor que
	    se ha intentado fijar tambi�n */
	bool correct() const { return _correct; }

	/*! !correct() */
	bool incorrect() const { return !_correct; }

	/*! Devuelve cierto si la unidad de medida no es correcta. */
	bool corrupt() const { return _corrupt; }

	/*! Devuelve cierto si el valor sirve para algo. */
	bool usefull() const { return !_corrupt && _correct && !_empty; }

	/*! Devuelve la unidad de medida de una magnitud */
	const Unit *unit() const { return _unit; }

	/*! Cambia la unidad de medida de una magnitud y transforma el valor
	    a la nueva unidad de medida */
	void transform(const Unit *unit) { if (_correct && (!_corrupt)) { _value = _unit->convert(_value, unit); _unit = unit; } }

	/*! Cambia la unidad de medida de una magnitud y transforma el valor
	    a la nueva unidad de medida */
	void transform(const QString &unit);

	/*! Devuelve el valor de esta magnitud en la unidad de medida
	    \a unit */
	double convert(const Unit *unit) const { return ((_correct && (!_corrupt)) ? _unit->convert(_value, unit) : 0.0); }

	/*! Devuelve el valor de esta magnitud en la unidad de medida
	    de nombre \a unitName */
	double convert(const QString &unitName) const;

	/*! Devuelve el valor de esta magnitud en la unidad de medida
	    de nombre \a unitName */
	Magnitude toUnit(const QString &unitName) const;

	/*! Devuelve el valor de esta magnitud en la unidad de medida
	    de nombre \a unitName */
	Magnitude toDefaultUnit() const;

	/*! Devuelve el valor de esta magnitud en la unidad de medida principal
	    de la dimension */
	double toMain() const { return ((_correct && (!_corrupt)) ? this->convert(_unit->dimension()->mainUnit()) : 0.0); }

	/*! Fija el valor de la magnitud al valor \a value en la unidad de medida
	    actual */
	void setValue(double value) { if (!_corrupt) { _value = value; _empty = false; } }

	void setValue(QString value);

	/*! Fija el valor y unidad de medida de una magnitud */
	void setMagnitude(double value, const Unit *unit) {
		_value = value; _unit = unit; _empty = (unit == nullptr); _correct = (unit != nullptr); _corrupt = !_correct; }

	QString toString() const;

	QString 		toStorableString();
	static Magnitude	fromStorableString(const QString &storableString,
					UnitSystem *unitSystem = nullptr);

	static int		typeId() { return _typeId; }
	static void		registerMetaType();
	};

Q_DECLARE_METATYPE(Magnitude);

#endif // MAGNITUDE_H
