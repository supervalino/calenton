/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: rowcontrolchildcolumnproxy.sip 196 2010-02-26 12:56:17Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/rowcontrolchildcolumnproxy.sip $
*****************************************************************************/

class RowControlChildColumnProxy : BaseForeignKey, RowControlChild {

%TypeHeaderCode
#include <RowControlChildColumnProxy>
%End

public:
	RowControlChildColumnProxy(RowControl *parent /TransferThis/);
	virtual ~RowControlChildColumnProxy();

	virtual void clear();
	virtual void revertRow(int row);
	virtual void setDb(const QSqlDatabase &db);

	virtual int column() const;
	virtual void setColumn(int column);
	};

