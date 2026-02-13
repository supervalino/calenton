/****************************************************************************
** Meta object code from reading C++ file 'seqtablemodel.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../data/seqtablemodel.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'seqtablemodel.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_SeqTableModel[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      11,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      25,   15,   14,   14, 0x0a,
      66,   46,   14,   14, 0x0a,
     124,  107,   14,   14, 0x0a,
     162,  107,   14,   14, 0x0a,
     199,   14,   14,   14, 0x0a,
     211,   14,   14,   14, 0x0a,
     225,   14,  220,   14, 0x0a,
     248,  237,   14,   14, 0x08,
     281,  277,   14,   14, 0x08,
     306,  299,   14,   14, 0x08,
     332,  237,   14,   14, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_SeqTableModel[] = {
    "SeqTableModel\0\0newRecord\0calcSeq(QSqlRecord&)\0"
    "topLeft,bottomRight\0"
    "slotDataChanged(QModelIndex,QModelIndex)\0"
    "parent,start,end\0slotRowsInserted(QModelIndex,int,int)\0"
    "slotRowsRemoved(QModelIndex,int,int)\0"
    "revertAll()\0revert()\0bool\0submitAll()\0"
    "row,record\0primeInsert(int,QSqlRecord&)\0"
    "row\0beforeDelete(int)\0record\0"
    "beforeInsert(QSqlRecord&)\0"
    "beforeUpdate(int,QSqlRecord&)\0"
};

void SeqTableModel::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        SeqTableModel *_t = static_cast<SeqTableModel *>(_o);
        switch (_id) {
        case 0: _t->calcSeq((*reinterpret_cast< QSqlRecord(*)>(_a[1]))); break;
        case 1: _t->slotDataChanged((*reinterpret_cast< const QModelIndex(*)>(_a[1])),(*reinterpret_cast< const QModelIndex(*)>(_a[2]))); break;
        case 2: _t->slotRowsInserted((*reinterpret_cast< const QModelIndex(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2])),(*reinterpret_cast< int(*)>(_a[3]))); break;
        case 3: _t->slotRowsRemoved((*reinterpret_cast< const QModelIndex(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2])),(*reinterpret_cast< int(*)>(_a[3]))); break;
        case 4: _t->revertAll(); break;
        case 5: _t->revert(); break;
        case 6: { bool _r = _t->submitAll();
            if (_a[0]) *reinterpret_cast< bool*>(_a[0]) = _r; }  break;
        case 7: _t->primeInsert((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< QSqlRecord(*)>(_a[2]))); break;
        case 8: _t->beforeDelete((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 9: _t->beforeInsert((*reinterpret_cast< QSqlRecord(*)>(_a[1]))); break;
        case 10: _t->beforeUpdate((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< QSqlRecord(*)>(_a[2]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData SeqTableModel::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject SeqTableModel::staticMetaObject = {
    { &QSqlTableModel::staticMetaObject, qt_meta_stringdata_SeqTableModel,
      qt_meta_data_SeqTableModel, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &SeqTableModel::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *SeqTableModel::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *SeqTableModel::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_SeqTableModel))
        return static_cast<void*>(const_cast< SeqTableModel*>(this));
    return QSqlTableModel::qt_metacast(_clname);
}

int SeqTableModel::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QSqlTableModel::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 11)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 11;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
