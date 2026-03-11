/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: unitsystem.cpp 200 2010-03-01 17:03:06Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/base/unitsystem.cpp $");

#include "unitsystem.h"
#include "unitcollection.h"
#include <Dimension>
#include <QDomNodeList>
#include <QDomDocument>
#include <QFile>
#include <QtDebug>

/*!
    \class UnitSystem unitsystem.h
    \brief Mantiene la base de datos de las dimensiones conocidas y sus unidades

    Es responsable de mantener toda la información sobre dimensiones, unidades
    y sistemas de medida.  No representa un sistema métrico, para esto ver
    \link UnitCollection UnitCollection \endlink.

    Esta clase tiene también el soporte para leer la configuracién de unidades
    de un fichero XML.

    Este fichero XML tiene un documentElement de tipo unitsystem, que contiene
    dos elementos: dimensions y systems, por lo que el fichero correcto más
    sencillo será:

    \code
    <unitsystem>
    <dimensions/>
    <systems/>
    </unitsystem>
    \endcode

    El elemento \a dimensions define las distintas dimensiones que se podrán
    medir y sus unidades, el elemento \a systems los distintos sistemas métricos.

    El elemento \a dimensions tiene un elemento para cada dimensión, que a su
    vez tiene distintos elementos para cada unidad de medida.  Cada unidad se
    define por su ratio y offset (ver \link Unit Unit \endlink), y la unidad
    principal tiene también un atributo \a main que lo indica, por ejemplo:

    \code
    <dimensions>
    <dimension name="temperature">
        <unit name="K" ratio="1" main="1"/>
        <unit name="ºC" ratio="1" offset="-273.15"/>
        <unit name="ºF" ratio="1.8" offset="-459.67"/>
        <unit name="ºR" ratio="1.8"/>
    </dimension>
    <dimension name="length">
        ....
    </dimension>
    <dimension name="energy">
        ....
    </dimension>
    </dimensions>
    \endcode

    Define la dimensión temperatura, con cuatro unidades de medida: Kelvin,
    Rankine, grados Farenheit y grados Celsius, la unidad principal es el
    Kelvin (unidad oficial del sistema internacional), por lo que ésta
    tiene marcado el atributo main, además se definen el resto mediante
    su ratio y offset en referencia a los Kelvin.  La unidad principal
    siempre tiene ratio="1" y offset="0".  El valor 0 para offset se
    asume por defecto.

    El elemento \a systems define los distintos sistemas métricos y
    sus unidades asociadas, por ejemplo:

    \code
    <systems>
    <system name="Sistema internacional">
        <dimension name="length" unit="m"/>
        <dimension name="mass" unit="kg"/>
        <dimension name="time" unit="s"/>
        <dimension name="pressure" unit="Pa"/>
        <dimension name="temperature" unit="K"/>
        <dimension name="flow" unit="m3/s"/>
        <dimension name="potential" unit="V"/>
        <dimension name="frecuency" unit="Hz"/>
        <dimension name="power" unit="w"/>
        <dimension name="energy" unit="J"/>
        <dimension name="humidity" unit="% HR"/>
        <dimension name="massflow" unit="kg/s"/>
        <dimension name="soundlevel" unit="dB"/>
        <dimension name="speed" unit="m/s"/>
    </system>
    <system name="Británico">
        ....
    </system>
    </systems>
    \endcode

    Se habría definido el "Sistema internacional" y tendríamos como unidad
    de medida de longitud el metro, de masa el kilogramo, de tiempo el
    segundo de presión el Pascal, de temperatura el Kelvin...  Todas
    las dimensiones y unidades deben estar definidas previamente dentro
    del elemento \a dimensions.
    
    \sa UnitCollection, Dimension, Unit, Magnitude
 */

UnitSystem *UnitSystem::_defaultUnitSystem = nullptr;

/*! Crea una nueva base de datos de unidades vacía */

UnitSystem::UnitSystem() : _defaultCollection(nullptr)

{
	}
	
/*! Crea una nueva base de datos de unidades y la configura con el contenido
    del fichero \a configFile */
    
UnitSystem::UnitSystem (
	QString	configFile
	) :
	_defaultCollection(nullptr)

{
//	qDebug() << "Leyendo sistema de medidas de: " << configFile;
	QDomDocument doc;
	QFile f(configFile);
	if (f.open(QIODevice::ReadOnly)) {
		doc.setContent(&f, false);
		}
	addXml(doc);
	}

/*! Destruye el objeto y todos los recursos asociados, inclu�das todas
    las dimensiones, unidades y sistemas métricos */

UnitSystem::~UnitSystem()

{
	for (const auto &d : _dimensions)
		delete d;
	_dimensions.clear();
	for (const auto &c : _collections)
		delete c;
	_collections.clear();
	_defaultCollection = nullptr;
	}

/*! Añade una dimensión de nombre \a dimension */

void UnitSystem::addDimension (
	Dimension	*dimension
	)
		
{
	_dimensions.insert(dimension->name(), dimension);
	}

/*!
    Añade una dimensión descrita por el elemento \a el leído desde
    el fichero de configuración unidades.xml.  Además de añadir la
    dimensión, añade todas las unidades descritas por \a el.
 */

void UnitSystem::addDimension (
	QDomElement	&el
	)

{
	QString name = el.attribute("name");
	if (name.isNull())
		return;
	QString desc = el.attribute("desc");
//	qDebug() << "Añado dimensión:" << name << ", con descripción: " << desc;
	Dimension *d = new Dimension(name, desc);
	QDomNodeList l = el.elementsByTagName("unit");
	for (int i = 0; i < l.count(); ++i) {
		QDomNode n = l.at(i);
		if (!n.isElement())
			continue;
		QDomElement e = n.toElement();
		QString uName = e.attribute("name");
		QString ratio = e.attribute("ratio");
		QString uMain = e.attribute("main");
		QString uOffset = e.attribute("offset");
		QString uPrec = e.attribute("prec");
		if (uName.isEmpty() || ratio.isEmpty())
			continue;
		bool conv;
		double dRatio = ratio.toDouble(&conv);
		if (!conv)
			continue;
		bool bMain = false;
		if (!uMain.isEmpty()) {
			int im = uMain.toInt(&conv);
			if (conv && (im == 1))
				bMain = true;
			}
		double dOffset = 0.0;
		if (!uOffset.isEmpty()) {
			dOffset = uOffset.toDouble(&conv);
			if (!conv)
				continue;
			}
		int prec = 0;
		if (!uPrec.isEmpty()) {
			prec = uPrec.toInt(&conv);
			if (!conv)
				continue;
			}
//		qDebug() << "Añado unidad" << uName << ", ratio:" << dRatio <<
//			", offset: " << dOffset << ", main: " << bMain <<
//			", prec: " << prec;
		d->addUnit(uName, dRatio, dOffset, bMain, prec);
		}
	addDimension(d);
	}

/*!
    Añade un sistema métrico definido por el elemento \a el que se ha leído
    del fichero unidades.xml.  Además de crear el \link UnitCollection
    UnitCollection \endlink, lo puebla con las unidades que contiene.
 */

void UnitSystem::addUnitCollection (
	QDomElement	&el
	)

{
	QString name = el.attribute("name");
//	qDebug() << "Añado sistema de medida:" << name;
	if (name.isEmpty())
		return;
	UnitCollection *c = new UnitCollection(name);
	_collections.insert(name, c);
	QDomNodeList l = el.elementsByTagName("dimension");
	for (int i = 0; i < l.count(); ++i) {
		if (!l.at(i).isElement())
			continue;
		QDomElement e = l.at(i).toElement();
		QString dName = e.attribute("name");
		QString defUnit = e.attribute("unit");
		Dimension *d = _dimensions.value(dName, nullptr);
		if (d == nullptr)
			continue;
		const Unit *u = d->unit(defUnit);
		if (u == nullptr)
			continue;
		c->addUnit(dName, u);
//		qDebug() << "Añado unidad para" << dName << ":" << defUnit;
		}
	}

/*!
    Puebla el \link UnitSystem UnitSystem \endlink con los datos que
    se han leído del fichero XML y que están en \a doc.
 */
 
void UnitSystem::addXml (
	QDomDocument	&doc
	)

{
	QDomNodeList l1 = doc.elementsByTagName("dimensions");
	if (l1.count() == 0)
		return;
	if (!l1.at(0).isElement())
		return;
	QDomElement ed = l1.at(0).toElement();
	QDomNodeList l = ed.elementsByTagName("dimension");
	for (int i = 0; i < l.count(); ++i) {
		QDomNode n = l.at(i);
		if (!n.isElement())
			continue;
		QDomElement e = n.toElement();
		addDimension(e);
		}
	l1 = doc.elementsByTagName("systems");
	if (l1.count() == 0)
		return;
	if (!l1.at(0).isElement())
		return;
	ed = l1.at(0).toElement();
	l = ed.elementsByTagName("system");
	for (int i = 0; i < l.count(); i++) {
		QDomNode n = l.at(i);
		if (!n.isElement())
			continue;
		QDomElement e = n.toElement();
		addUnitCollection(e);
		}
	}

/*! Obtiene el objeto \link Dimension Dimension \endlink que representa
    la dimensión de nombre \a name */
    
Dimension *UnitSystem::getDimension (
	QString	name
	)

{
	return _dimensions.value(name, nullptr);
	}

/*! Fija como sistema métrico por defecto el que tiene por nombre
    \a name.  Devuelve \a true si puede hacerlo y \a false si
    falla. */
    
bool UnitSystem::setDefaultUnitCollection (
	QString	name
	)

{
	if (name.isNull()) {
		_defaultCollection = nullptr;
		return true;
		}
	UnitCollection *c = _collections.value(name, nullptr);

	if (c != nullptr) {
		_defaultCollection = c;
		return true;
		}
	else
		return false;
	}

/*! Devuelve el objeto \link UnitCollection UnitCollection \endlink
    que define el sistema métrico por defecto. */
    
UnitCollection *UnitSystem::defaultUnitCollection()

{
	return _defaultCollection;
	}	

/*! Devuelve el objeto \link Unit Unit \endlink que define la unidad
    de medida de nombre \a unitName para la dimensión \a dimension. */

const Unit *UnitSystem::unit (
	QString	dimension,
	QString	unitName
	) const

{
	if (unitName.isNull()) {
		if (_defaultCollection == nullptr) {
			qWarning("Se pide unidad por defecto para %s y no existe"
				" _defaultCollection", qPrintable(dimension));
			Dimension *d = _dimensions.value(dimension, nullptr);
			if (d != nullptr) {
				const Unit *u = d->defaultUnit();
				if (u == nullptr)
					u = d->mainUnit();
				return u;
				}
			return nullptr;
			}
		const Unit *u = _defaultCollection->getUnit(dimension);
		if (u == nullptr) {
			Dimension *d = _dimensions.value(dimension, nullptr);
			if (d == nullptr)
				return nullptr;
			return d->mainUnit();
			qWarning("No existe unidad por defecto para %s\n",
				qPrintable(dimension));
			}
		return u;
		}
	else {
		Dimension *d = _dimensions.value(dimension, nullptr);
		if (d == nullptr)
			return nullptr;
		return d->unit(unitName);
		}
	}

QStringList	UnitSystem::getAllUnitCollections()

{
	return _collections.keys();
	}
