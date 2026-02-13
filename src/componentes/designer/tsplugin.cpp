/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: tsplugin.cpp 214 2010-04-06 08:24:03Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/designer/tsplugin.cpp $");

#include "tsplugin.h"
#include "datadialogplugin.h"
#include "tcomboboxplugin.h"
#include "dimensioneditplugin.h"
#include "ttabwidgetplugin.h"
#include "tsqlbuttonboxplugin.h"
#include "ttableviewplugin.h"
#include "tsqltablenavigatorplugin.h"

TSPlugin::TSPlugin (
	QObject	*parent
	) :
	QObject(parent)
	
{
	widgets.append(new DataDialogPlugin(this));
	widgets.append(new TComboBoxPlugin(this));
	widgets.append(new DimensionEditPlugin(this));
	widgets.append(new TTabWidgetPlugin(this));
	widgets.append(new TSqlButtonBoxPlugin(this));
	widgets.append(new TTableViewPlugin(this));
	widgets.append(new TSqlTableNavigatorPlugin(this));
	}
	
QList<QDesignerCustomWidgetInterface *>	TSPlugin::customWidgets() const

{
	return widgets;
	}

Q_EXPORT_PLUGIN2(tsplugin, TSPlugin)
