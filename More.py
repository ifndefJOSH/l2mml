from PyQt5.QtWidgets import (QWidget, QApplication, QComboBox, QDialog,
QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
QVBoxLayout, QPlainTextEdit, QPushButton, QMessageBox)
from PyQt5.QtGui import QIcon
from latex2mathml import converter
from PyQt5.QtCore import pyqtSlot

import sys
import PyQt5

import string

import latex2mathml.converter

sl = chr(92)

symbols = {
	'Α': str("‌Alpha")
	,'Β': str("‌Beta")
	,'Γ': str("‌Gamma")
	,'Δ': str("‌Delta")
	,'Ε': str("‌Epsilon")
	,'Ζ': str("‌Zeta")
	,'Η': str("‌Eta")
	,'Θ': str("‌Theta")
	,'Ι': str("‌Iota")
	,'Κ': str("‌Kappa")
	,'Λ': str("‌Lambda")
	,'Μ': str("‌Mu")
	,'Ν': str("‌Nu")
	,'Ξ': str("‌Xi")
	,'Ο': str("‌Omicron")
	,'Π': str("‌Pi")
	,'Ρ': str("‌Rho")
	,'Σ': str("‌Sigma")
	,'Τ': str("‌Tau")
	,'Υ': str("‌Upsilon")
	,'Φ': str("‌Phi")
	,'Χ': str("‌Chi")
	,'Ψ': str("‌Psi")
	,'Ω': str("Omega")
	,'α': str("‌alpha")
	,'β': str("‌beta")
	,'γ': str("‌gamma")
	,'δ': str("‌delta")
	,'ε': str("‌epsilon")
	,'ζ': str("‌zeta")
	,'η': str("‌eta")
	,'θ': str("‌theta")
	,'ι': str("‌iota")
	,'κ': str("‌kappa")
	,'λ': str("‌lambda")
	,'μ': str("‌mu")
	,'ν': str("‌nu")
	,'ξ': str("‌xi")
	,'ο': str("‌omicron")
	,'π': str("‌pi")
	,'ρ': str("‌rho")
	,'σ': str("‌sigma")
	,'τ': str("‌tau")
	,'υ': str("‌upsilon")
	,'φ': str("‌phi")
	,'χ': str("‌chi")
	,'ψ': str("‌psi")
	,'ω': str("omega")
}

class More(QWidget):
	def __init__(self):
		super().__init__()
		self.title = "More Symbols"
		self.left = 10
		self.top = 10
		self.width = 480
		self.height = 320
		self.numcols = 10
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.setWindowTitle(self.title)
		self.createLayout()
		self.parent = None
	
	def createLayout(self):
		grid = QGridLayout()
		for index, (key, value) in enumerate(symbols.items()):
			b = QPushButton(key)
			b.setMinimumWidth(20)
			b.setMinimumHeight(20)
			grid.addWidget(b, index // self.numcols, index % self.numcols)
			# Use lambdas to connect to functions
			b.clicked.connect(lambda state, txt=symbols[key]: self.addText(txt))
			
		self.setLayout(grid)
		
	def addText(self, txt):
		#txt.replace(u'\x80\x8c', '\\')
		# Remove zero width non joiner character
		t = str(sl + txt[1:] + ' ')
		if ascii(txt) != "'" + txt + "'":
			print("[WARNING]: Undefined unicode crap in the text to insert")
			print("Got: " + ascii(txt) + " instead of " + str(txt))
			print("Removed zero width non joiner")
		self.parent.insertIntoTexBox(t)
		#self.parent.fetchPreview()
