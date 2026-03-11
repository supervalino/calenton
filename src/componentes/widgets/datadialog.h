/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: datadialog.h 118 2009-10-11 21:00:12Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/widgets/datadialog.h $
*****************************************************************************/

#ifndef DATADIALOG_H
#define DATADIALOG_H

#include <QDialog>
#include <QSqlRecord>

class SeqTableModel;
class QComboBox;
class QCheckBox;

class DataDialog: public QDialog {
	Q_OBJECT
public:
	enum EditMode { None = 0, Editing = 1, Adding = 2 };
protected:
	SeqTableModel	*_model;
	EditMode	_editMode;
	QSqlRecord	_record;
	QSqlRecord	_lastRecord;
	QString		_editionError;
public:
	DataDialog(QWidget *parent = nullptr, SeqTableModel *model = nullptr);
	~DataDialog();

	/*! Devuelve el modelo de datos utilizado */
	SeqTableModel *model() { return _model; }
	/*! Fija el modelo de datos que utilizará el diálogo */
	void setModel(SeqTableModel *model) { _model = model; }

	/*! Indica el \link DataDialog::EditMode modo de edición \endlink */
	EditMode editMode() const { return _editMode; }
	QSqlRecord lastRecord() const { return _lastRecord; }
protected:
	virtual bool	putData(const QSqlRecord &r);
	virtual bool	getData(QSqlRecord &r);
	
	void	putIdComboBox(SeqTableModel *model, QComboBox *combo, 
			int id, QString columnName = QString("id"));
	virtual bool	realAdd(QSqlRecord &r);
	
	int		checkToInteger(QCheckBox *check);
	Qt::CheckState	integerToCheck(int state);
	
	void	setEditionError(const QString &message);
	void	clearEditionError();
public:
	bool	hasEditionError();
	QString	editionError();
public slots:
	virtual bool	edit(int row);
	virtual bool	add();
	virtual void	accept();
	};

#endif // DATADIALOG_H
