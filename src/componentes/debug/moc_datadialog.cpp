/****************************************************************************
** Meta object code from reading C++ file 'datadialog.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../widgets/datadialog.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'datadialog.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_DataDialog[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       3,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      21,   17,   12,   11, 0x0a,
      31,   11,   12,   11, 0x0a,
      37,   11,   11,   11, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_DataDialog[] = {
    "DataDialog\0\0bool\0row\0edit(int)\0add()\0"
    "accept()\0"
};

void DataDialog::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        DataDialog *_t = static_cast<DataDialog *>(_o);
        switch (_id) {
        case 0: { bool _r = _t->edit((*reinterpret_cast< int(*)>(_a[1])));
            if (_a[0]) *reinterpret_cast< bool*>(_a[0]) = _r; }  break;
        case 1: { bool _r = _t->add();
            if (_a[0]) *reinterpret_cast< bool*>(_a[0]) = _r; }  break;
        case 2: _t->accept(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData DataDialog::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject DataDialog::staticMetaObject = {
    { &QDialog::staticMetaObject, qt_meta_stringdata_DataDialog,
      qt_meta_data_DataDialog, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &DataDialog::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *DataDialog::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *DataDialog::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_DataDialog))
        return static_cast<void*>(const_cast< DataDialog*>(this));
    return QDialog::qt_metacast(_clname);
}

int DataDialog::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
