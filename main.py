import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *

class pantalla(QMainWindow):
    def __init__(self):
        super(pantalla, self).__init__()
        uic.loadUi("calculadora.ui", self)

        self.id_operacion = 1  # Contador para el historial

        # Conectar los botones con las funciones
        self.setup_buttons()

    def setup_buttons(self):
        # Botones numéricos
        for i in range(10):
            getattr(self, f"btn_{i}").clicked.connect(lambda _, num=i: self.add_to_display(str(num)))

        # Botones de operadores
       # ...existing code...
        self.btn_suma.clicked.connect(lambda: self.add_to_display("+"))
        self.btn_resta.clicked.connect(lambda: self.add_to_display("-"))
        self.btn_multiplicacion.clicked.connect(lambda: self.add_to_display("*"))
        self.btn_dividir.clicked.connect(lambda: self.add_to_display("÷"))
        self.btn_coma.clicked.connect(lambda: self.add_to_display("."))
        self.btn_igual.clicked.connect(self.calculate)
        self.btn_borrar_ultimo_numero.clicked.connect(self.delete_last_character)
        self.btn_clear.clicked.connect(self.clear_display)
# ...existing code...


    def add_to_display(self, text):
        current = self.display.text()
        self.display.setText(current + text)

    def clear_display(self):
        self.display.clear()

    def delete_last_character(self):
        current = self.display.text()
        self.display.setText(current[:-1])

    def calculate(self):
        try:
            operation = self.display.text()
            result = eval(operation)
            self.display.setText(str(result))
            self.add_to_history(operation, result)
        except Exception as e:
            self.show_error("Operación inválida")
            self.clear_display()

    def add_to_history(self, operation, result):
        row_position = self.table_history.rowCount()
        self.table_history.insertRow(row_position)
        self.table_history.setItem(row_position, 0, QTableWidgetItem(str(self.id_operacion)))
        self.table_history.setItem(row_position, 1, QTableWidgetItem(operation))
        self.table_history.setItem(row_position, 2, QTableWidgetItem(str(result)))
        self.id_operacion += 1

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dia = pantalla()
    dia.show()
    sys.exit(app.exec())