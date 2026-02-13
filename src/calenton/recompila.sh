#!/bin/bash

find . -name \*.pyc -exec rm {} \;

cd forms/ui
rm -f Ui_*.py
for i in *.ui
do
	base=`basename $i .ui`
	pyfile="Ui_${base}.py"
	echo -n "Compilando $base ..."
	pyuic4 -o $pyfile -x $i
	echo
done
	
