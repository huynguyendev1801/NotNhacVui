# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GiaoDienClient.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(721, 484)
        Form.setStyleSheet("QLabel#labelTitle{\n"
"font: 28pt \"MS Shell Dlg 2\";\n"
"font-weight: bold;\n"
"color: #f8f8f2;\n"
"}\n"
"QWidget#Form{\n"
"background: #6272a4;\n"
"}\n"
"QLineEdit#txtAnswer{\n"
"font: 13pt \"MS Shell Dlg 2\";\n"
"color: #282a36;\n"
"border-radius: 5px;\n"
"}\n"
"QTextBrowser{\n"
"font: 13pt \"MS Shell Dlg 2\";\n"
"color: #282a36;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#btnSend{\n"
"font: 13pt \"MS Shell Dlg 2\";\n"
"background-color: #50fa7b;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#btnSend:hover{\n"
"background-color: #8be9fd;\n"
"}")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(10, 310, 701, 81))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(20, 24, 101, 21))
        self.label_3.setStyleSheet("color: #f8f8f2;\n"
"font: 13pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.txtAnswer = QtWidgets.QLineEdit(self.frame_4)
        self.txtAnswer.setGeometry(QtCore.QRect(140, 20, 391, 31))
        self.txtAnswer.setObjectName("txtAnswer")
        self.btnSend = QtWidgets.QPushButton(self.frame_4)
        self.btnSend.setGeometry(QtCore.QRect(540, 20, 51, 28))
        self.btnSend.setObjectName("btnSend")
        self.labelTitle = QtWidgets.QLabel(Form)
        self.labelTitle.setGeometry(QtCore.QRect(30, 10, 661, 71))
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(10, 370, 701, 91))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 111, 41))
        self.label_4.setStyleSheet("color: #f8f8f2;\n"
"font: 13pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.labelNotify = QtWidgets.QLabel(self.frame_5)
        self.labelNotify.setGeometry(QtCore.QRect(150, 10, 491, 71))
        self.labelNotify.setStyleSheet("color: #f8f8f2;\n"
"font: 13pt \"MS Shell Dlg 2\";")
        self.labelNotify.setText("")
        self.labelNotify.setObjectName("labelNotify")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 93, 711, 71))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 10, 101, 31))
        self.label.setStyleSheet("color: #f8f8f2;\n"
"font: 13pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 10, 451, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(10, 180, 711, 121))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 81, 21))
        self.label_2.setStyleSheet("color: #f8f8f2;\n"
"font: 13pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.txtQuestion = QtWidgets.QTextBrowser(self.frame_3)
        self.txtQuestion.setGeometry(QtCore.QRect(140, 10, 451, 91))
        self.txtQuestion.setObjectName("txtQuestion")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", " Trả lời:"))
        self.btnSend.setText(_translate("Form", "Gửi"))
        self.labelTitle.setText(_translate("Form", "TRÒ CHƠI NỐT NHẠC VUI"))
        self.label_4.setText(_translate("Form", "Thống báo:"))
        self.label.setText(_translate("Form", "Nốt nhạc:"))
        self.label_2.setText(_translate("Form", "Câu hỏi:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
