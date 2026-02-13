/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: dimensioneditplugin.cpp 132 2009-10-27 12:11:17Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/designer/dimensioneditplugin.cpp $");

#include "dimensioneditplugin.h"
#include <DimensionEdit>

#include <QtPlugin>

DimensionEditPlugin::DimensionEditPlugin (
	QObject	*parent
	) :
	QObject(parent),
	initialized(false)
	
{
	}
	
void DimensionEditPlugin::initialize (
	QDesignerFormEditorInterface *
	)
	
{
	if (initialized)
		return;
	initialized = true;
	}

bool DimensionEditPlugin::isInitialized() const

{
	return initialized;
	}
	
QWidget	*DimensionEditPlugin::createWidget (
	QWidget	*parent
	)
	
{
	return new DimensionEdit(parent);
	}

QString	DimensionEditPlugin::name() const

{
	return QString("DimensionEdit");
	}
	
QString DimensionEditPlugin::group() const

{
	return QString("Trustserver Widgets");
	}
	
QIcon DimensionEditPlugin::icon() const

{
	return QIcon();
	}
	
QString DimensionEditPlugin::toolTip() const

{
	return QString("");
	}
	
QString DimensionEditPlugin::whatsThis() const

{
	return QString("");
	}
	
bool DimensionEditPlugin::isContainer() const

{
	return false;
	}
	
QString DimensionEditPlugin::domXml() const

{
	return "<widget class=\"DimensionEdit\" name=\"dimensionEdit\">\n"
		" <property name=\"geometry\">\n"
		"  <rect>\n"
		"   <x>0</x>\n"
		"   <y>0</y>\n"
		"   <width>100</width>\n"
		"   <height>18</height>\n"
		"  </rect>\n"
		" </property>\n"
		" <property name=\"toolTip\" >\n"
		"  <string>Editor de línea con conversión de unidades</string>\n"
		" </property>\n"
		" <property name=\"whatsThis\" >\n"
		"  <string>Al cambiar las unidades se realizará una conversión</string>\n"
		" </property>\n"
		"</widget>\n";
	}
	
QString DimensionEditPlugin::includeFile() const

{
	return "ts.h";
	}
	
QString DimensionEditPlugin::codeTemplate() const

{
	return "";
	}
