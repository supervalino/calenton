/****************************************************************************
** Meta object code from reading C++ file 'tsqlbuttonbox.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../widgets/tsqlbuttonbox.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'tsqlbuttonbox.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_TSqlButtonBox[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      11,   14, // methods
       5,   69, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       6,       // signalCount

 // signals: signature, parameters, type, tag, flags
      25,   15,   14,   14, 0x05,
      51,   43,   14,   14, 0x05,
      69,   43,   14,   14, 0x05,
      90,   43,   14,   14, 0x05,
     107,   43,   14,   14, 0x05,
     125,   43,   14,   14, 0x05,

 // slots: signature, parameters, type, tag, flags
     145,   43,   14,   14, 0x08,
     173,   43,   14,   14, 0x08,
     204,   43,   14,   14, 0x08,
     231,   43,   14,   14, 0x08,
     259,   43,   14,   14, 0x08,

 // properties: name, type, flags
     294,  289, 0x01095103,
     305,  289, 0x01095103,
     317,  289, 0x01095103,
     331,  289, 0x01095103,
     343,  289, 0x01095103,

       0        // eod
};

static const char qt_meta_stringdata_TSqlButtonBox[] = {
    "TSqlButtonBox\0\0b,checked\0clicked(int,bool)\0"
    "checked\0saveClicked(bool)\0"
    "discardClicked(bool)\0addClicked(bool)\0"
    "editClicked(bool)\0deleteClicked(bool)\0"
    "on_saveButton_clicked(bool)\0"
    "on_discardButton_clicked(bool)\0"
    "on_addButton_clicked(bool)\0"
    "on_editButton_clicked(bool)\0"
    "on_deleteButton_clicked(bool)\0bool\0"
    "addEnabled\0editEnabled\0deleteEnabled\0"
    "saveEnabled\0discardEnabled\0"
};

void TSqlButtonBox::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        TSqlButtonBox *_t = static_cast<TSqlButtonBox *>(_o);
        switch (_id) {
        case 0: _t->clicked((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< bool(*)>(_a[2]))); break;
        case 1: _t->saveClicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 2: _t->discardClicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 3: _t->addClicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 4: _t->editClicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 5: _t->deleteClicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 6: _t->on_saveButton_clicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 7: _t->on_discardButton_clicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 8: _t->on_addButton_clicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 9: _t->on_editButton_clicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 10: _t->on_deleteButton_clicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData TSqlButtonBox::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject TSqlButtonBox::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_TSqlButtonBox,
      qt_meta_data_TSqlButtonBox, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &TSqlButtonBox::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *TSqlButtonBox::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *TSqlButtonBox::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_TSqlButtonBox))
        return static_cast<void*>(const_cast< TSqlButtonBox*>(this));
    return QWidget::qt_metacast(_clname);
}

int TSqlButtonBox::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 11)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 11;
    }
#ifndef QT_NO_PROPERTIES
      else if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast< bool*>(_v) = isAddEnabled(); break;
        case 1: *reinterpret_cast< bool*>(_v) = isEditEnabled(); break;
        case 2: *reinterpret_cast< bool*>(_v) = isDeleteEnabled(); break;
        case 3: *reinterpret_cast< bool*>(_v) = isSaveEnabled(); break;
        case 4: *reinterpret_cast< bool*>(_v) = isDiscardEnabled(); break;
        }
        _id -= 5;
    } else if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: setAddEnabled(*reinterpret_cast< bool*>(_v)); break;
        case 1: setEditEnabled(*reinterpret_cast< bool*>(_v)); break;
        case 2: setDeleteEnabled(*reinterpret_cast< bool*>(_v)); break;
        case 3: setSaveEnabled(*reinterpret_cast< bool*>(_v)); break;
        case 4: setDiscardEnabled(*reinterpret_cast< bool*>(_v)); break;
        }
        _id -= 5;
    } else if (_c == QMetaObject::ResetProperty) {
        _id -= 5;
    } else if (_c == QMetaObject::QueryPropertyDesignable) {
        _id -= 5;
    } else if (_c == QMetaObject::QueryPropertyScriptable) {
        _id -= 5;
    } else if (_c == QMetaObject::QueryPropertyStored) {
        _id -= 5;
    } else if (_c == QMetaObject::QueryPropertyEditable) {
        _id -= 5;
    } else if (_c == QMetaObject::QueryPropertyUser) {
        _id -= 5;
    }
#endif // QT_NO_PROPERTIES
    return _id;
}

// SIGNAL 0
void TSqlButtonBox::clicked(int _t1, bool _t2)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)), const_cast<void*>(reinterpret_cast<const void*>(&_t2)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void TSqlButtonBox::saveClicked(bool _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}

// SIGNAL 2
void TSqlButtonBox::discardClicked(bool _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 2, _a);
}

// SIGNAL 3
void TSqlButtonBox::addClicked(bool _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 3, _a);
}

// SIGNAL 4
void TSqlButtonBox::editClicked(bool _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 4, _a);
}

// SIGNAL 5
void TSqlButtonBox::deleteClicked(bool _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 5, _a);
}
QT_END_MOC_NAMESPACE
