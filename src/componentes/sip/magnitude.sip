/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: magnitude.sip 133 2009-10-27 14:22:39Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/magnitude.sip $
*****************************************************************************/

class Magnitude /Supertype=sip.wrapper/ {

%TypeHeaderCode
#include <Magnitude>
%End

public:
	Magnitude();
	Magnitude(const Unit *unit);
	Magnitude(double value, const Unit *unit);
	Magnitude(const Magnitude &m);
	Magnitude(const QString &dimension, const QString &unit, double value);
	Magnitude(const QString &s);
	
	~Magnitude();

	double value() const;
	bool empty() const;
	void clean();
	void allClean();
	void setUnit(const Unit *unit);	
	void setUnit(const QString &unitName);

	bool correct() const;
	bool incorrect() const;
	bool corrupt() const;
	bool usefull() const;
	const Unit *unit() const;
	void transform(const Unit *unit);
	void transform(const QString &unit);

	double convert(const Unit *unit) const;
	double convert(const QString &unitName) const;
	Magnitude toUnit(const QString &unitName) const;
	Magnitude toDefaultUnit() const;
	double toMain() const;

	void setValue(double value);
	void setValue(QString value);
	void setMagnitude(double value, const Unit *unit) ;
	QString toString() const;

	QString 		toStorableString();
	static Magnitude	fromStorableString(const QString &storableString, 
						UnitSystem *unitSystem = NULL);
	
	static QVariant::Type	typeId();
	static void		registerMetaType();
	};