# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VL-diskusia-zamykanie.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 10, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 120, 271, 51))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 741, 231))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 470, 151, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 410, 521, 51))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "<- BACK"))
        self.label.setText(_translate("MainWindow", "Autor: Stara Blazkova\n"
"Tema:Kto nezamyka vchodove dvere?!!?!"))
        self.label_3.setText(_translate("MainWindow", "Autor .............. Cas .............. Komentar .................................................\n"
"--------------------- ------------------ -----------------------------------------------------\n"
"Stara Blazkova ...... 1.1.2023 10:00 ... Dobre rano sudruhovia, dakto vkuse nezamyka vchodove dvere do bytovky.?\n"
"Stara Blazkova ...... 1.1.2023 10:01 ... Aj teraz su odomknute. Nevie o tom niekto nieco?\n"
"Peter z druheho ..... 1.1.2023 10:05 ... Jozko z tretieho bol ten, co nezamykal.\n"
"Jozko z tretieho .... 1.1.2023 10:10 ... Peter, preco siris klamstva?\n"
"Jozko z tretieho .... 1.1.2023 10:15 ... Videl som, ako si v noci nocil na kvetinac.\n"
"Majka kvetinacova ... 1.1.2023 10:20 ... Peter, dufam ze to neni pravda s tym kvetinacom.\n"
"Peter z druheho ..... 1.1.2023 10:25 ... Ano priznavam sa, bol som to ja. Prepacte.\n"
""))
        self.pushButton_2.setText(_translate("MainWindow", "PRIDAT KOMENTAR"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Vchodove dvere vobec maju zamok?</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())