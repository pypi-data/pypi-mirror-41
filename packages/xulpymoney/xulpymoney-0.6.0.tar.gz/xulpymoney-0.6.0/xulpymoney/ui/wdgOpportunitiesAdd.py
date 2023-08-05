import datetime
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from xulpymoney.opportunities import Opportunity
from xulpymoney.libxulpymoneyfunctions import qmessagebox
from xulpymoney.ui.Ui_wdgOpportunitiesAdd import Ui_wdgOpportunitiesAdd

class wdgOpportunitiesAdd(QWidget, Ui_wdgOpportunitiesAdd):
    def __init__(self, mem, opportunity=None,  parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.mem=mem
        self.opportunity=opportunity
        self.parent=parent

        self.productSelector.setupUi(self.mem, None)
        if opportunity==None:
            self.lbl.setText("Add new opportunity")
            self.deDate.setDate(datetime.date.today())
            self.opportunity=Opportunity(self.mem)
            self.productSelector.setSelected(None)
        else:
            self.lbl.setText("Edit opportunity")
            self.deDate.setDate(self.opportunity.date)
            self.txtEntry.setText(self.opportunity.entry)
            self.txtTarget.setText(self.opportunity.target)
            self.txtStoploss.setText(self.opportunity.stoploss)
            self.productSelector.setSelected(self.opportunity.product)

    @pyqtSlot()
    def on_buttonbox_accepted(self):
        if not (self.txtEntry.isValid()):
            qmessagebox(self.tr("Incorrect data. Try again."))
            return
        if self.productSelector.selected==None:
            qmessagebox(self.tr("You must select a product"))
            return
            
        self.opportunity.date=self.deDate.date().toPyDate()
        self.opportunity.entry=self.txtEntry.decimal()
        self.opportunity.target=self.txtTarget.decimal()
        self.opportunity.stoploss=self.txtStoploss.decimal()
        self.opportunity.product=self.productSelector.selected
        
        self.opportunity.save()
        self.mem.con.commit()
        self.parent.accept()

    @pyqtSlot()
    def on_buttonbox_rejected(self):
        self.parent.reject()
