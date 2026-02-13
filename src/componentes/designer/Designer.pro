CONFIG += designer \
    plugin \
    debug_and_release \
    precompile_header
QT += sql \
    svg \
    network \
    xml
TEMPLATE = lib
INCLUDEPATH += ../include \
    ../ui_include
LIBPATH += $$(HOME)/usr/lib
LIBS += -lcomponentes
PRECOMPILED_HEADER = ../include/static.h
TARGET = tsplugin
CONFIG(debug, debug|release) { 
    unix:TARGET = $$join(TARGET,,,_debug)
    else:TARGET = $$join(TARGET,,,d)
}
HEADERS = tsplugin.h \
    datadialogplugin.h \
    tcomboboxplugin.h \
    dimensioneditplugin.h \
    ttabwidgetplugin.h \
    tsqlbuttonboxplugin.h \
    ttableviewplugin.h \
    tsqltablenavigatorplugin.h
SOURCES = tsplugin.cpp \
    datadialogplugin.cpp \
    tcomboboxplugin.cpp \
    dimensioneditplugin.cpp \
    ttabwidgetplugin.cpp \
    tsqlbuttonboxplugin.cpp \
    ttableviewplugin.cpp \
    tsqltablenavigatorplugin.cpp
target.path = $$(HOME)/usr/plugins/designer
INSTALLS += target
