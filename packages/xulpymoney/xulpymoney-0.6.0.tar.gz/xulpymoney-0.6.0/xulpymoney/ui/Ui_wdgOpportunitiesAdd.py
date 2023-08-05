# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/wdgOpportunitiesAdd.ui'
#
# Created by: PyQt5 UI code generator 5.12.dev1812231618
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wdgOpportunitiesAdd(object):
    def setupUi(self, wdgOpportunitiesAdd):
        wdgOpportunitiesAdd.setObjectName("wdgOpportunitiesAdd")
        wdgOpportunitiesAdd.resize(959, 260)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/bank.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        wdgOpportunitiesAdd.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(wdgOpportunitiesAdd)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl = QtWidgets.QLabel(wdgOpportunitiesAdd)
        self.lbl.setMinimumSize(QtCore.QSize(800, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setText("")
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout.addWidget(self.lbl)
        self.productSelector = wdgProductSelector(wdgOpportunitiesAdd)
        self.productSelector.setObjectName("productSelector")
        self.verticalLayout.addWidget(self.productSelector)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.deDate = QtWidgets.QDateEdit(wdgOpportunitiesAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deDate.sizePolicy().hasHeightForWidth())
        self.deDate.setSizePolicy(sizePolicy)
        self.deDate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.deDate.setCalendarPopup(True)
        self.deDate.setObjectName("deDate")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.deDate)
        self.label_2 = QtWidgets.QLabel(wdgOpportunitiesAdd)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtEntry = myQLineEdit(wdgOpportunitiesAdd)
        self.txtEntry.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtEntry.setObjectName("txtEntry")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtEntry)
        self.label_5 = QtWidgets.QLabel(wdgOpportunitiesAdd)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label = QtWidgets.QLabel(wdgOpportunitiesAdd)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_3 = QtWidgets.QLabel(wdgOpportunitiesAdd)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtStoploss = myQLineEdit(wdgOpportunitiesAdd)
        self.txtStoploss.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtStoploss.setObjectName("txtStoploss")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtStoploss)
        self.txtTarget = myQLineEdit(wdgOpportunitiesAdd)
        self.txtTarget.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtTarget.setObjectName("txtTarget")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtTarget)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonbox = QtWidgets.QDialogButtonBox(wdgOpportunitiesAdd)
        self.buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonbox.setCenterButtons(True)
        self.buttonbox.setObjectName("buttonbox")
        self.verticalLayout.addWidget(self.buttonbox)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(wdgOpportunitiesAdd)
        QtCore.QMetaObject.connectSlotsByName(wdgOpportunitiesAdd)
        wdgOpportunitiesAdd.setTabOrder(self.txtEntry, self.txtTarget)
        wdgOpportunitiesAdd.setTabOrder(self.txtTarget, self.txtStoploss)
        wdgOpportunitiesAdd.setTabOrder(self.txtStoploss, self.deDate)

    def retranslateUi(self, wdgOpportunitiesAdd):
        _translate = QtCore.QCoreApplication.translate
        self.deDate.setDisplayFormat(_translate("wdgOpportunitiesAdd", "yyyy/MM/dd"))
        self.label_2.setText(_translate("wdgOpportunitiesAdd", "Opportunity date"))
        self.txtEntry.setText(_translate("wdgOpportunitiesAdd", "0"))
        self.label_5.setText(_translate("wdgOpportunitiesAdd", "Entry"))
        self.label.setText(_translate("wdgOpportunitiesAdd", "Target"))
        self.label_3.setText(_translate("wdgOpportunitiesAdd", "Stop loss"))
        self.txtStoploss.setText(_translate("wdgOpportunitiesAdd", "0"))
        self.txtTarget.setText(_translate("wdgOpportunitiesAdd", "0"))

from xulpymoney.ui.myqlineedit import myQLineEdit
from xulpymoney.ui.wdgProductSelector import wdgProductSelector
import xulpymoney.images.xulpymoney_rc
