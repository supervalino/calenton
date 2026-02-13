/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: relone2oneproxy.sip 197 2010-03-01 01:04:10Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/relone2oneproxy.sip $
*****************************************************************************/

class RelOne2OneProxy : RowControlChildColumnProxy {

%TypeHeaderCode
#include <RelOne2OneProxy>
%End

public:
	RelOne2OneProxy(RelOne2One *rel /TransferThis/);
	virtual ~RelOne2OneProxy();

	virtual bool acceptRole(int role);
	virtual bool setterAcceptRole(int role);
	virtual bool setValue(const QVariant & value, int row, 
				int column, const SeqTableModel *m);
	virtual bool needsUpdateControl();
	virtual QVariant value(int row, int column, const SeqTableModel *m);
	
	virtual RelOne2One *parent();
	};

