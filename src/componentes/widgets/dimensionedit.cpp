/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: dimensionedit.cpp 137 2009-10-27 14:38:57Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/widgets/dimensionedit.cpp $");

#include "dimensionedit.h"
#include <Dimension>
#include <QMessageBox>

/*!
    \class DimensionEdit dimensionedit.h
    \brief QWidget de edici�n de magnitud con unidades

    Para facilitar el uso del sistema de unidades en la entrada de datos,
    se crea este widget que encapsula un QLineEdit y un QComboBox.  En el
    QLineEdit se introduce una cantidad numérica y el QComboBox permite
    elegir la unidad deseada.

    Este widget realiza de forma autom�tica la conversión de unidades y
    proporciona funciones getter/setter para el tipo Magnitude.

    Además se proporciona un plugin para el designer para facilitar la
    edición de diálogos con entrada de unidades.

    \sa Unit, Magnitude, Dimension
 */

/*! Crea un nuevo widget dentro de \a parent */
DimensionEdit::DimensionEdit (
	QWidget	*parent
	) :
	QWidget(parent),
	_magnitude(),
	_shownMagnitude(),
	_defaultMagnitude(),
	_onInit(false),
	_default(true),
	_hasDefault(false),
	_textAltered(false),
	_hBoxLayout(0),
	_lineEdit(0),
	_comboBox(0)

{
	setupUi();
	_lineEdit->installEventFilter(this);
	_comboBox->installEventFilter(this);
	}

/*! Destruye el widget y todos los elementos asociados */

DimensionEdit::~DimensionEdit()

{
	}

/*! Crea el layout del widget, crea los elementos y los presenta de forma
    adecuada */
    
void DimensionEdit::setupUi()

{
	this->setObjectName(QString::fromLocal8Bit("DimensionEditClass"));
	this->resize(QSize(80, 25).expandedTo(this->minimumSizeHint()));
	_hBoxLayout = new QHBoxLayout(this);
	_hBoxLayout->setSpacing(6);
	_hBoxLayout->setMargin(0);
	_hBoxLayout->setObjectName(QString::fromLocal8Bit("hBoxLayout"));
	_lineEdit = new QLineEdit(this);
	_lineEdit->setObjectName(QString::fromLocal8Bit("lineEdit"));
//	_lineEdit->setFocusPolicy(Qt::NoFocus);
	_lineEdit->setFocusPolicy(Qt::ClickFocus);
	_hBoxLayout->addWidget(_lineEdit);
	_comboBox = new QComboBox(this);
	_comboBox->setObjectName(QString::fromLocal8Bit("comboBox"));
	_comboBox->setEditable(false);
//	_comboBox->setFocusPolicy(Qt::NoFocus);
	_comboBox->setFocusPolicy(Qt::ClickFocus);
	_hBoxLayout->addWidget(_comboBox);
	this->setFocusPolicy(Qt::WheelFocus);
//	this->setFocusPolicy(Qt::NoFocus);
	setTabOrder(_comboBox, _lineEdit);
//	this->setFocusProxy(_comboBox);
	this->resize(QSize(80,25).expandedTo(this->minimumSizeHint()));
	QMetaObject::connectSlotsByName(this);	
	}

/*!
    Rellena el combo box con todas las unidades posibles para la
    magnitud que estamos editando, además deja como unidad
    actual seleccionada la unidad que tiene en este momento
    la magnitud
 */
    
void DimensionEdit::setupCombo()

{
	Magnitude m;
	
	if (_default && _hasDefault)
		m = _defaultMagnitude;
	else
		m = _shownMagnitude;
	_comboBox->clear();
	if (!m.correct()) 
		return;
	const Unit *unit = m.unit();
	if (unit == 0) 
		return;
	const Dimension *d = unit->dimension();
	const Dimension::UnitMap &um = d->units();
	Dimension::UnitMap::const_iterator i;
	const Unit *defUnit = m.unit();
	int def = 0;
	int n;
	for (i = um.begin(), n = 0; i != um.end(); ++i, ++n) {
		Unit *u = i.value();
		QString name = u->name();
		_comboBox->insertItem(n, name);
		if (u == defUnit)
			def = n;
		}
	_comboBox->setCurrentIndex(def);
	}

void DimensionEdit::setLineEditColor (
	bool	def
	)

{
	if (!def) {
		_lineEdit->setPalette(QPalette());
		return;
		}
	QPalette p;
	p.setColor(QPalette::Text, QColor(180, 180, 180));
	_lineEdit->setPalette(p);
	}
	
/*! Rellena el lineEdit con el valor numérico de la magnitud que se
    edita */
    
void DimensionEdit::setupLineEdit()

{
	QString s;
	Magnitude m;
	
	if (_default)
		if (!_hasDefault) 
			s = QString();
		else
			s = QString("%1").arg(_defaultMagnitude.value(), 0, 'f', 
						_defaultMagnitude.unit()->prec());
	else
		s = QString("%1").arg(_shownMagnitude.value(), 0, 'f', 
						_shownMagnitude.unit()->prec());
	setLineEditColor(_default);
	_lineEdit->setText(s);
	}

/*!
    Función setter para fijar el valor de la magnitud que se ha de
    editar.  Se cambia el contenido del QLineEdit y del QComboBox,
    para reflejar el contenido de \a magnitude
 */
 
void DimensionEdit::setMagnitude (
	Magnitude	magnitude
	)

{
	_onInit = true;
	_magnitude = magnitude;
	_shownMagnitude = _magnitude;
	_textAltered = false;
	_default = magnitude.empty();
	setupCombo();
	setupLineEdit();
	_onInit = false;
	emit altered(this);
	}

void DimensionEdit::setDefaultMagnitude (
	Magnitude	defaultMagnitude
	)
	
{
	_onInit = true;
	_defaultMagnitude = defaultMagnitude;
	_hasDefault = (!defaultMagnitude.empty()) && defaultMagnitude.correct();
	if (_magnitude.empty()) {
		setupCombo();
		setupLineEdit();
		}
	_onInit = false;
	emit altered(this);
	}
	
/*!
    Función getter para obtener el valor introducido por el usuario de la
    magnitud.  La magnitud devuelta viene expresada en la unidad elegida
    por el usuario.
 */
 
const Magnitude DimensionEdit::magnitude() const

{
	QString text;
	Magnitude res = _magnitude;
	
	if (!_default) {
		QString unit = _comboBox->currentText();
		if (_textAltered) {
			text = _lineEdit->text();
			res.setUnit(unit);
			res.setValue(text);
			}
		else
			res.transform(unit);
		}
	else
		res.clean();
	return res;
	}
	
const Magnitude DimensionEdit::displayMagnitude() const

{
	if (_default && _hasDefault)
		return _defaultMagnitude;
	Magnitude res = _magnitude;
	if (_textAltered) {
		QString text = _lineEdit->text();
		res.setUnit(_comboBox->currentText());
		res.setValue(text);
		}
	else
		res.transform(_comboBox->currentText());
	return res;
	}

/*! Devuelve el contenido del QLineEdit */
QString DimensionEdit::text()

{
	if (_default)
		return QString();
	return _lineEdit->text();
	}

/*!
    Este slot se invoca cuando el usuario cambia de unidades
    en el combo box.  Se lee el valor presente en el line edit,
    se realiza la conversi�n de unidades de lo que hab�a a lo que
    se ha elegido y se rellena el line edit con el valor convertido.
 */
 
void DimensionEdit::on_comboBox_activated (
	const QString &text
	)

{
	if (_onInit)
		return;
	Magnitude m;
	if (!_default && _textAltered) {
		QString t = _lineEdit->text();
		_magnitude.setUnit(_shownMagnitude.unit());
		_magnitude.setValue(t);
		_textAltered = false;
		if (! _magnitude.correct()) 
			return;
		}
	_shownMagnitude = _magnitude;
	if (!_default)
		_shownMagnitude.transform(text);
	else if (_hasDefault)
		_defaultMagnitude.transform(text);
	setupLineEdit();
	if (!_default) {
		emit altered(this);
		emit dataChanged(this);
		}
	}

/*! Vac�a el line edit */
void DimensionEdit::clear()

{
	_lineEdit->setText(QString());
	_default = true;
	_textAltered = false;
	}

/*! Permite elevar la se�al \link DimensionEdit::dataChanged() dataChanged() cuando
    se edita el contenido del line edit */
    
void DimensionEdit::on_lineEdit_textEdited (
	const QString	&text
	)

{
	_default = text.isEmpty();
	_textAltered = true;
	emit altered(this);
	emit dataChanged(this);
	}

void DimensionEdit::focusInEvent (
	QFocusEvent	*evt
	)

{
	_lineEdit->setFocus();
//	if (evt->reason() == Qt::BacktabFocusReason)
//		_lineEdit->setFocus();
//	else
//		_comboBox->setFocus();
	evt->accept();
	}

QWidget *DimensionEdit::prevWidget()

{
	QWidget *w, *n;

	w = this;
	n = nextInFocusChain();
	while ((n != this) && (n != NULL)) {
		w = n;
		n = n->nextInFocusChain();
		}
	return ((n != NULL) ? w : NULL);
	}
	
bool DimensionEdit::filterKey (
	QObject	*watched, 
	QEvent	*event
	)
	
{
	QKeyEvent *ke = (QKeyEvent *)event;
	if ((ke->key() == Qt::Key_Tab) || (ke->key() == Qt::Key_Backtab)) {
		if ((ke->key() == Qt::Key_Tab) && (ke->modifiers() == Qt::NoModifier)) {
			if ((focusWidget() == _comboBox) && _lineEdit->isEnabled()) {
				_lineEdit->setFocus();
				return true;
				}
			else if ((focusWidget() == _lineEdit) || 
					((focusWidget() == _comboBox) && !_lineEdit->isEnabled())) {
				QWidget *w = nextInFocusChain();
				if (w != 0)
					w->setFocus();
				return true;
				}
			return true;
			}
		else if ((ke->key() == Qt::Key_Backtab) || (ke->modifiers() == Qt::ShiftModifier)) {
//			if (focusWidget() == _comboBox) {
				QWidget *w = prevWidget();
				if (w != 0)
					w->setFocus();
				return true;
//				}
//			else if (focusWidget() == _lineEdit) {
//				_comboBox->setFocus();
//				return true;
//				}
			return true;
			}
		}
	return QWidget::eventFilter(watched, event);
	}
	
bool DimensionEdit::filterFocusIn (
	QObject	*watched,
	QEvent	*event
	)
	
{
	QLineEdit *le = dynamic_cast<QLineEdit *>(watched);
	if (le == _lineEdit) {
		if (_default)
			_lineEdit->setText(QString());
		setLineEditColor(false);
		return false;
		}
	return QWidget::eventFilter(watched, event);
	}
	
bool DimensionEdit::filterFocusOut (
	QObject	*watched, 
	QEvent	*event
	)
	
{
	QLineEdit *le = dynamic_cast<QLineEdit *>(watched);
	if (le == _lineEdit) {
		if (_lineEdit->text().isEmpty()) {
			_default = true;
			setupLineEdit();
			}
		else 
			_default = false;
		}
	return QWidget::eventFilter(watched, event);
	}
	
bool DimensionEdit::eventFilter (
	QObject	*watched,
	QEvent	*event
	)

{
	switch (event->type()) { 
		case QEvent::KeyPress: return filterKey(watched, event);
		case QEvent::FocusIn: return filterFocusIn(watched, event);
		case QEvent::FocusOut: return filterFocusOut(watched, event);
		default: return QWidget::eventFilter(watched, event);
		}
	}
	
bool DimensionEdit::isEditorEnabled()

{
	return _lineEdit->isEnabled();
	}
	
void DimensionEdit::setEditorEnabled (
	bool	enabled
	)
	
{
	_lineEdit->setEnabled(enabled);
	}
