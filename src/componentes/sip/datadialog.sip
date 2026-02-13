/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: datadialog.sip 123 2009-10-12 15:20:23Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/datadialog.sip $
*****************************************************************************/

class DataDialog: QDialog {

%TypeHeaderCode
#include <DataDialog>
%End
public:
	enum EditMode { None = 0, Editing = 1, Adding = 2 };
	
	DataDialog(QWidget *parent /TransferThis/ = 0, SeqTableModel *model = 0);
	~DataDialog();

	SeqTableModel *model();
	void setModel(SeqTableModel *model);

	EditMode editMode();
	QSqlRecord lastRecord();
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

