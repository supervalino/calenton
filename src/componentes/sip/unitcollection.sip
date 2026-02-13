/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: unitcollection.sip 135 2009-10-27 14:33:31Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/unitcollection.sip $
*****************************************************************************/

class UnitCollection /Supertype=sip.wrapper/ {

%TypeHeaderCode
#include <UnitCollection>
%End

public:
	typedef QMap<QString, const Unit *> UnitMap;
private:
	UnitCollection();
public:
	UnitCollection(QString name);
	~UnitCollection();

	void		addUnit(QString dimension, const Unit *unit);
	const Unit	*getUnit(QString dimension);
	const QString	&name();
	};