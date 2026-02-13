/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: tsplugin.h 122 2009-10-12 14:04:11Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/designer/tsplugin.h $
*****************************************************************************/

#ifndef TSPLUGIN_H
#define TSPLUGIN_H

#include <QtDesigner/QtDesigner>
#include <QtCore/qplugin.h>

class TSPlugin: public QObject, public QDesignerCustomWidgetCollectionInterface

{
	Q_OBJECT
	Q_INTERFACES(QDesignerCustomWidgetCollectionInterface)
public:
	TSPlugin(QObject *parent = 0);
	
	virtual QList<QDesignerCustomWidgetInterface *> customWidgets() const;
	
private:
	QList<QDesignerCustomWidgetInterface *>	widgets;
	};
	
#endif // TSPLUGIN_H

