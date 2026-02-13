/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: rowcontrolchild.sip 196 2010-02-26 12:56:17Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/rowcontrolchild.sip $
*****************************************************************************/

class RowControlChild {

%TypeHeaderCode
#include <RowControlChild>
%End

public:
	RowControlChild(RowControl *parent);
	virtual ~RowControlChild();
	
	RowControl	*parent() const;
	int		index() const;
	void		setIndex(int index);
	};
