/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: ttabwidgetplugin.h 175 2010-01-27 17:13:36Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/designer/ttabwidgetplugin.h $
*****************************************************************************/

#ifndef TTABWIDGETPLUGIN_H
#define TTABWIDGETPLUGIN_H

#include <QDesignerCustomWidgetInterface>

class TTabWidgetPlugin: public QObject, public QDesignerCustomWidgetInterface {
	Q_OBJECT
	Q_INTERFACES(QDesignerCustomWidgetInterface)
private:
	bool	initialized;
public:
	TTabWidgetPlugin(QObject *parent = 0);
	
	bool isContainer() const;
	bool isInitialized() const;
	QIcon icon() const;
	QString codeTemplate() const;
	QString domXml() const;
	QString group() const;
	QString includeFile() const;
	QString name() const;
	QString toolTip() const;
	QString whatsThis() const;
	QWidget *createWidget(QWidget *parent);
	void initialize(QDesignerFormEditorInterface *core);
	};

#endif // TTABWIDGETPLUGIN_H
