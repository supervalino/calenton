/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: tcomboboxplugin.cpp 131 2009-10-27 11:59:22Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/designer/tcomboboxplugin.cpp $");

#include "tcomboboxplugin.h"
#include <TComboBox>

#include <QtPlugin>

TComboBoxPlugin::TComboBoxPlugin (
	QObject	*parent
	) :
	QObject(parent),
	initialized(false)
	
{
	}
	
void TComboBoxPlugin::initialize (
	QDesignerFormEditorInterface *
	)
	
{
	if (initialized)
		return;
	initialized = true;
	}

bool TComboBoxPlugin::isInitialized() const

{
	return initialized;
	}
	
QWidget	*TComboBoxPlugin::createWidget (
	QWidget	*parent
	)
	
{
	return new TComboBox(parent);
	}

QString	TComboBoxPlugin::name() const

{
	return QString("TComboBox");
	}
	
QString TComboBoxPlugin::group() const

{
	return QString("Trustserver Widgets");
	}
	
QIcon TComboBoxPlugin::icon() const

{
	return QIcon();
	}
	
QString TComboBoxPlugin::toolTip() const

{
	return QString("");
	}
	
QString TComboBoxPlugin::whatsThis() const

{
	return QString("");
	}
	
bool TComboBoxPlugin::isContainer() const

{
	return false;
	}
	
QString TComboBoxPlugin::domXml() const

{
	return "<widget class=\"TComboBox\" name=\"comboBox\"/>";
	}
	
QString TComboBoxPlugin::includeFile() const

{
	return "ts.h";
	}
	
QString TComboBoxPlugin::codeTemplate() const

{
	return "";
	}
