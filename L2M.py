from PyQt5.QtWidgets import (QWidget, QApplication, QComboBox, QDialog,
QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
QVBoxLayout, QPlainTextEdit, QPushButton, QMessageBox, QFrame, QCheckBox)
from PyQt5.QtGui import QIcon, QImage, QPixmap
#from PyQt5 import 
from latex2mathml import converter
from PyQt5.QtCore import pyqtSlot, QUrl, QUrlQuery

import sys
import PyQt5

from PyQt5.QtNetwork import *

from io import BytesIO
import sympy

import latex2mathml.converter

from More import More

class MainDialog(QWidget):
	
	def __init__(self):
		super().__init__()
		self.title = "LaTeX to MathML Converter (GUI)"
		self.left = 10
		self.top = 10
		self.width = 640
		self.height = 480
		self.http = QNetworkAccessManager()
		self.moreSymbols = More()
		self.moreSymbols.parent = self
		self.addWidgets()
		self.initUI()
		
	def initUI(self):
		mainLayout = QVBoxLayout()
		mainLayout.addWidget(self.formGroupBox)
		self.setLayout(mainLayout)
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.show()
		
	def addWidgets(self):
		self.formGroupBox = QGroupBox("Convert LaTeX to MathML")
		layout = QFormLayout()
		self.clear = QPushButton("Clear")
		self.clear.clicked.connect(self.clearOnClick)
		layout.addRow(QLabel("LaTeX Equation:"))
		self.latexBox = QPlainTextEdit(self)
		self.latexBox.textChanged.connect(self.fetchPreview)
		layout.addRow(self.latexBox)
		# Create buttons for adding certain things to the LaTeX:
		grid = QGridLayout()
		self.frac = QPushButton("Fraction")
		self.sqrt = QPushButton("Square Root")
		self.sin = QPushButton("Sine")
		self.cos = QPushButton("Cosine")
		self.tan = QPushButton("Tangent")
		self.sec = QPushButton("Secant")
		self.csc = QPushButton("Cosecant")
		self.cot = QPushButton("Cotangent")
		self.dx = QPushButton("Derivative (x)")
		self.integ = QPushButton("Integration")
		self.l = QPushButton("( )")
		self.more = QPushButton("More...")
		# Add all of these buttons to our grid layout
		grid.addWidget(self.frac, 0, 0)
		grid.addWidget(self.sqrt, 0, 1)
		grid.addWidget(self.sin, 0, 2)
		grid.addWidget(self.cos, 0, 3)
		grid.addWidget(self.tan, 0, 4)
		grid.addWidget(self.sec, 0, 5)
		grid.addWidget(self.csc, 1, 0)
		grid.addWidget(self.cot, 1, 1)
		grid.addWidget(self.dx, 1, 2)
		grid.addWidget(self.integ, 1, 3)
		grid.addWidget(self.l, 1, 4)
		grid.addWidget(self.more, 1, 5)
		# Connect them to functions
		self.frac.clicked.connect(self.fracOnClick)
		self.sqrt.clicked.connect(self.sqrtOnClick)
		self.sin.clicked.connect(self.sinOnClick)
		self.cos.clicked.connect(self.cosOnClick)
		self.tan.clicked.connect(self.tanOnClick)
		self.sec.clicked.connect(self.secOnClick)
		self.csc.clicked.connect(self.cscOnClick)
		self.cot.clicked.connect(self.cotOnClick)
		self.dx.clicked.connect(self.dxOnClick)
		self.integ.clicked.connect(self.integOnClick)
		self.l.clicked.connect(self.lOnClick)
		self.more.clicked.connect(self.moreOnClick)
		#grid.setColumnStretch(1, 4)
		#grid.setColumnStretch(2, 4)
		#buttons = QFormLayout()
		layout.addRow(grid)
		layout.addRow(QLabel("Preview"))
		self.outputLabel = QLabel()
		self.outputLabel.setFrameShape(QFrame.StyledPanel)
		layout.addRow(self.outputLabel)
		# layout.addRow(self.frac, self.sqrt) # , self.sin, self.cos)
		self.liveUpdate = QCheckBox("Live MathML update")
		layout.addRow(QLabel("MathML Output:"))
		self.mathMLBox = QPlainTextEdit(self)
		layout.addRow(self.mathMLBox)
		layout.addRow(self.liveUpdate)
		self.confirm = QPushButton("Convert")
		self.confirm.setToolTip("Convert LaTeX equation to MathML")
		self.confirm.clicked.connect(self.confirmOnClick)
		layout.addRow(self.confirm, self.clear)
		self.formGroupBox.setLayout(layout)
		
	# @pyqtSlot
	def confirmOnClick(self):
		print("Converting LaTeX to MathML...")
		latex = self.latexBox.toPlainText()
		if latex == "":
			print("Cannot convert empty string")
			self.errorBox("Cannot convert empty string.", "You must type something.")
			return
		try:
			mathml = latex2mathml.converter.convert(latex)
			self.mathMLBox.setPlainText(mathml)
			print("Done!")
		except:
			print("Some kind of error occurred:")
			self.errorBox("Some kind of error occurred", "Please use command line to see full stack trace for debugging")
			
	def fracOnClick(self):
		self.latexBox.insertPlainText("\\frac{}{}")
		
	def sqrtOnClick(self):
		self.latexBox.insertPlainText("\\sqrt{}")

	def sinOnClick(self):
		self.latexBox.insertPlainText("\\sin\\left( \\right)")

	def cosOnClick(self):
		self.latexBox.insertPlainText("\\cos\\left( \\right)")

	def tanOnClick(self):
		self.latexBox.insertPlainText("\\tan\\left( \\right)")

	def secOnClick(self):
		self.latexBox.insertPlainText("\\sec\\left( \\right)")

	def cscOnClick(self):
		self.latexBox.insertPlainText("\\csc\\left( \\right)")

	def cotOnClick(self):
		self.latexBox.insertPlainText("\\cot\\left( \\right)")

	def dxOnClick(self):
		self.latexBox.insertPlainText("\\frac{d}{dx}\left[ \\right]")

	def integOnClick(self):
		self.latexBox.insertPlainText("\\int dx")
		
	def lOnClick(self):
		self.latexBox.insertPlainText("\\left( \\right)")
		
	def moreOnClick(self):
		self.moreSymbols.show()
		pass
			
	def clearOnClick(self):
		print("Clearing")
		self.latexBox.setPlainText("")
		self.mathMLBox.setPlainText("")
		self.outputLabel.setPixmap(QPixmap())
		
	def errorBox(self, errTxt, infoText=""):
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Critical)
		msg.setText("Error: " + errTxt)
		msg.setInformativeText(infoText)
		msg.setWindowTitle("Error")
		msg.exec_()
		
	def fetchPreview(self):
		#url = QUrl()
		#urlQuery = QUrlQuery()
		#url.setPath("/cgi-bin/mathurl")
		#urlQuery.setQueryDelimiters("=", ";")
		#urlQuery.addQueryItem("D", "3")
		#urlQuery.addQueryItem("tex", str(QUrl.toPercentEncoding(
                         #self.latexBox.toPlainText())))
		#self.http.connectToHost("mathurl.com")
		if self.liveUpdate.isChecked():
			self.confirmOnClick()
		try:
			image = QImage()
			obj = BytesIO();
			sympy.preview('$$' + self.latexBox.toPlainText() + '$$', viewer='BytesIO', outputbuffer=obj, euler=False)
			obj.seek(0)
			# sympy.preview('$$' + self.latexBox.toPlainText() + '$$', output="png", euler=False)
			#url.setQuery(urlQuery)
			#print("URL for query: " + str(url))
			#reply = self.http.get(QNetworkRequest(url))
			if not image.loadFromData(obj.read()):
				print("No preview image")
				print(str(obj.read()))
				return
			pixmap = QPixmap(QPixmap.fromImage(image))
			self.outputLabel.setPixmap(pixmap)
		except:
			print("Invalid formula")
			
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MainDialog()
	sys.exit(app.exec_())
