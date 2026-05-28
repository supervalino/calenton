#!/bin/bash

make distclean; qmake-qt4; make debug-install

(cd designer; make distclean; qmake-qt4; make install)

(cd sip; rm -f generated/*; python configure.py; cd generated; make install)


