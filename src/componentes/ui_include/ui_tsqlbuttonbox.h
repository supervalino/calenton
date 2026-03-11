/********************************************************************************
** Form generated from reading UI file 'tsqlbuttonbox.ui'
**
** Created by: Qt User Interface Compiler version 6.10.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TSQLBUTTONBOX_H
#define UI_TSQLBUTTONBOX_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_TSqlButtonBox
{
public:
    QHBoxLayout *horizontalLayout;
    QPushButton *saveButton;
    QPushButton *discardButton;
    QSpacerItem *horizontalSpacer;
    QPushButton *addButton;
    QPushButton *editButton;
    QPushButton *deleteButton;

    void setupUi(QWidget *TSqlButtonBox)
    {
        if (TSqlButtonBox->objectName().isEmpty())
            TSqlButtonBox->setObjectName("TSqlButtonBox");
        TSqlButtonBox->resize(425, 26);
        horizontalLayout = new QHBoxLayout(TSqlButtonBox);
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        horizontalLayout->setObjectName("horizontalLayout");
        saveButton = new QPushButton(TSqlButtonBox);
        saveButton->setObjectName("saveButton");

        horizontalLayout->addWidget(saveButton);

        discardButton = new QPushButton(TSqlButtonBox);
        discardButton->setObjectName("discardButton");

        horizontalLayout->addWidget(discardButton);

        horizontalSpacer = new QSpacerItem(1, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        addButton = new QPushButton(TSqlButtonBox);
        addButton->setObjectName("addButton");

        horizontalLayout->addWidget(addButton);

        editButton = new QPushButton(TSqlButtonBox);
        editButton->setObjectName("editButton");

        horizontalLayout->addWidget(editButton);

        deleteButton = new QPushButton(TSqlButtonBox);
        deleteButton->setObjectName("deleteButton");

        horizontalLayout->addWidget(deleteButton);

        QWidget::setTabOrder(saveButton, discardButton);
        QWidget::setTabOrder(discardButton, addButton);
        QWidget::setTabOrder(addButton, editButton);
        QWidget::setTabOrder(editButton, deleteButton);

        retranslateUi(TSqlButtonBox);

        QMetaObject::connectSlotsByName(TSqlButtonBox);
    } // setupUi

    void retranslateUi(QWidget *TSqlButtonBox)
    {
        TSqlButtonBox->setWindowTitle(QCoreApplication::translate("TSqlButtonBox", "Form", nullptr));
        saveButton->setText(QCoreApplication::translate("TSqlButtonBox", "Guardar", nullptr));
        discardButton->setText(QCoreApplication::translate("TSqlButtonBox", "Descartar", nullptr));
        addButton->setText(QCoreApplication::translate("TSqlButtonBox", "A\303\261adir", nullptr));
        editButton->setText(QCoreApplication::translate("TSqlButtonBox", "Editar", nullptr));
        deleteButton->setText(QCoreApplication::translate("TSqlButtonBox", "Eliminar", nullptr));
    } // retranslateUi

};

namespace Ui {
    class TSqlButtonBox: public Ui_TSqlButtonBox {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_TSQLBUTTONBOX_H
