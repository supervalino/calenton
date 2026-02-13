/****************************************************************************
** Meta object code from reading C++ file 'dimensionedit.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../widgets/dimensionedit.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'dimensionedit.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_DimensionEdit[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       4,   14, // methods
       2,   34, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       2,       // signalCount

 // signals: signature, parameters, type, tag, flags
      20,   15,   14,   14, 0x05,
      48,   15,   14,   14, 0x05,

 // slots: signature, parameters, type, tag, flags
      77,   72,   14,   14, 0x08,
     108,   72,   14,   14, 0x08,

 // properties: name, type, flags
     150,  140, 0x0009510b,
     165,  160, 0x01095103,

       0        // eod
};

static const char qt_meta_stringdata_DimensionEdit[] = {
    "DimensionEdit\0\0edit\0dataChanged(DimensionEdit*)\0"
    "altered(DimensionEdit*)\0text\0"
    "on_comboBox_activated(QString)\0"
    "on_lineEdit_textEdited(QString)\0"
    "Magnitude\0magnitude\0bool\0editorEnabled\0"
};

void DimensionEdit::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        DimensionEdit *_t = static_cast<DimensionEdit *>(_o);
        switch (_id) {
        case 0: _t->dataChanged((*reinterpret_cast< DimensionEdit*(*)>(_a[1]))); break;
        case 1: _t->altered((*reinterpret_cast< DimensionEdit*(*)>(_a[1]))); break;
        case 2: _t->on_comboBox_activated((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 3: _t->on_lineEdit_textEdited((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData DimensionEdit::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject DimensionEdit::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_DimensionEdit,
      qt_meta_data_DimensionEdit, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &DimensionEdit::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *DimensionEdit::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *DimensionEdit::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_DimensionEdit))
        return static_cast<void*>(const_cast< DimensionEdit*>(this));
    return QWidget::qt_metacast(_clname);
}

int DimensionEdit::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 4)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 4;
    }
#ifndef QT_NO_PROPERTIES
      else if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast< Magnitude*>(_v) = magnitude(); break;
        case 1: *reinterpret_cast< bool*>(_v) = isEditorEnabled(); break;
        }
        _id -= 2;
    } else if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: setMagnitude(*reinterpret_cast< Magnitude*>(_v)); break;
        case 1: setEditorEnabled(*reinterpret_cast< bool*>(_v)); break;
        }
        _id -= 2;
    } else if (_c == QMetaObject::ResetProperty) {
        _id -= 2;
    } else if (_c == QMetaObject::QueryPropertyDesignable) {
        _id -= 2;
    } else if (_c == QMetaObject::QueryPropertyScriptable) {
        _id -= 2;
    } else if (_c == QMetaObject::QueryPropertyStored) {
        _id -= 2;
    } else if (_c == QMetaObject::QueryPropertyEditable) {
        _id -= 2;
    } else if (_c == QMetaObject::QueryPropertyUser) {
        _id -= 2;
    }
#endif // QT_NO_PROPERTIES
    return _id;
}

// SIGNAL 0
void DimensionEdit::dataChanged(DimensionEdit * _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void DimensionEdit::altered(DimensionEdit * _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}
QT_END_MOC_NAMESPACE
