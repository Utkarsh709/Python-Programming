Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
... from PyQt5.QtWidgets import QApplication, QMainWindow
... from PyQt5.uic import loadUi
... 
... 
... class Calculator(QMainWindow):
...     def __init__(self):
...         super(Calculator, self).__init__()
...         loadUi('calculator_ui.py', self)
... 
...         # Connect buttons to methods
...         self.pushButton_0.clicked.connect(lambda: self.append_digit('0'))
...         self.pushButton_1.clicked.connect(lambda: self.append_digit('1'))
...         self.pushButton_2.clicked.connect(lambda: self.append_digit('2'))
...         self.pushButton_3.clicked.connect(lambda: self.append_digit('3'))
...         self.pushButton_4.clicked.connect(lambda: self.append_digit('4'))
...         self.pushButton_5.clicked.connect(lambda: self.append_digit('5'))
...         self.pushButton_6.clicked.connect(lambda: self.append_digit('6'))
...         self.pushButton_7.clicked.connect(lambda: self.append_digit('7'))
...         self.pushButton_8.clicked.connect(lambda: self.append_digit('8'))
...         self.pushButton_9.clicked.connect(lambda: self.append_digit('9'))
... 
...         self.pushButton_add.clicked.connect(lambda: self.append_operator('+'))
...         self.pushButton_subtract.clicked.connect(lambda: self.append_operator('-'))
...         self.pushButton_multiply.clicked.connect(lambda: self.append_operator('*'))
...         self.pushButton_divide.clicked.connect(lambda: self.append_operator('/'))
... 
...         self.pushButton_clear.clicked.connect(self.clear_display)
...         self.pushButton_equals.clicked.connect(self.calculate_result)
... 
...     def append_digit(self, digit):
...         current_text = self.lineEdit_display.text()
...         new_text = current_text + digit
...         self.lineEdit_display.setText(new_text)
... 
...     def append_operator(self, operator):
...         current_text = self.lineEdit_display.text()
        new_text = current_text + operator
        self.lineEdit_display.setText(new_text)

    def clear_display(self):
        self.lineEdit_display.clear()

    def calculate_result(self):
        expression = self.lineEdit_display.text()
        try:
            result = eval(expression)
            self.lineEdit_display.setText(str(result))
        except Exception as e:
            self.lineEdit_display.setText('Error')


app = QApplication(sys.argv)
calculator = Calculator()
calculator.show()
sys.exit(app.exec_())
