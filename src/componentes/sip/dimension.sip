/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: dimension.sip 139 2009-11-06 10:20:33Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/dimension.sip $
*****************************************************************************/

class Dimension /Supertype=sip.wrapper/ {

%TypeHeaderCode
#include <Dimension>
%End

public:
//	typedef QMap<QString, Unit *> UnitMap;

	Dimension(QString name, QString description);
	~Dimension();

	QString name() const;
	QString description() const;
	
	void addUnit(QString name, double ratio, double offset, bool main, int prec);
	double convert(QString from, QString to, double value) const;
	double convert(const Unit *from, const Unit *to, double value) const;
	double convert(const Unit *from, QString to, double value) const;

	const Unit *unit(const QString &name) const;
	
	const Unit	*defaultUnit() const;
	void		setDefaultUnit(const Unit *defaultUnit);

//	const UnitMap &units() const;
	QStringList unitNames() const;
	const Unit *mainUnit() const;
	};
