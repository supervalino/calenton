/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: dimensionedit.sip 133 2009-10-27 14:22:39Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/sip/dimensionedit.sip $
*****************************************************************************/

class DimensionEdit : QWidget {

%TypeHeaderCode
#include <DimensionEdit>
%End

public:
	DimensionEdit(QWidget *parent /TransferThis/ = 0);
	~DimensionEdit();

	void		clear();
	const Magnitude magnitude() const;
	const Magnitude displayMagnitude() const;
	void 		setMagnitude(Magnitude magnitude);
	void 		setDefaultMagnitude(Magnitude defaultMagnitude);
	bool 		isDefault();
	bool		isEditorEnabled();
	void		setEditorEnabled(bool editorEnabled);
	QString 	text();

	virtual bool 	eventFilter(QObject *watched, QEvent *event);
protected:
	virtual void 	focusInEvent(QFocusEvent *evt);
signals:
	void dataChanged(DimensionEdit *edit);
	void altered(DimensionEdit *edit);
	};

