/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: datadialogplugin.h 122 2009-10-12 14:04:11Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/designer/datadialogplugin.h $
*****************************************************************************/

#ifndef DATADIALOGPLUGIN_H
#define DATADIALOGPLUGIN_H

#include <QDesignerCustomWidgetInterface>

class DataDialogPlugin: public QObject, public QDesignerCustomWidgetInterface {
	Q_OBJECT
	Q_INTERFACES(QDesignerCustomWidgetInterface)
private:
	bool	initialized;
public:
	DataDialogPlugin(QObject *parent = 0);
	
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

#endif // DATADIALOGPLUGIN_H
