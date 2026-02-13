TARGET = ts.so
OFILES = siptscmodule.o siptsQList0101RowControl.o siptsTSqlTableNavigatorDelegate.o siptsTSqlTableNavigator.o siptsTTableView.o siptsTSqlButtonBox.o siptsTTabWidget.o siptsFKItemDelegate.o siptsDimensionEdit.o siptsTComboBox.o siptsDataDialog.o siptsSeqTableModel.o siptsRelOne2OneProxy.o siptsRelOne2One.o siptsRowControlChildColumnProxy.o siptsRowControl.o siptsRowControlChild.o siptsForeignKey.o siptsFKModel.o siptsBaseForeignKey.o siptsComboDataModel.o siptsMagnitude.o siptsUnitSystem.o siptsUnitCollection.o siptsUnit.o siptsDimension.o
HFILES = sipAPIts.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DQT_NO_DEBUG -DQT_CORE_LIB -DQT_GUI_LIB -DQT_SQL_LIB -DQT_XML_LIB -I. -I/home/picazo/work/emisiones/trunk/src/componentes/sip/../include -I/home/picazo/work/emisiones/trunk/src/componentes/sip/../ui_include -I/usr/include/python2.7 -I/usr/share/qt4/mkspecs/default -I/usr/include/qt4/QtCore -I/usr/include/qt4/QtGui -I/usr/include/qt4/QtSql -I/usr/include/qt4/QtXml -I/usr/include/qt4 -I/usr/X11R6/include
CFLAGS =  -g -O2 -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security  -D_FORTIFY_SOURCE=2 -fPIC -O2 -Wall -W -D_REENTRANT
CXXFLAGS =  -g -O2 -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security  -D_FORTIFY_SOURCE=2 -fPIC -O2 -Wall -W -D_REENTRANT
LFLAGS =  -Wl,-z,relro -Wl,-O1 -shared  -Wl,-O1 -Wl,--version-script=ts.exp
LIBS = -L/home/picazo/work/emisiones/trunk/src/componentes/sip/../lib -L/usr/lib -L/usr/X11R6/lib -lcomponentes -lQtCore -lQtGui -lQtSql -lQtXml
MOC = moc-qt4
.SUFFIXES: .c .o .cpp .cc .cxx .C


.cpp.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cc.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cxx.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.C.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.c.o:
	$(CC) -c $(CFLAGS) $(CPPFLAGS) -o $@ $<

all: $(TARGET)

$(OFILES): $(HFILES)

$(TARGET): $(OFILES)
	@echo '{ global: initts; local: *; };' > ts.exp
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@test -d $(DESTDIR)/home/picazo/usr/python || mkdir -p $(DESTDIR)/home/picazo/usr/python
	cp -f $(TARGET) $(DESTDIR)/home/picazo/usr/python/$(TARGET)
	@test -d $(DESTDIR)/home/picazo/usr/python || mkdir -p $(DESTDIR)/home/picazo/usr/python
	cp -f ../__init__.py $(DESTDIR)/home/picazo/usr/python/__init__.py

clean:
	-rm -f $(TARGET)
	-rm -f siptscmodule.o
	-rm -f siptsQList0101RowControl.o
	-rm -f siptsTSqlTableNavigatorDelegate.o
	-rm -f siptsTSqlTableNavigator.o
	-rm -f siptsTTableView.o
	-rm -f siptsTSqlButtonBox.o
	-rm -f siptsTTabWidget.o
	-rm -f siptsFKItemDelegate.o
	-rm -f siptsDimensionEdit.o
	-rm -f siptsTComboBox.o
	-rm -f siptsDataDialog.o
	-rm -f siptsSeqTableModel.o
	-rm -f siptsRelOne2OneProxy.o
	-rm -f siptsRelOne2One.o
	-rm -f siptsRowControlChildColumnProxy.o
	-rm -f siptsRowControl.o
	-rm -f siptsRowControlChild.o
	-rm -f siptsForeignKey.o
	-rm -f siptsFKModel.o
	-rm -f siptsBaseForeignKey.o
	-rm -f siptsComboDataModel.o
	-rm -f siptsMagnitude.o
	-rm -f siptsUnitSystem.o
	-rm -f siptsUnitCollection.o
	-rm -f siptsUnit.o
	-rm -f siptsDimension.o
	-rm -f ts.exp
