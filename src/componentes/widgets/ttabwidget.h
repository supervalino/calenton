/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: ttabwidget.h 175 2010-01-27 17:13:36Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/widgets/ttabwidget.h $
*****************************************************************************/

#ifndef TTABWIDGET_H
#define TTABWIDGET_H

#include <QTabWidget>

class TTabWidget: public QTabWidget {
	Q_OBJECT
	Q_PROPERTY(bool locked READ isLocked WRITE setLocked)
private:
	bool		_locked;
	QList<bool>	_pageEnabled;
public:
	TTabWidget(QWidget *parent = 0);
	~TTabWidget();

	bool	isLocked() const;
public slots:
	void	lock();
	void	unlock();
	void	setLocked(bool status);
	};

#endif // TTABWIDGET_H
