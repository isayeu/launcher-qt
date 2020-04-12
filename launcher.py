#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launcher.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import os, subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog



class Ui_Dialog(object):
	def __init__(self):
		super(Ui_Dialog, self).__init__()
		#path = self.lineEdit.text()
		
		
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(278, 353)
		self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
		self.gridLayout_2.setObjectName("gridLayout_2")
		self.gridLayout = QtWidgets.QGridLayout()
		self.gridLayout.setObjectName("gridLayout")
		
		self.radioButtonPrime = QtWidgets.QRadioButton(Dialog)
		self.radioButtonPrime.setChecked(True)
		self.radioButtonPrime.setObjectName("radioButtonPrime")
		self.gridLayout.addWidget(self.radioButtonPrime, 0, 0, 1, 1)
		self.radioButtonNoPrime = QtWidgets.QRadioButton(Dialog)
		radioButtonPrime = "prime-run"
		self.radioButtonNoPrime.setObjectName("radioButtonNoPrime")
		radioButtonNoPrime = ""
		self.gridLayout.addWidget(self.radioButtonNoPrime, 1, 0, 1, 1)
		self.ButtonGroup = QtWidgets.QButtonGroup()
		self.ButtonGroup.addButton(self.radioButtonNoPrime)
		self.ButtonGroup.addButton(self.radioButtonPrime)
		self.ButtonGroup.setId(self.radioButtonNoPrime, 0)
		self.ButtonGroup.setId(self.radioButtonPrime, 1)
		
		self.ButtonRun = QtWidgets.QPushButton(Dialog)
		self.ButtonRun.setObjectName("ButtonRun")
		self.gridLayout.addWidget(self.ButtonRun, 2, 0, 1, 1)
		
		self.ButtonExit = QtWidgets.QPushButton(Dialog)
		self.ButtonExit.setObjectName("ButtonExit")
		self.gridLayout.addWidget(self.ButtonExit, 3, 0, 1, 1)
		self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)
		self.ButtonSelect = QtWidgets.QPushButton(Dialog)
		self.ButtonSelect.setObjectName("ButtonSelect")
		self.gridLayout_2.addWidget(self.ButtonSelect, 1, 0, 1, 1)
		self.lineEdit = QtWidgets.QLineEdit(Dialog)
		self.lineEdit.setObjectName("lineEdit")
		self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
		self.ButtonSelect.clicked.connect(self.SelectFile)
		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)
		self.ButtonRun.clicked.connect(self.run)
		
		self.ButtonExit.clicked.connect(QtCore.QCoreApplication.instance().quit) #Exit
				
	def SelectFile(self):
		self.lineEdit.setText(QFileDialog.getOpenFileName()[0])
		
	
	def run (self, button):
		path = self.lineEdit.text()
		button = self.ButtonGroup.checkedId()
		if button == 1:
			prmrun = ("prime-run")
			game = subprocess.run([prmrun, path])
		else:
			game = subprocess.run(path)
		
		
		#print (button)
		#game = subprocess.run(path)
				
	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
		self.radioButtonNoPrime.setText(_translate("Dialog", "No Prime-run"))
		self.ButtonRun.setText(_translate("Dialog", "Make Me Fucking Good"))
		self.radioButtonPrime.setText(_translate("Dialog", "Prime-run"))
		self.ButtonExit.setText(_translate("Dialog", "Do not press"))
		self.ButtonSelect.setText(_translate("Dialog", "Select Start File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
