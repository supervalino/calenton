#!/bin/sh

make distclean
qmake-qt4
make install

cd sip
rm generated/*
python configure.py
cd generated
make install

cd ../../designer
make distclean
qmake-qt4
make install

