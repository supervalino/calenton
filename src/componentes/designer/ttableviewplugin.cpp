/*****************************************************************************
  TRUST COMPONENTS

  (C) Trustserver S. L., 2009

  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: ttableviewplugin.cpp 214 2010-04-06 08:24:03Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/designer/ttableviewplugin.cpp $");

#include "ttableviewplugin.h"
#include <TTableView>

#include <QtPlugin>

TTableViewPlugin::TTableViewPlugin (
	QObject	*parent
	) :
	QObject(parent),
	initialized(false)

{
	}

void TTableViewPlugin::initialize (
	QDesignerFormEditorInterface *
	)

{
	if (initialized)
		return;
	initialized = true;
	}

bool TTableViewPlugin::isInitialized() const

{
	return initialized;
	}

QWidget	*TTableViewPlugin::createWidget (
	QWidget	*parent
	)

{
	return new TTableView(parent);
	}

QString	TTableViewPlugin::name() const

{
	return QString("TTableView");
	}

QString TTableViewPlugin::group() const

{
	return QString("Trustserver Widgets");
	}

QIcon TTableViewPlugin::icon() const

{
	return QIcon();
	}

QString TTableViewPlugin::toolTip() const

{
	return QString("");
	}

QString TTableViewPlugin::whatsThis() const

{
	return QString("");
	}

bool TTableViewPlugin::isContainer() const

{
	return false;
	}

QString TTableViewPlugin::domXml() const

{
	return "<widget class=\"TTableView\"/>";
	}

QString TTableViewPlugin::includeFile() const

{
	return "ts.h";
	}

QString TTableViewPlugin::codeTemplate() const

{
	return "";
	}

