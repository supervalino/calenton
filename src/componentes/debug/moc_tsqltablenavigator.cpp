/****************************************************************************
** Meta object code from reading C++ file 'tsqltablenavigator.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../widgets/tsqltablenavigator.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'tsqltablenavigator.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_TSqlTableNavigator[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      11,   14, // methods
       7,   69, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       2,       // signalCount

 // signals: signature, parameters, type, tag, flags
      26,   20,   19,   19, 0x05,
      47,   41,   19,   19, 0x05,

 // slots: signature, parameters, type, tag, flags
      69,   66,   19,   19, 0x0a,
      93,   86,   19,   19, 0x0a,
     132,  112,   19,   19, 0x08,
     201,  195,   19,   19, 0x08,
     251,  243,   19,   19, 0x08,
     283,  243,   19,   19, 0x08,
     318,  243,   19,   19, 0x08,
     354,  243,   19,   19, 0x08,
     387,  243,   19,   19, 0x08,

 // properties: name, type, flags
     425,  420, 0x01095103,
     440,  420, 0x01095103,
     458,  420, 0x01095103,
     502,  470, 0x0009510b,
     515,  420, 0x01095103,
     569,  536, 0x0009510b,
     620,  583, 0x0009510b,

       0        // eod
};

static const char qt_meta_stringdata_TSqlTableNavigator[] = {
    "TSqlTableNavigator\0\0newId\0idChanged(int)\0"
    "dirty\0dirtyChanged(bool)\0id\0"
    "setParentId(int)\0filter\0setFilter(QString)\0"
    "selected,deselected\0"
    "on_uiTableView_selectionChanged(QItemSelection,QItemSelection)\0"
    "index\0on_uiTableView_doubleClicked(QModelIndex)\0"
    "checked\0on_uiButtonBox_addClicked(bool)\0"
    "on_uiButtonBox_deleteClicked(bool)\0"
    "on_uiButtonBox_discardClicked(bool)\0"
    "on_uiButtonBox_editClicked(bool)\0"
    "on_uiButtonBox_saveClicked(bool)\0bool\0"
    "autoResizeRows\0autoResizeColumns\0"
    "showButtons\0QAbstractItemView::EditTriggers\0"
    "editTriggers\0alternatingRowColors\0"
    "QAbstractItemView::SelectionMode\0"
    "selectionMode\0QAbstractItemView::SelectionBehavior\0"
    "selectionBehavior\0"
};

void TSqlTableNavigator::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        TSqlTableNavigator *_t = static_cast<TSqlTableNavigator *>(_o);
        switch (_id) {
        case 0: _t->idChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 1: _t->dirtyChanged((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 2: _t->setParentId((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 3: _t->setFilter((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 4: _t->on_uiTableView_selectionChanged((*reinterpret_cast< const QItemSelection(*)>(_a[1])),(*reinterpret_cast< const QItemSelection(*)>(_a[2]))); break;
        case 5: _t->on_uiTableView_doubleClicked((*reinterpret_cast< const QModelIndex(*)>(_a[1]))); break;
        case 6: _t->on_uiButtonBox_addClicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 7: _t->on_uiButtonBox_deleteClicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 8: _t->on_uiButtonBox_discardClicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 9: _t->on_uiButtonBox_editClicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 10: _t->on_uiButtonBox_saveClicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        default: ;
        }
    }
}

#ifdef Q_NO_DATA_RELOCATION
static const QMetaObjectAccessor qt_meta_extradata_TSqlTableNavigator[] = {
        QAbstractItemView::getStaticMetaObject,
#else
static const QMetaObject *qt_meta_extradata_TSqlTableNavigator[] = {
        &QAbstractItemView::staticMetaObject,
#endif //Q_NO_DATA_RELOCATION
    0
};

const QMetaObjectExtraData TSqlTableNavigator::staticMetaObjectExtraData = {
    qt_meta_extradata_TSqlTableNavigator,  qt_static_metacall 
};

const QMetaObject TSqlTableNavigator::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_TSqlTableNavigator,
      qt_meta_data_TSqlTableNavigator, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &TSqlTableNavigator::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *TSqlTableNavigator::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *TSqlTableNavigator::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_TSqlTableNavigator))
        return static_cast<void*>(const_cast< TSqlTableNavigator*>(this));
    return QWidget::qt_metacast(_clname);
}

int TSqlTableNavigator::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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
        case 0: *reinterpret_cast< bool*>(_v) = isAutoResizeRows(); break;
        case 1: *reinterpret_cast< bool*>(_v) = isAutoResizeColumns(); break;
        case 2: *reinterpret_cast< bool*>(_v) = showButtons(); break;
        case 3: *reinterpret_cast< QAbstractItemView::EditTriggers*>(_v) = editTriggers(); break;
        case 4: *reinterpret_cast< bool*>(_v) = alternatingRowColors(); break;
        case 5: *reinterpret_cast< QAbstractItemView::SelectionMode*>(_v) = selectionMode(); break;
        case 6: *reinterpret_cast< QAbstractItemView::SelectionBehavior*>(_v) = selectionBehavior(); break;
        }
        _id -= 7;
    } else if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: setAutoResizeRows(*reinterpret_cast< bool*>(_v)); break;
        case 1: setAutoResizeColumns(*reinterpret_cast< bool*>(_v)); break;
        case 2: setShowButtons(*reinterpret_cast< bool*>(_v)); break;
        case 3: setEditTriggers(*reinterpret_cast< QAbstractItemView::EditTriggers*>(_v)); break;
        case 4: setAlternatingRowColors(*reinterpret_cast< bool*>(_v)); break;
        case 5: setSelectionMode(*reinterpret_cast< QAbstractItemView::SelectionMode*>(_v)); break;
        case 6: setSelectionBehavior(*reinterpret_cast< QAbstractItemView::SelectionBehavior*>(_v)); break;
        }
        _id -= 7;
    } else if (_c == QMetaObject::ResetProperty) {
        _id -= 7;
    } else if (_c == QMetaObject::QueryPropertyDesignable) {
        _id -= 7;
    } else if (_c == QMetaObject::QueryPropertyScriptable) {
        _id -= 7;
    } else if (_c == QMetaObject::QueryPropertyStored) {
        _id -= 7;
    } else if (_c == QMetaObject::QueryPropertyEditable) {
        _id -= 7;
    } else if (_c == QMetaObject::QueryPropertyUser) {
        _id -= 7;
    }
#endif // QT_NO_PROPERTIES
    return _id;
}

// SIGNAL 0
void TSqlTableNavigator::idChanged(int _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void TSqlTableNavigator::dirtyChanged(bool _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}
QT_END_MOC_NAMESPACE
