/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: magnitude.cpp 200 2010-03-01 17:03:06Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/base/magnitude.cpp $");

#include "magnitude.h"
#include <stdio.h>
#include <UnitSystem>
#include <Dimension>
#include <Unit>

QVariant::Type Magnitude::_typeId = QVariant::Invalid;

Magnitude::Magnitude (
	const QString	&s
	)
	
{
	allClean();
	UnitSystem *unitSystem = UnitSystem::defaultUnitSystem();
	if (unitSystem == NULL)
		return;
	if (s.isEmpty()) 
		return;
	QStringList sl = s.split("|");
	if (sl.count() < 2) 
		return;
	const Unit *unit = unitSystem->unit(sl.at(0), sl.at(1));
	if (unit == NULL) 
		return;
	_unit = unit;
	_correct = true;
	_corrupt = false;
	
	if (sl.count() == 2)
		return;
	bool good;
	double value = sl.at(2).toDouble(&good);
	if (!good)
		return;
	_value = value;
	_empty = false;	
	}

Magnitude::Magnitude (
	const QString	&dimension,
	const QString	&unit,
	double		value
	)
	
{
	allClean();
	UnitSystem *unitSystem = UnitSystem::defaultUnitSystem();
	if (unitSystem == NULL)
		return;
	const Unit *u = unitSystem->unit(dimension, unit);
	if (u == NULL)
		return;
	_unit = u;
	_correct = true;
	_corrupt = false;
	_value = value;
	_empty = false;
	}
	
/*!
    \a value es convertido a un double y se asigna al valor de la
    magnitud, si la conversión no es correcta, la magnitud queda en estado
    incorrecto
 */
    
void Magnitude::setValue(QString value)

{
	if (!_corrupt) {
		if (value.isEmpty()) {
			_value = 0.0;
			_empty = true;
			_correct = true;
			}
		else {
			_value = value.toDouble(&_correct);
			_empty = !_correct;
			}
		}
	}

void Magnitude::registerMetaType()

{
	_typeId = QVariant::Type(qRegisterMetaType<Magnitude>("Magnitude"));
//	qDebug() << "Registrado tipo para Magnitude: " << int(_typeId);
	}
	
QString	Magnitude::toString() const

{
	if (empty() || _corrupt || (!_correct) || (_unit == NULL))
		return QString();
	Magnitude m2;
	m2 = toDefaultUnit();
	if (m2.empty())
		m2 = *this;
	QString res = QString("%1 %2").arg(m2._value, 0, 'f', m2._unit->prec()).arg(m2._unit->name());
	return res;
	}

QString	Magnitude::toStorableString()

{
	if (_unit == NULL)
		return QString();
	QString f = QString("%1|%2").arg(_unit->dimension()->name()).arg(_unit->name());
	if (empty())
		return f;
	QString res = QString("%2|%3").arg(f).arg(_value);
	return res;
	}
	
Magnitude	Magnitude::fromStorableString (
	const QString	&storableString,
	UnitSystem	*unitSystem
	)
	
{
	if (unitSystem == NULL)
		unitSystem = UnitSystem::defaultUnitSystem();
	if (unitSystem == NULL)
		return Magnitude();
	if (storableString.isEmpty())
		return Magnitude();
	QStringList sl = storableString.split("|");
	if (sl.count() < 2)
		return Magnitude();
	const Unit *unit = unitSystem->unit(sl.at(0), sl.at(1));
	if (unit == NULL)
		return Magnitude();
	Magnitude res(unit);
	if (sl.count() == 2)
		return res;
	bool good;
	double value = sl.at(2).toDouble(&good);
	if (!good)
		return res;
	res.setValue(value);
	return res;	
	}

void	Magnitude::setUnit (
	const QString	&unitName
	)
	
{
	if (_unit == 0)
		return;
	const Dimension *d = _unit->dimension();
	const Unit *u = d->unit(unitName);
	setUnit(u);
	}

double	Magnitude::convert (
	const QString	&unitName
	) const
	
{
	const Unit	*u;
	
	if (!_correct || _corrupt)
		return 0.0;
	u = _unit->dimension()->unit(unitName);
	if (u == 0)
		return 0.0;
	return this->convert(u);
	}

void	Magnitude::transform (
	const QString	&unitName
	)
	
{
	const Unit	*u;
	
	if (!_correct || _corrupt)
		return;
	u = _unit->dimension()->unit(unitName);
	if (u == 0)
		return;
	this->transform(u);
	}

Magnitude	Magnitude::toUnit (
	const QString	&unitName
	) const
	
{
	const Unit	*u;
	
	if (!_correct || _corrupt)
		return Magnitude();
	u = _unit->dimension()->unit(unitName);
	if (u == 0)
		return Magnitude();
	double v = this->convert(u);
	return Magnitude(v, u);
	}

Magnitude	Magnitude::toDefaultUnit() const
	
{
	const Unit	*u;
	
	if (!_correct || _corrupt)
		return Magnitude();
	UnitSystem *unitSystem = UnitSystem::defaultUnitSystem();
	if (unitSystem == NULL)
		return Magnitude();
	u = unitSystem->unit(_unit->dimension()->name());
	if (u == 0)
		return Magnitude();
	double v = this->convert(u);
	return Magnitude(v, u);
	}
