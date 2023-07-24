import datetime
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import qt_PitynaUI
import pityna

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.pityna = pityna.Pityna('pityna')
        self.action = True
        self.ui = qt_PitynaUI.Ui_MainWindow()
        self.log = []
        
        self.ui.setupUi(self)
        
    def putlog(self, str):
        self.ui.listWidgetLog.addItem(str)
        self.log.append(str + '\n')
        
    def prompt(self):
        p = self.pityna.get_name()
        if self.action == True:
            p += ':' + self.pityna.get_responder_name()
            
        return p + '> '
    
    def change_looks(self):
        em = self.pityna.emotion.mood
        
        if -5 <= em <=5:
            self.ui.labelShowImg.setPixmap(QtGui.QPixmap(":/re/talk.gif"))
        elif -10 <= em < -5:
            self.ui.labelShowImg.setPixmap(QtGui.QPixmap(":/re/empty.gif"))
        elif -15 <= em <= -10:
            self.ui.labelShowImg.setPixmap(QtGui.QPixmap(":/re/angry.gif"))
        elif 5 <= em <= 15:
            self.ui.labelShowImg.setPixmap(QtGui.QPixmap(":/re/happy.gif"))

    def writeLog(self):
        now = 'Pityna System Dialogue Log: '\
            + datetime.datetime.now().strftime('%Y-%m-%d %H:%m::%S')\
            + '\n'
        
        self.log.insert(0, now)
        with open('dics/log.txt', 'a', encoding='utf_8') as f:
            f.writelines(self.log)

    def buttonTalkSlot(self):
        value = self.ui.lineEdit.text()
        
        if not value:
            self.ui.labelResponce.setText('なに？')
        else:
            response = self.pityna.dialogue(value)
            self.ui.labelResponce.setText(response)
            self.putlog('> ' + value)
            self.putlog(self.prompt() + response)
            self.ui.lineEdit.clear()

        self.change_looks()
            
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(
            self,
            "あのねー",
            "ランダム辞書を更新してもいい?",
            buttons = QtWidgets.QMessageBox.Yes | 
            QtWidgets.QMessageBox.No 
            )
        
        if reply == QtWidgets.QMessageBox.Yes:
            self.pityna.save()
            self.writeLog()
            event.accept()
        else:
            event.accept()
            
    def showResponderName(self):
        self.action = True
        
    def hiddenResponderName(self):
        self.action = False