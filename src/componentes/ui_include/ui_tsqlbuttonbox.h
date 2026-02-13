/********************************************************************************
** Form generated from reading UI file 'tsqlbuttonbox.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TSQLBUTTONBOX_H
#define UI_TSQLBUTTONBOX_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QWidget>

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
            TSqlButtonBox->setObjectName(QString::fromUtf8("TSqlButtonBox"));
        TSqlButtonBox->resize(425, 26);
        horizontalLayout = new QHBoxLayout(TSqlButtonBox);
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        saveButton = new QPushButton(TSqlButtonBox);
        saveButton->setObjectName(QString::fromUtf8("saveButton"));

        horizontalLayout->addWidget(saveButton);

        discardButton = new QPushButton(TSqlButtonBox);
        discardButton->setObjectName(QString::fromUtf8("discardButton"));

        horizontalLayout->addWidget(discardButton);

        horizontalSpacer = new QSpacerItem(1, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        addButton = new QPushButton(TSqlButtonBox);
        addButton->setObjectName(QString::fromUtf8("addButton"));

        horizontalLayout->addWidget(addButton);

        editButton = new QPushButton(TSqlButtonBox);
        editButton->setObjectName(QString::fromUtf8("editButton"));

        horizontalLayout->addWidget(editButton);

        deleteButton = new QPushButton(TSqlButtonBox);
        deleteButton->setObjectName(QString::fromUtf8("deleteButton"));

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
        TSqlButtonBox->setWindowTitle(QApplication::translate("TSqlButtonBox", "Form", 0, QApplication::UnicodeUTF8));
        saveButton->setText(QApplication::translate("TSqlButtonBox", "Guardar", 0, QApplication::UnicodeUTF8));
        discardButton->setText(QApplication::translate("TSqlButtonBox", "Descartar", 0, QApplication::UnicodeUTF8));
        addButton->setText(QApplication::translate("TSqlButtonBox", "A\303\261adir", 0, QApplication::UnicodeUTF8));
        editButton->setText(QApplication::translate("TSqlButtonBox", "Editar", 0, QApplication::UnicodeUTF8));
        deleteButton->setText(QApplication::translate("TSqlButtonBox", "Eliminar", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class TSqlButtonBox: public Ui_TSqlButtonBox {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_TSQLBUTTONBOX_H
