from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main_window import Ui_MainWindow
from dialog import Ui_Dialog
from stylesheets import main_style_sheet
from stylesheets import dialog_style_sheet
class Dialog(QDialog):
    def __init__(self,parent=None):
        super(Dialog,self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setStyleSheet(dialog_style_sheet)


class MainWindow(QMainWindow, Ui_MainWindow, Ui_Dialog  ):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)

        #setting up the UI
        self.setupUi(self)
        self.btn_new_task.clicked.connect(self.add_tasks)
        self.done = []
        self.undone = []

        self.btn_done.clicked.connect(self.doneTask)
        self.btn_undone.clicked.connect(self.undoneTask)
        self.setStyleSheet(main_style_sheet)
       
    
    def doneTask(self):
        task = self.listWidget_2.takeItem(self.listWidget_2.currentRow())
        self.listWidget.addItem(task.text())

    def undoneTask(self):
        task = self.listWidget.takeItem(self.listWidget.currentRow())
        self.listWidget_2.addItem(task.text())
    def add_tasks(self):
        dlog = Dialog()
        dlog.ui.buttonBox.accepted.connect(
            lambda: ( self.read_task(dlog.ui.lineEdit.text()))
        )
        dlog.exec()
    
    def read_task(self,task):
        if bool(task) != False:
            self.listWidget_2.addItem(task)
        

app = QApplication([])
window = MainWindow()
window.show()
app.exec()