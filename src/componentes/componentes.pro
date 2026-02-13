TEMPLATE = lib
CONFIG += debug_and_release \
    dll \
    precompile_header
QT += sql \
    svg \
    network \
    xml
INCLUDEPATH += include \
    ui_include
PRECOMPILED_HEADER = include/static.h
TARGET = componentes

# CONFIG(debug, debug|release){
# unix : TARGET = $$join(TARGET,,,_debug)
# else : TARGET = $$join(TARGET,,,d)
# }
include(base/base.pri)
include(data/data.pri)
include(widgets/widgets.pri)
target.path = $$(HOME)/usr/lib
DESTDIR = lib
UI_DIR = ui_include
INSTALLS += target
OTHER_FILES += sip/baseforeignkey.sip \
    sip/unitsystem.sip \
    sip/unit.sip \
    sip/unitcollection.sip \
    sip/ttabwidget.sip \
    sip/ts.sip \
    sip/tcombobox.sip \
    sip/seqtablemodel.sip \
    sip/rowcontrol.sip \
    sip/rowcontrolchild.sip \
    sip/rowcontrolchildcolumnproxy.sip \
    sip/relone2one.sip \
    sip/relone2oneproxy.sip \
    sip/magnitude.sip \
    sip/foreignkey.sip \
    sip/fkmodel.sip \
    sip/fkitemdelegate.sip \
    sip/dimension.sip \
    sip/dimensionedit.sip \
    sip/datadialog.sip \
    sip/combodatamodel.sip \
    sip/baseforeignkey.sip \
    sip/tsqltablenavigator.sip \
    sip/tsqlbuttonbox.sip \
    sip/ttableview.sip
