/********************************************************************************
** Form generated from reading UI file 'tsqltablenavigator.ui'
**
** Created by: Qt User Interface Compiler version 6.10.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TSQLTABLENAVIGATOR_H
#define UI_TSQLTABLENAVIGATOR_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>
#include "ts.h"

QT_BEGIN_NAMESPACE

class Ui_TSqlTableNavigator
{
public:
    QVBoxLayout *verticalLayout;
    TTableView *uiTableView;
    TSqlButtonBox *uiButtonBox;

    void setupUi(QWidget *TSqlTableNavigator)
    {
        if (TSqlTableNavigator->objectName().isEmpty())
            TSqlTableNavigator->setObjectName("TSqlTableNavigator");
        TSqlTableNavigator->resize(433, 308);
        verticalLayout = new QVBoxLayout(TSqlTableNavigator);
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        verticalLayout->setObjectName("verticalLayout");
        uiTableView = new TTableView(TSqlTableNavigator);
        uiTableView->setObjectName("uiTableView");

        verticalLayout->addWidget(uiTableView);

        uiButtonBox = new TSqlButtonBox(TSqlTableNavigator);
        uiButtonBox->setObjectName("uiButtonBox");
        uiButtonBox->setAddEnabled(false);
        uiButtonBox->setEditEnabled(false);
        uiButtonBox->setDeleteEnabled(false);
        uiButtonBox->setSaveEnabled(false);
        uiButtonBox->setDiscardEnabled(false);

        verticalLayout->addWidget(uiButtonBox);


        retranslateUi(TSqlTableNavigator);

        QMetaObject::connectSlotsByName(TSqlTableNavigator);
    } // setupUi

    void retranslateUi(QWidget *TSqlTableNavigator)
    {
        TSqlTableNavigator->setWindowTitle(QCoreApplication::translate("TSqlTableNavigator", "Form", nullptr));
    } // retranslateUi

};

namespace Ui {
    class TSqlTableNavigator: public Ui_TSqlTableNavigator {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_TSQLTABLENAVIGATOR_H
