/*****************************************************************************
  TRUST COMPONENTS

  (C) Trustserver S. L., 2009

  Todos los derechos reservados.

  $Id: ttableview.h 214 2010-04-06 08:24:03Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/widgets/ttableview.h $
*****************************************************************************/

#ifndef TTABLEVIEW_H
#define TTABLEVIEW_H

#include <QTableView>

class TTableView: public QTableView {
	Q_OBJECT
public:
	TTableView(QWidget *parent = 0);
	~TTableView();

	virtual void	setSelectionModel(QItemSelectionModel *selectionModel);

signals:
	void selectionChanged(const QItemSelection &selected, const QItemSelection &deselected);

private slots:
	void internalSelectionChanged(const QItemSelection &selected, const QItemSelection &deselected);
	};

#endif // TTABLEVIEW_H
