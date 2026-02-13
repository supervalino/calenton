/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: seqtablemodel.sip 187 2010-02-15 09:41:40Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/seqtablemodel.sip $
*****************************************************************************/

class FKModel : ComboDataModel {

%TypeHeaderCode
#include <FKModel>
%End

public:
	FKModel(QSqlDatabase &db, const QString &table, 
		const QString &column, const QString &where,
		const QMap<QString, QVariant> &filters,
		bool nullValue = false,
		const QString &nullMessage = QString());
	~FKModel();

	void setWhere(const QString &where, const QMap<QString, QVariant> &filters);
	void setFilters(const QMap<QString, QVariant> &filters);
	};

