/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: seqtablemodel.sip 185 2010-02-12 15:23:20Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/seqtablemodel.sip $
*****************************************************************************/

class ComboDataModel : QAbstractListModel {

%TypeHeaderCode
#include <ComboDataModel>
%End

public:
	ComboDataModel(QObject *parent /TransferThis/ = 0,
			bool nullValue = false,
			const QString &nullMessage = QString());
	ComboDataModel(QSqlQuery &q, QObject *parent /TransferThis/ = 0,
			bool nullValue = false,
			const QString &nullMessage = QString());
	~ComboDataModel();

	virtual int rowCount(const QModelIndex &parent = QModelIndex()) const;
	virtual QVariant data(const QModelIndex &index, int role) const;
	
	virtual void setQuery(QSqlQuery &q);
	void setQuery(const QString &sql, QSqlDatabase db);

	void	setNullValue(bool nullValue);
	bool	nullValue() const;

	void	setNullMessage(const QString &nullMessage);
	QString	nullMessage() const;
	};


