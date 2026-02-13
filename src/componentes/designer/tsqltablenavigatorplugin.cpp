/*****************************************************************************
  TRUST COMPONENTS

  (C) Trustserver S. L., 2009

  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: tsqltablenavigatorplugin.cpp 214 2010-04-06 08:24:03Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/designer/tsqltablenavigatorplugin.cpp $");

#include "tsqltablenavigatorplugin.h"
#include <TSqlTableNavigator>

#include <QtPlugin>

TSqlTableNavigatorPlugin::TSqlTableNavigatorPlugin (
	QObject	*parent
	) :
	QObject(parent),
	initialized(false)

{
	}

void TSqlTableNavigatorPlugin::initialize (
	QDesignerFormEditorInterface *
	)

{
	if (initialized)
		return;
	initialized = true;
	}

bool TSqlTableNavigatorPlugin::isInitialized() const

{
	return initialized;
	}

QWidget	*TSqlTableNavigatorPlugin::createWidget (
	QWidget	*parent
	)

{
	return new TSqlTableNavigator(parent);
	}

QString	TSqlTableNavigatorPlugin::name() const

{
	return QString("TSqlTableNavigator");
	}

QString TSqlTableNavigatorPlugin::group() const

{
	return QString("Trustserver Widgets");
	}

QIcon TSqlTableNavigatorPlugin::icon() const

{
	return QIcon();
	}

QString TSqlTableNavigatorPlugin::toolTip() const

{
	return QString("");
	}

QString TSqlTableNavigatorPlugin::whatsThis() const

{
	return QString("");
	}

bool TSqlTableNavigatorPlugin::isContainer() const

{
	return false;
	}

QString TSqlTableNavigatorPlugin::domXml() const

{
	return "<widget class=\"TSqlTableNavigator\"/>";
	}

QString TSqlTableNavigatorPlugin::includeFile() const

{
	return "ts.h";
	}

QString TSqlTableNavigatorPlugin::codeTemplate() const

{
	return "";
	}

