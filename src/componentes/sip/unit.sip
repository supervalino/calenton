/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: unit.sip 133 2009-10-27 14:22:39Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/unit.sip $
*****************************************************************************/

class Unit /Supertype = sip.wrapper/ {

%TypeHeaderCode
#include <Unit>
%End

public:
	Unit(Dimension *dimension, QString name, double ratio, double offset, int prec);

	~Unit();

	double to(double n) const;
	double from(double n) const;
	QString name() const;
	int prec() const;

	const Dimension *dimension() const;

	double convert(double value, const Unit *unit) const;
	};
