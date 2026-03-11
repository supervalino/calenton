/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: dimensionedit.h 137 2009-10-27 14:38:57Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/widgets/dimensionedit.h $
*****************************************************************************/

#ifndef DIMENSIONEDIT_H
#define DIMENSIONEDIT_H

#include <QWidget>
#include <QHBoxLayout>
#include <QLineEdit>
#include <QComboBox>
#include <Magnitude>

class UnitSystem;

class DimensionEdit : public QWidget {
	Q_OBJECT
	Q_PROPERTY(Magnitude magnitude READ magnitude WRITE setMagnitude)
	Q_PROPERTY(bool editorEnabled READ isEditorEnabled WRITE setEditorEnabled)
private:
	Magnitude	_magnitude;
	Magnitude	_shownMagnitude;
	Magnitude	_defaultMagnitude;
	bool		_onInit;
	bool		_default;
	bool		_hasDefault;
	bool		_textAltered;
public:
	DimensionEdit(QWidget *parent = nullptr);
	~DimensionEdit();

	void		clear();
	const Magnitude magnitude() const;
	const Magnitude displayMagnitude() const;
	void 		setMagnitude(Magnitude magnitude);
	void 		setDefaultMagnitude(Magnitude defaultMagnitude);
	bool 		isDefault() { return _default; }
	bool		isEditorEnabled();
	void		setEditorEnabled(bool editorEnabled);
	QString 	text();

	virtual bool 	eventFilter(QObject *watched, QEvent *event);
private:
	virtual bool	filterKey(QObject *watched, QEvent *event);
	virtual bool	filterFocusIn(QObject *watched, QEvent *event);
	virtual bool	filterFocusOut(QObject *watched, QEvent *event);
protected:
	QHBoxLayout	*_hBoxLayout;
	QLineEdit	*_lineEdit;
	QComboBox	*_comboBox;
private:
	void 		setupUi();
	void 		setupCombo();
	void 		setupLineEdit();
	QWidget		*prevWidget();
	void		setLineEditColor(bool def);
protected:
	virtual void 	focusInEvent(QFocusEvent *evt);
private slots:
	void on_comboBox_activated(const QString &text);
	void on_lineEdit_textEdited(const QString &text);
signals:
        /*! Se emite cada vez que cambia algo en el QLineEdit o que
            se cambian las unidades en el QComboBox por interacci�n
            con el usuario, pero no program�ticamente */
	void dataChanged(DimensionEdit *edit);
	/*! Se emite cada vez que cambia algo debido a interacci�n con 
	    el usuario o program�ticamente */
	void altered(DimensionEdit *edit);
	};

#endif // DIMENSIONEDIT_H
