/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: relone2one.sip 199 2010-03-01 16:51:33Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/relone2one.sip $
*****************************************************************************/

class RelOne2One : RowControl {

%TypeHeaderCode
#include <RelOne2One>
%End

public:
	RelOne2One(QString idColumnName, QString relTable);
	virtual ~RelOne2One();

	QString	relTable() const;
	QString idColumnName() const;

	virtual void clearCache();
	virtual void revertRow(int row);
	virtual void addColumn(const QString &fieldName,
			       const QString &destName);
	
	virtual void addToTable(SeqTableModel *table);
	
	virtual bool setValue(const RelOne2OneProxy *p,
				const QVariant &value, int row,
				int column, const SeqTableModel *m);
	virtual QVariant value(const RelOne2OneProxy *p,
				int row, int column, 
				const SeqTableModel *m);

	virtual void primeInsert(int row, QSqlRecord &r);
	virtual void beforeInsert(QSqlRecord &r);
	virtual void afterUpdate(int row, QSqlRecord &r);
	virtual void afterDelete(int row, QSqlRecord &r);
	
	virtual void reloadMetadata();
protected:
	int	internalColumn(const QString &origColumnName);
	bool	setCacheValue(int row, int myColumnNumber,
				const QVariant &value);
	void	addColumnData(const QString &origName, const QString &destName,
				bool userColumn);
	int	encodeRowInId(int row);
	int	decodeRowFromId(int falseId);
	};


