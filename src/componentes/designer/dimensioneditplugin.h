/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: dimensioneditplugin.h 132 2009-10-27 12:11:17Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/designer/dimensioneditplugin.h $
*****************************************************************************/

#ifndef DIMENSIONEDITPLUGIN_H
#define DIMENSIONEDITPLUGIN_H

#include <QDesignerCustomWidgetInterface>

class DimensionEditPlugin: public QObject, public QDesignerCustomWidgetInterface {
	Q_OBJECT
	Q_INTERFACES(QDesignerCustomWidgetInterface)
private:
	bool	initialized;
public:
	DimensionEditPlugin(QObject *parent = 0);
	
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

#endif // DIMENSIONEDITPLUGIN_H
