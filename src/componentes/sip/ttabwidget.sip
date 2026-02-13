/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: ttabwidget.sip 176 2010-01-28 10:11:23Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/ttabwidget.sip $
*****************************************************************************/

class TTabWidget : QTabWidget {

%TypeHeaderCode
#include <TTabWidget>
%End

public:
	TTabWidget(QWidget *parent /TransferThis/ = 0);
	~TTabWidget();

	bool	isLocked() const;
public slots:
	void	lock();
	void	unlock();
	void	setLocked(bool status);
	};
