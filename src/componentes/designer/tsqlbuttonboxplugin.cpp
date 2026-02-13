/*****************************************************************************
  TRUST COMPONENTS

  (C) Trustserver S. L., 2009

  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: tsqlbuttonboxplugin.cpp 214 2010-04-06 08:24:03Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/designer/tsqlbuttonboxplugin.cpp $");

#include "tsqlbuttonboxplugin.h"
#include <TSqlButtonBox>

#include <QtPlugin>

TSqlButtonBoxPlugin::TSqlButtonBoxPlugin (
	QObject	*parent
	) :
	QObject(parent),
	initialized(false)

{
	}

void TSqlButtonBoxPlugin::initialize (
	QDesignerFormEditorInterface *
	)

{
	if (initialized)
		return;
	initialized = true;
	}

bool TSqlButtonBoxPlugin::isInitialized() const

{
	return initialized;
	}

QWidget	*TSqlButtonBoxPlugin::createWidget (
	QWidget	*parent
	)

{
	return new TSqlButtonBox(parent);
	}

QString	TSqlButtonBoxPlugin::name() const

{
	return QString("TSqlButtonBox");
	}

QString TSqlButtonBoxPlugin::group() const

{
	return QString("Trustserver Widgets");
	}

QIcon TSqlButtonBoxPlugin::icon() const

{
	return QIcon();
	}

QString TSqlButtonBoxPlugin::toolTip() const

{
	return QString("");
	}

QString TSqlButtonBoxPlugin::whatsThis() const

{
	return QString("");
	}

bool TSqlButtonBoxPlugin::isContainer() const

{
	return false;
	}

QString TSqlButtonBoxPlugin::domXml() const

{
	return "<widget class=\"TSqlButtonBox\"/>";
	}

QString TSqlButtonBoxPlugin::includeFile() const

{
	return "ts.h";
	}

QString TSqlButtonBoxPlugin::codeTemplate() const

{
	return "";
	}

