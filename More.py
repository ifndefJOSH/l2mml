from PyQt5.QtWidgets import (QWidget, QApplication, QComboBox, QDialog,
QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
QVBoxLayout, QPlainTextEdit, QPushButton, QMessageBox)
from PyQt5.QtGui import QIcon
from latex2mathml import converter
from PyQt5.QtCore import pyqtSlot

import sys
import PyQt5

import latex2mathml.converter

sl = chr(92)

symbols = {
	'Α': "‌Alpha"
	,'Β': "‌Beta"
	,'Γ': "‌Gamma"
	,'Δ': "‌Delta"
	,'Ε': "‌Epsilon"
	,'Ζ': "‌Zeta"
	,'Η': "‌Eta"
	,'Θ': "‌Theta"
	,'Ι': "‌Iota"
	,'Κ': "‌Kappa"
	,'Λ': "‌Lambda"
	,'Μ': "‌Mu"
	,'Ν': "‌Nu"
	,'Ξ': "‌Xi"
	,'Ο': "‌Omicron"
	,'Π': "‌Pi"
	,'Ρ': "‌Rho"
	,'Σ': "‌Sigma"
	,'Τ': "‌Tau"
	,'Υ': "‌Upsilon"
	,'Φ': "‌Phi"
	,'Χ': "‌Chi"
	,'Ψ': "‌Psi"
	,'Ω': "Omega"
	,'α': "‌alpha"
	,'β': "‌beta"
	,'γ': "‌gamma"
	,'δ': "‌delta"
	,'ε': "‌epsilon"
	,'ζ': "‌zeta"
	,'η': "‌eta"
	,'θ': "‌theta"
	,'ι': "‌iota"
	,'κ': "‌kappa"
	,'λ': "‌lambda"
	,'μ': "‌mu"
	,'ν': "‌nu"
	,'ξ': "‌xi"
	,'ο': "‌omicron"
	,'π': "‌pi"
	,'ρ': "‌rho"
	,'σ': "‌sigma"
	,'τ': "‌tau"
	,'υ': "‌upsilon"
	,'φ': "‌phi"
	,'χ': "‌chi"
	,'ψ': "‌psi"
	,'ω': "omega"
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
		self.parent.insertIntoTexBox(sl + txt + ' ')
		#self.parent.fetchPreview()
