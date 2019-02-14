/********************************************************************************
** Form generated from reading UI file 'kdPortTunnel.ui'
**
** Created by: Qt User Interface Compiler version 4.8.7
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_KDPORTTUNNEL_H
#define UI_KDPORTTUNNEL_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QFormLayout>
#include <QtGui/QGridLayout>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPlainTextEdit>
#include <QtGui/QPushButton>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_mainWindow
{
public:
    QWidget *layoutWidget;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QPushButton *pb_start;
    QPushButton *pb_clear_info;
    QGridLayout *gridLayout;
    QFormLayout *fl_status;
    QLabel *lb_status_title;
    QLabel *lb_status;
    QFormLayout *formLayout;
    QLabel *lb_local_port;
    QPlainTextEdit *pte_local_port;
    QLabel *lb_target_addr;
    QPlainTextEdit *pte_target_addr;
    QLabel *lb_target_port;
    QPlainTextEdit *pte_target_port;
    QLabel *label_2;

    void setupUi(QWidget *mainWindow)
    {
        if (mainWindow->objectName().isEmpty())
            mainWindow->setObjectName(QString::fromUtf8("mainWindow"));
        mainWindow->resize(513, 262);
        layoutWidget = new QWidget(mainWindow);
        layoutWidget->setObjectName(QString::fromUtf8("layoutWidget"));
        layoutWidget->setGeometry(QRect(9, 9, 497, 237));
        verticalLayout = new QVBoxLayout(layoutWidget);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(0);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalLayout->setSizeConstraint(QLayout::SetDefaultConstraint);
        pb_start = new QPushButton(layoutWidget);
        pb_start->setObjectName(QString::fromUtf8("pb_start"));
        QSizePolicy sizePolicy(QSizePolicy::Maximum, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(pb_start->sizePolicy().hasHeightForWidth());
        pb_start->setSizePolicy(sizePolicy);

        horizontalLayout->addWidget(pb_start);

        pb_clear_info = new QPushButton(layoutWidget);
        pb_clear_info->setObjectName(QString::fromUtf8("pb_clear_info"));
        sizePolicy.setHeightForWidth(pb_clear_info->sizePolicy().hasHeightForWidth());
        pb_clear_info->setSizePolicy(sizePolicy);

        horizontalLayout->addWidget(pb_clear_info);


        verticalLayout->addLayout(horizontalLayout);

        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        fl_status = new QFormLayout();
        fl_status->setObjectName(QString::fromUtf8("fl_status"));
        fl_status->setFieldGrowthPolicy(QFormLayout::FieldsStayAtSizeHint);
        fl_status->setRowWrapPolicy(QFormLayout::WrapAllRows);
        fl_status->setFormAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop);
        lb_status_title = new QLabel(layoutWidget);
        lb_status_title->setObjectName(QString::fromUtf8("lb_status_title"));

        fl_status->setWidget(0, QFormLayout::LabelRole, lb_status_title);

        lb_status = new QLabel(layoutWidget);
        lb_status->setObjectName(QString::fromUtf8("lb_status"));

        fl_status->setWidget(1, QFormLayout::LabelRole, lb_status);


        gridLayout->addLayout(fl_status, 0, 1, 1, 1);

        formLayout = new QFormLayout();
        formLayout->setObjectName(QString::fromUtf8("formLayout"));
        formLayout->setSizeConstraint(QLayout::SetDefaultConstraint);
        formLayout->setFieldGrowthPolicy(QFormLayout::FieldsStayAtSizeHint);
        formLayout->setRowWrapPolicy(QFormLayout::DontWrapRows);
        formLayout->setHorizontalSpacing(6);
        formLayout->setVerticalSpacing(6);
        lb_local_port = new QLabel(layoutWidget);
        lb_local_port->setObjectName(QString::fromUtf8("lb_local_port"));

        formLayout->setWidget(0, QFormLayout::LabelRole, lb_local_port);

        pte_local_port = new QPlainTextEdit(layoutWidget);
        pte_local_port->setObjectName(QString::fromUtf8("pte_local_port"));
        QSizePolicy sizePolicy1(QSizePolicy::Maximum, QSizePolicy::Maximum);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(pte_local_port->sizePolicy().hasHeightForWidth());
        pte_local_port->setSizePolicy(sizePolicy1);
        pte_local_port->setMaximumSize(QSize(16777215, 30));

        formLayout->setWidget(0, QFormLayout::FieldRole, pte_local_port);

        lb_target_addr = new QLabel(layoutWidget);
        lb_target_addr->setObjectName(QString::fromUtf8("lb_target_addr"));

        formLayout->setWidget(1, QFormLayout::LabelRole, lb_target_addr);

        pte_target_addr = new QPlainTextEdit(layoutWidget);
        pte_target_addr->setObjectName(QString::fromUtf8("pte_target_addr"));
        sizePolicy1.setHeightForWidth(pte_target_addr->sizePolicy().hasHeightForWidth());
        pte_target_addr->setSizePolicy(sizePolicy1);
        pte_target_addr->setMaximumSize(QSize(16777215, 30));

        formLayout->setWidget(1, QFormLayout::FieldRole, pte_target_addr);

        lb_target_port = new QLabel(layoutWidget);
        lb_target_port->setObjectName(QString::fromUtf8("lb_target_port"));

        formLayout->setWidget(2, QFormLayout::LabelRole, lb_target_port);

        pte_target_port = new QPlainTextEdit(layoutWidget);
        pte_target_port->setObjectName(QString::fromUtf8("pte_target_port"));
        sizePolicy1.setHeightForWidth(pte_target_port->sizePolicy().hasHeightForWidth());
        pte_target_port->setSizePolicy(sizePolicy1);
        pte_target_port->setMaximumSize(QSize(16777215, 30));

        formLayout->setWidget(2, QFormLayout::FieldRole, pte_target_port);


        gridLayout->addLayout(formLayout, 0, 0, 1, 1);


        verticalLayout->addLayout(gridLayout);

        label_2 = new QLabel(layoutWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        verticalLayout->addWidget(label_2);


        retranslateUi(mainWindow);
        QObject::connect(mainWindow, SIGNAL(destroyed()), mainWindow, SLOT(close()));

        QMetaObject::connectSlotsByName(mainWindow);
    } // setupUi

    void retranslateUi(QWidget *mainWindow)
    {
        mainWindow->setWindowTitle(QApplication::translate("mainWindow", "TCP\347\275\221\347\273\234\346\225\260\346\215\256\350\275\254\345\217\221\345\231\250", 0, QApplication::UnicodeUTF8));
        pb_start->setText(QApplication::translate("mainWindow", "\345\220\257\345\212\250", 0, QApplication::UnicodeUTF8));
        pb_clear_info->setText(QApplication::translate("mainWindow", "\346\270\205\347\251\272\344\277\241\346\201\257", 0, QApplication::UnicodeUTF8));
        lb_status_title->setText(QApplication::translate("mainWindow", "\345\275\223\345\211\215\347\212\266\346\200\201", 0, QApplication::UnicodeUTF8));
        lb_status->setText(QApplication::translate("mainWindow", "\345\256\242->\346\234\215\345\255\227\350\212\202: 0 Byte\n"
"\346\234\215->\345\256\242\345\255\227\350\212\202: 0 Byte", 0, QApplication::UnicodeUTF8));
        lb_local_port->setText(QApplication::translate("mainWindow", "\347\233\221\345\220\254\346\216\245\345\217\243", 0, QApplication::UnicodeUTF8));
        pte_local_port->setPlainText(QApplication::translate("mainWindow", "1234", 0, QApplication::UnicodeUTF8));
        lb_target_addr->setText(QApplication::translate("mainWindow", "\347\233\256\346\240\207\345\234\260\345\235\200", 0, QApplication::UnicodeUTF8));
        pte_target_addr->setPlainText(QApplication::translate("mainWindow", "192.168.1.127", 0, QApplication::UnicodeUTF8));
        lb_target_port->setText(QApplication::translate("mainWindow", "\347\233\256\346\240\207\347\253\257\345\217\243", 0, QApplication::UnicodeUTF8));
        pte_target_port->setPlainText(QApplication::translate("mainWindow", "80", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("mainWindow", "\346\234\252\345\220\257\345\212\250", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class mainWindow: public Ui_mainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_KDPORTTUNNEL_H
