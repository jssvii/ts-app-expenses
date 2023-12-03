# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'expense_manager_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ExpenseManagerMain(object):
    def setupUi(self, ExpenseManagerMain):
        if not ExpenseManagerMain.objectName():
            ExpenseManagerMain.setObjectName(u"ExpenseManagerMain")
        ExpenseManagerMain.resize(800, 600)
        self.actionNew_profile = QAction(ExpenseManagerMain)
        self.actionNew_profile.setObjectName(u"actionNew_profile")
        self.actionOpen_profile = QAction(ExpenseManagerMain)
        self.actionOpen_profile.setObjectName(u"actionOpen_profile")
        self.actionDelete_profile = QAction(ExpenseManagerMain)
        self.actionDelete_profile.setObjectName(u"actionDelete_profile")
        self.actionDelete_profile_2 = QAction(ExpenseManagerMain)
        self.actionDelete_profile_2.setObjectName(u"actionDelete_profile_2")
        self.actionClose_profile = QAction(ExpenseManagerMain)
        self.actionClose_profile.setObjectName(u"actionClose_profile")
        self.actionAdd_income_source = QAction(ExpenseManagerMain)
        self.actionAdd_income_source.setObjectName(u"actionAdd_income_source")
        self.actionAdd_payment_type = QAction(ExpenseManagerMain)
        self.actionAdd_payment_type.setObjectName(u"actionAdd_payment_type")
        self.actionAdd_payment_method = QAction(ExpenseManagerMain)
        self.actionAdd_payment_method.setObjectName(u"actionAdd_payment_method")
        self.actionImport_transactions = QAction(ExpenseManagerMain)
        self.actionImport_transactions.setObjectName(u"actionImport_transactions")
        self.actionIncome_sources = QAction(ExpenseManagerMain)
        self.actionIncome_sources.setObjectName(u"actionIncome_sources")
        self.actionPayment_methods = QAction(ExpenseManagerMain)
        self.actionPayment_methods.setObjectName(u"actionPayment_methods")
        self.actionTransactions = QAction(ExpenseManagerMain)
        self.actionTransactions.setObjectName(u"actionTransactions")
        self.actionDebts = QAction(ExpenseManagerMain)
        self.actionDebts.setObjectName(u"actionDebts")
        self.centralwidget = QWidget(ExpenseManagerMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.eoSplitter = QSplitter(self.centralwidget)
        self.eoSplitter.setObjectName(u"eoSplitter")
        self.eoSplitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.eoSplitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.expensesLayout = QVBoxLayout(self.layoutWidget)
        self.expensesLayout.setSpacing(6)
        self.expensesLayout.setObjectName(u"expensesLayout")
        self.expensesLayout.setContentsMargins(0, 0, 0, 0)
        self.expensesTreeView = QTreeView(self.layoutWidget)
        self.expensesTreeView.setObjectName(u"expensesTreeView")

        self.expensesLayout.addWidget(self.expensesTreeView)

        self.addOrRemoveLayout = QHBoxLayout()
        self.addOrRemoveLayout.setSpacing(2)
        self.addOrRemoveLayout.setObjectName(u"addOrRemoveLayout")
        self.addExpenseButton = QPushButton(self.layoutWidget)
        self.addExpenseButton.setObjectName(u"addExpenseButton")

        self.addOrRemoveLayout.addWidget(self.addExpenseButton)

        self.removeExpenseButton = QPushButton(self.layoutWidget)
        self.removeExpenseButton.setObjectName(u"removeExpenseButton")

        self.addOrRemoveLayout.addWidget(self.removeExpenseButton)

        self.addOrRemoveSpacer = QSpacerItem(248, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.addOrRemoveLayout.addItem(self.addOrRemoveSpacer)


        self.expensesLayout.addLayout(self.addOrRemoveLayout)

        self.eoSplitter.addWidget(self.layoutWidget)
        self.overviewFrame = QFrame(self.eoSplitter)
        self.overviewFrame.setObjectName(u"overviewFrame")
        self.overviewFrame.setFrameShape(QFrame.StyledPanel)
        self.overviewFrame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_2 = QVBoxLayout(self.overviewFrame)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.overviewSplitter = QSplitter(self.overviewFrame)
        self.overviewSplitter.setObjectName(u"overviewSplitter")
        self.overviewSplitter.setOrientation(Qt.Vertical)
        self.expenseSummaryTableView = QTableView(self.overviewSplitter)
        self.expenseSummaryTableView.setObjectName(u"expenseSummaryTableView")
        self.overviewSplitter.addWidget(self.expenseSummaryTableView)
        self.transactionSummaryTableView = QTableView(self.overviewSplitter)
        self.transactionSummaryTableView.setObjectName(u"transactionSummaryTableView")
        self.overviewSplitter.addWidget(self.transactionSummaryTableView)

        self.verticalLayout_2.addWidget(self.overviewSplitter)

        self.eoSplitter.addWidget(self.overviewFrame)

        self.verticalLayout_3.addWidget(self.eoSplitter)

        ExpenseManagerMain.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ExpenseManagerMain)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menuMain = QMenu(self.menubar)
        self.menuMain.setObjectName(u"menuMain")
        self.menuWindow = QMenu(self.menubar)
        self.menuWindow.setObjectName(u"menuWindow")
        ExpenseManagerMain.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ExpenseManagerMain)
        self.statusbar.setObjectName(u"statusbar")
        ExpenseManagerMain.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menuMain.addAction(self.actionNew_profile)
        self.menuMain.addAction(self.actionOpen_profile)
        self.menuMain.addAction(self.actionDelete_profile_2)
        self.menuMain.addAction(self.actionClose_profile)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.actionAdd_income_source)
        self.menuMain.addAction(self.actionAdd_payment_method)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.actionImport_transactions)
        self.menuWindow.addAction(self.actionIncome_sources)
        self.menuWindow.addAction(self.actionPayment_methods)
        self.menuWindow.addAction(self.actionTransactions)
        self.menuWindow.addAction(self.actionDebts)

        self.retranslateUi(ExpenseManagerMain)

        QMetaObject.connectSlotsByName(ExpenseManagerMain)
    # setupUi

    def retranslateUi(self, ExpenseManagerMain):
        ExpenseManagerMain.setWindowTitle(QCoreApplication.translate("ExpenseManagerMain", u"ExpenseManager", None))
        self.actionNew_profile.setText(QCoreApplication.translate("ExpenseManagerMain", u"New profile...", None))
        self.actionOpen_profile.setText(QCoreApplication.translate("ExpenseManagerMain", u"Open profile...", None))
        self.actionDelete_profile.setText(QCoreApplication.translate("ExpenseManagerMain", u"Delete profile...", None))
        self.actionDelete_profile_2.setText(QCoreApplication.translate("ExpenseManagerMain", u"Delete profile...", None))
        self.actionClose_profile.setText(QCoreApplication.translate("ExpenseManagerMain", u"Close profile...", None))
        self.actionAdd_income_source.setText(QCoreApplication.translate("ExpenseManagerMain", u"Add income source...", None))
        self.actionAdd_payment_type.setText(QCoreApplication.translate("ExpenseManagerMain", u"Add payment type...", None))
        self.actionAdd_payment_method.setText(QCoreApplication.translate("ExpenseManagerMain", u"Add payment method...", None))
        self.actionImport_transactions.setText(QCoreApplication.translate("ExpenseManagerMain", u"Import transactions...", None))
        self.actionIncome_sources.setText(QCoreApplication.translate("ExpenseManagerMain", u"Income sources", None))
        self.actionPayment_methods.setText(QCoreApplication.translate("ExpenseManagerMain", u"Payment methods", None))
        self.actionTransactions.setText(QCoreApplication.translate("ExpenseManagerMain", u"Transactions", None))
        self.actionDebts.setText(QCoreApplication.translate("ExpenseManagerMain", u"Debts", None))
        self.addExpenseButton.setText(QCoreApplication.translate("ExpenseManagerMain", u"+", None))
        self.removeExpenseButton.setText(QCoreApplication.translate("ExpenseManagerMain", u"-", None))
        self.menuMain.setTitle(QCoreApplication.translate("ExpenseManagerMain", u"Main", None))
        self.menuWindow.setTitle(QCoreApplication.translate("ExpenseManagerMain", u"Window", None))
    # retranslateUi

