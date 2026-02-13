/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: tcomboboxplugin.h 122 2009-10-12 14:04:11Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/designer/tcomboboxplugin.h $
*****************************************************************************/

#ifndef TCOMBOBOXPLUGIN_H
#define TCOMBOBOXPLUGIN_H

#include <QDesignerCustomWidgetInterface>

class TComboBoxPlugin: public QObject, public QDesignerCustomWidgetInterface {
	Q_OBJECT
	Q_INTERFACES(QDesignerCustomWidgetInterface)
private:
	bool	initialized;
public:
	TComboBoxPlugin(QObject *parent = 0);
	
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

#endif // TCOMBOBOXPLUGIN_H
