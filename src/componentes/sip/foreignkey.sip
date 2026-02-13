/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: seqtablemodel.sip 187 2010-02-15 09:41:40Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/seqtablemodel.sip $
*****************************************************************************/

class ForeignKey : BaseForeignKey {

%TypeHeaderCode
#include <ForeignKey>
%End

public:
	ForeignKey(QString table, QString column);
	virtual ~ForeignKey();

	QString 	value(int id);
	QVariant	value(int row, int column, const SeqTableModel *m);
	int		inverseMap(const QString &v, const QMap<QString, QVariant> &filters);
	FKModel 	*model(const QMap<QString, QVariant> &filters,
				bool nullValue = false,
				const QString &nullMessage = QString());
	void		setDb(const QSqlDatabase &db);
	void		clear();
	void		revertRow(int row);
protected:
	virtual QString	constructWhere(const QMap<QString, QVariant> &filters) const;
	virtual QString	constructKey(const QMap<QString, QVariant> &filters) const;
	};
	
