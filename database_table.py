import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout
from Table_output import TablePaintDelegate
from PyQt5.QtGui import QColor

class DatabaseDialog(QDialog):
    def __init__(self, matrix, title):
        super().__init__()
        self.title = title
        self.matrix = matrix
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)

        layout = QVBoxLayout()

        table_widget = QTableWidget()
        table_widget.setRowCount(len(self.matrix))
        table_widget.setColumnCount(len(self.matrix[0]))

        delegate = TablePaintDelegate(QColor(127,255,255),table_widget)
        table_widget.setItemDelegateForRow(0, delegate)
        
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                item = QTableWidgetItem(str(self.matrix[row][col]))
                table_widget.setItem(row, col, item)

        layout.addWidget(table_widget)
        self.setLayout(layout)
        self.show()





