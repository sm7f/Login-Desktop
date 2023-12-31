from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMessageBox



class AddStyles:
    def __init__(self):
        # Estabelecer a conexão com o banco de dados
        (
        )

    def style_top(self):
        return ( "border-radius: 0px;\n"
"background: #141414;\n"
""
        )
    def style_content(self):
        return ( "border-radius: 0px;\n"
"background: #141414;\n"
""
        )

    def style_login_area(self):
        return ( "QFrame:{\n"
"    background: #0c0e0c;\n"
"    border: 2px solid #58fe81;\n"
"    border-radius: 5px;\n"
"}"

        )

    def style_logo(self):
        return ( "background:url(:/Image/teste5.jpg);\n"
"background-repeat: no-repeat;\n"
"\n"
"    \n"
""

        )
    def style_user(self):
        return ( "QLineEdit {\n"
"    border:2px solid rgb(45,45,45);\n"
"    border-radius:5px;\n"
"    padding:15px;\n"
"    background-color:rgb(30,30,30);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover{\n"
"    border:2px solid #ff29e2;\n"
"}\n"
"QLineEdit:focus{\n"
"    border:2px solid #ff29e2;\n"
"}\n"
""

        )
    def style_password(self):
        return ( "QLineEdit {\n"
"    border:2px solid rgb(45,45,45);\n"
"    border-radius:5px;\n"
"    padding:15px;\n"
"    background-color:rgb(30,30,30);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover{\n"
"    border:2px solid #ff29e2;\n"
"}\n"
"QLineEdit:focus{\n"
"    border:2px solid #ff29e2;\n"
"}\n"
""

        )
    def style_check(self):
        return ( "QCheckBox::indicator{\n"
"    border: 3px solid #ff29e2;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background-color:#0a0b0a;\n"
"}\n"
"QCheckBox::indicator::checked{\n"
"    color: rgb(45,45,45);\n"
"    border: 3px solid #58fe81;\n"
"    background-color:#58fe81;\n"
"}\n"
"\n"
"QCheckBox{\n"
"    color: rgb(200, 200, 200)\n"
"}\n"
""

        )
    def style_login(self):
        return ( "QPushButton{\n"
"    color: rgb(100, 100, 100);\n"
"    background-color:rgb(30,30,30);\n"
"    border: 2px solid rgb(60,60,60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #58fe81;\n"
"    border: 2px solid rgb(60,60,60);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #58fe81;\n"
"    border: 2px solid #ff29e2;\n"
"}"

        )
    def style_login(self):
        return ( "QPushButton{\n"
"    color: rgb(100, 100, 100);\n"
"    background-color:rgb(30,30,30);\n"
"    border: 2px solid rgb(60,60,60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #58fe81;\n"
"    border: 2px solid rgb(60,60,60);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #58fe81;\n"
"    border: 2px solid #ff29e2;\n"
"}"
        )
    def style_buttom_bar(self):
        return ( "border-radius: 0px;\n"
"background: #212220;\n"
""
        )