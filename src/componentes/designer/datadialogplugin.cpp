/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: datadialogplugin.cpp 131 2009-10-27 11:59:22Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/designer/datadialogplugin.cpp $");

#include "datadialogplugin.h"
#include <DataDialog>

#include <QtPlugin>

DataDialogPlugin::DataDialogPlugin (
	QObject	*parent
	) :
	QObject(parent),
	initialized(false)
	
{
	}
	
void DataDialogPlugin::initialize (
	QDesignerFormEditorInterface *
	)
	
{
	if (initialized)
		return;
	initialized = true;
	}

bool DataDialogPlugin::isInitialized() const

{
	return initialized;
	}
	
QWidget	*DataDialogPlugin::createWidget (
	QWidget	*parent
	)
	
{
	return new DataDialog(parent, 0);
	}

QString	DataDialogPlugin::name() const

{
	return QString("DataDialog");
	}
	
QString DataDialogPlugin::group() const

{
	return QString("Trustserver Widgets");
	}
	
QIcon DataDialogPlugin::icon() const

{
	return QIcon();
	}
	
QString DataDialogPlugin::toolTip() const

{
	return QString("");
	}
	
QString DataDialogPlugin::whatsThis() const

{
	return QString("");
	}
	
bool DataDialogPlugin::isContainer() const

{
	return true;
	}
	
QString DataDialogPlugin::domXml() const

{
	return QString();
	}
	
QString DataDialogPlugin::includeFile() const

{
	return "ts.h";
	}
	
QString DataDialogPlugin::codeTemplate() const

{
	return "";
	}
