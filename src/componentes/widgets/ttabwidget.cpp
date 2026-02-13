/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: ttabwidget.cpp 175 2010-01-27 17:13:36Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/widgets/ttabwidget.cpp $");

#include "ttabwidget.h"

TTabWidget::TTabWidget (
	QWidget	*parent
	) :
	QTabWidget(parent),
	_locked(false),
	_pageEnabled()
	
{
	}
	
TTabWidget::~TTabWidget()

{
	}

void	TTabWidget::lock()

{
	if (_locked)
		return;
	_pageEnabled = QList<bool>();
	for (int i = 0; i < count(); i++) {
		_pageEnabled.append(isTabEnabled(i));
		if (i != currentIndex())
			setTabEnabled(i, false);
		}
	_locked = true;
	}
	
void TTabWidget::unlock()

{
	if (!_locked)
		return;
	int n = qMin(count(), _pageEnabled.count());
	for (int i = 0; i < n; i++)
		setTabEnabled(i, _pageEnabled.at(i));
	_locked = false;
	}

bool TTabWidget::isLocked() const 

{
	return _locked;
	}

void TTabWidget::setLocked (
	bool	locked
	)
	
{
	if (locked == _locked)
		return;
	if (locked)
		lock();
	else
		unlock();
	}
