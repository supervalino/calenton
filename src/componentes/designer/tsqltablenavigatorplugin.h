/*****************************************************************************
  TRUST COMPONENTS

  (C) Trustserver S. L., 2009

  Todos los derechos reservados.

  $Id: tsqltablenavigatorplugin.h 214 2010-04-06 08:24:03Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/designer/tsqltablenavigatorplugin.h $
*****************************************************************************/

#ifndef TSQLTABLENAVIGATORPLUGIN_H
#define TSQLTABLENAVIGATORPLUGIN_H

#include <QDesignerCustomWidgetInterface>

class TSqlTableNavigatorPlugin: public QObject, public QDesignerCustomWidgetInterface {
	Q_OBJECT
	Q_INTERFACES(QDesignerCustomWidgetInterface)
private:
	bool	initialized;
public:
	TSqlTableNavigatorPlugin(QObject *parent = 0);

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

#endif // TSQLTABLENAVIGATORPLUGIN_H
