/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: unitsystem.sip 139 2009-11-06 10:20:33Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/unitsystem.sip $
*****************************************************************************/

class UnitSystem /Supertype=sip.wrapper/ {

%TypeHeaderCode
#include <UnitSystem>
%End

public:
	typedef QMap<QString, Dimension *> DimensionMap;
	typedef QMap<QString, UnitCollection *> UnitCollectionMap;
	
	UnitSystem();
	UnitSystem(QString configFile);
	~UnitSystem();

	Dimension *getDimension(QString name);

	void		addDimension(Dimension *dimension /Transfer/ );
	bool		setDefaultUnitCollection(QString name);
	UnitCollection	*defaultUnitCollection();
	const Unit	*unit(QString dimension, QString unitName = QString()) const;
	QStringList	getAllUnitCollections();
//	DimensionMap	getAllDimensions();
	QStringList	getAllDimensionsList();
	const Dimension	*getDimension(const QString &dimensionName);
	
	static void		setDefaultUnitSystem(UnitSystem *unitSystem /Transfer/);
	static UnitSystem	*defaultUnitSystem();
	};