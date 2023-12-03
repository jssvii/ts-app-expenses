"""
"""

from PySide2 import QtWidgets

from .ui.expense_manager_main import Ui_ExpenseManagerMain


class ExpenseManager(QtWidgets.QMainWindow):
    """
    """

    def __init__(self):
        super().__init__()

        self.ui = Ui_ExpenseManagerMain()
        self.ui.setupUi(self)