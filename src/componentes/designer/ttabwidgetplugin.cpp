/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: ttabwidgetplugin.cpp 175 2010-01-27 17:13:36Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/designer/ttabwidgetplugin.cpp $");

#include "ttabwidgetplugin.h"
#include <TTabWidget>

#include <QtPlugin>

TTabWidgetPlugin::TTabWidgetPlugin (
	QObject	*parent
	) :
	QObject(parent),
	initialized(false)
	
{
	}
	
void TTabWidgetPlugin::initialize (
	QDesignerFormEditorInterface *
	)
	
{
	if (initialized)
		return;
	initialized = true;
	}

bool TTabWidgetPlugin::isInitialized() const

{
	return initialized;
	}
	
QWidget	*TTabWidgetPlugin::createWidget (
	QWidget	*parent
	)
	
{
	return new TTabWidget(parent);
	}

QString	TTabWidgetPlugin::name() const

{
	return QString("TTabWidget");
	}
	
QString TTabWidgetPlugin::group() const

{
	return QString("Trustserver Widgets");
	}
	
QIcon TTabWidgetPlugin::icon() const

{
	return QIcon();
	}
	
QString TTabWidgetPlugin::toolTip() const

{
	return QString("");
	}
	
QString TTabWidgetPlugin::whatsThis() const

{
	return QString("");
	}
	
bool TTabWidgetPlugin::isContainer() const

{
	return true;
	}
	
QString TTabWidgetPlugin::domXml() const

{
	return "<widget class=\"TTabWidget\"> "
			"<property name=\"geometry\"> "
				"<rect> "
					"<x>0</x> "
					"<y>0</y> "
					"<width>120</width> "
					"<height>80</height> "
				"</rect> "
			"</property> "
			"<property name=\"objectName\"> "
				"<string notr=\"true\">tabWidget</string> "
			"</property> "
			"<widget class=\"QWidget\" name=\"tab\"> "
				"<attribute name=\"title\"> "
					"<string>Tab 1</string> "
				"</attribute> "
			"</widget> "
			"<widget class=\"QWidget\" name=\"tab\"> "
				"<attribute name=\"title\"> "
					"<string>Tab 2</string> "
				"</attribute> "
			"</widget> "
		"</widget> ";
	}
	
QString TTabWidgetPlugin::includeFile() const

{
	return "ts.h";
	}
	
QString TTabWidgetPlugin::codeTemplate() const

{
	return "";
	}
