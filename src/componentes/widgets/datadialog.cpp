/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
*****************************************************************************/
#include <Hdr>

ID_ID("$Id: datadialog.cpp 131 2009-10-27 11:59:22Z bruno $");
ID_URL("$URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/widgets/datadialog.cpp $");

#include "datadialog.h"
#include <SeqTableModel>
#include <QtSql>
#include <QMessageBox>
#include <QComboBox>
#include <QCheckBox>

/*!
    \enum DataDialog::EditMode datadialog.h
    \brief Distintos estados en que puede estar operando un \link DataDialog
           DataDialog \endlink
 */

/*!
    \var DataDialog::EditMode DataDialog::None
    \brief El diálogo no está activo.
 */
 
/*!
    \var DataDialog::EditMode DataDialog::Editing
    \brief El diálogo está editando un registro existente.
 */
 
/*!
    \var DataDialog::EditMode DataDialog::Adding
    \brief El diálogo está editando un registro para añadir.
 */
 
/*!
    \class DataDialog datadialog.h
    \brief Encapsula la funcionalidad común a los diálogos de mantenimiento
           de tablas maestras.

    Automatiza el alta y edición de registros, y sólo requiere
    que las clases derivadas implementen los métodos \link DataDialog::getData()
    getData(QSqlRecord &)\endlink y \link DataDialog::putData()
    putData(QSqlRecord &)\endlink.

 */

/*!
    Construye un nuevo DataDialog con padre \a parent y conectado al modelo
    de datos \a model
*/
 
DataDialog::DataDialog (
	QWidget		*parent,
	SeqTableModel	*model
	) : 
	QDialog(parent),
	_model(model),
	_editMode(None),
	_editionError()
	
{
	}
	
/*!
    Elimina el diálogo y todo lo que depende de él.  No se destruye el
    modelo de datos.
*/

DataDialog::~DataDialog() 

{
	}

/*!
    Esta función debe ser implementada por el cliente y debe actualizar
    los controles del diálogo con los datos presentes en el QSqlRecord
    recibido como parámetro.
 */
 
bool	DataDialog::putData (
	const QSqlRecord &
	)
	
{
	return true;
	}

/*!
    Esta función debe ser implementada por el cliente y debe recoger en el
    QSqlRecord los valores presentes en los controles del diálogo.

    Si algún dato no es correcto, el cliente deberá devolver false y 
    fijar un mensaje de error utilizando \link DataDialog::setEditionError(QString &)
    setEditionError(const QString &)\endlink.
    Este mensaje será mostrado al usuario de forma automática y continuará
    la edición de datos hasta que estos sean correctos o se cancele la
    edición.
 */
 
bool	DataDialog::getData (
	QSqlRecord &
	)
	
{
	return true;
	}
	
void	DataDialog::setEditionError (
	const QString	&editionError
	)
	
{
	_editionError = editionError;
	}
	
void	DataDialog::clearEditionError()

{
	_editionError = QString();
	}
	
QString	DataDialog::editionError()

{
	return _editionError;
	}
	
bool	DataDialog::hasEditionError()

{
	return !_editionError.isNull();
	}
	
/*!
   Edita el contenido de la fila \a row en el modelo de datos.  Si el usuario
   acepta el diálogo los datos se actualizarán en el modelo de datos.  El cliente
   es responsable de forzar el volcado de datos a la base de datos subyacente.
 */
 
bool	DataDialog::edit (
	int	row
	)

{
	if (_model == NULL)
		return false;

	_record = _model->record(row);
	this->putData(_record);
	
	_editMode = Editing;
	clearEditionError();
	if (QDialog::exec() == QDialog::Accepted) {
		if (hasEditionError()) {
			QMessageBox::warning(this, tr("Error"), editionError(), QMessageBox::Ok, 0);
			return false;
			}
		if (!_model->setRecord(row, _record)) {
			setEditionError(_model->database().lastError().databaseText());
			return false;
			}
		_lastRecord = _record;
		_record = QSqlRecord();
		return true;
		}
	return false;
	}

/*!
  Este slot es responsable de recoger los datos editados y, si no son correctos,
  pedir su corrección al usuario.
 */
void	DataDialog::accept()

{
	if (this->getData(_record))
		QDialog::accept();
	else {
		if (hasEditionError())
			QMessageBox::warning(this, tr("Error"), editionError(), QMessageBox::Ok, 0);
		clearEditionError();
		}
	}
	
bool	DataDialog::realAdd (
	QSqlRecord	&r
	)

{
	if (_model == NULL)
		return false;
	_editMode = Adding;
	_record = r;
	clearEditionError();
	if (QDialog::exec() == QDialog::Accepted) {
		if (hasEditionError()) {
			QMessageBox::warning(this, tr("Error"), editionError(), QMessageBox::Ok, 0);
			return false;
			}
		_model->calcSeq(_record);
		if (!_model->insertRecord(-1, _record)) {
			setEditionError(_model->database().lastError().databaseText());
			return false;
			}
		_lastRecord = _record;
		_record = QSqlRecord();
		return true;
		}
	return false;
	}

/*!
   Añade un nuevo registro al modelo de datos y permite editar su contenido.
   Si el usuario acepta queda un nuevo registro con los datos introducidos,
   el cliente es responsable de forzar la escritura de datos a la base de
   datos subyacente.
 */

bool	DataDialog::add()

{
	if (_model == NULL)
		return false;
		
	QSqlRecord	r = _model->record();

	return realAdd(r);
	}

/*!
   Función de utilería.  Pone como elemento actual del QComboBox \a combo
   la línea que tiene en el modelo de datos \a model (que se supone enlazado
   a \a combo), el valor entero indicado por \a id en la columna que
   se llama \a columnName
 */
	
void	DataDialog::putIdComboBox (
	SeqTableModel	*model, 
	QComboBox	*combo, 
	int		id,
	QString		columnName
	)
	
{
	int nRows = model->rowCount();
	int currentIndex = -1;

	for (int i = 0; i < nRows; i++) {
		int id1 = model->record(i).value(columnName).toInt();
		if (id == id1) {
			currentIndex = i;
			break;
			}
		}
	combo->setCurrentIndex(currentIndex);
	}

/*!
   Devuelve 1 ó 0 según el \a check esté marcado o no.
 */
 
int	DataDialog::checkToInteger (
	QCheckBox	*check
	)
	
{
	return (check->checkState() == Qt::Checked) ? 1 : 0;
	}

/*!
   Devuelve Qt::Checked o Qt::Unchecked según \a state sea 1 ó 0.
 */
 
Qt::CheckState	DataDialog::integerToCheck (
	int	state
	)
	
{
	return state ? Qt::Checked : Qt::Unchecked;
	}
