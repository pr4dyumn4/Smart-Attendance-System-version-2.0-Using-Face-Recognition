import database as dt
from mysql.connector import Error
from PyQt5.QtWidgets import QMessageBox,QApplication,QWidget,QPushButton
from PyQt5 import QtWidgets
import os
import sys
class Mark:
   def __init__(self):      
      self.fob=open('attendence.txt','r')
      names = self.fob.read().split('\n')
      self.a = [x for x in names if x]
      print(self.a)
      #self.markattendence()
   def showDialog(self):
      msgBox = QMessageBox()
      msgBox.setIcon(QMessageBox.Information)
      msgBox.setText("Your Attendence have been marked")
      msgBox.setWindowTitle("QMessageBox Example")
      msgBox.setStandardButtons(QMessageBox.Ok )
      msgBox.buttonClicked.connect(self.msgButtonClick)
      returnValue = msgBox.exec()
      if returnValue == QMessageBox.Ok:
         print('OK clicked')
   def msgButtonClick(self,i):
      print("Button clicked is:",i.text())
   def dataname(self):
      self.data = dt.data('college')
      return self.data.showonly(tb='classroom',a='name')

   def markattendence(self):
      try:
         myresults = self.dataname()
         hot = {39:None,40:None,41:None,44:None,93:None,91:None}
         andy = str(myresults).translate(hot)               
         bunty = andy.split(' ')
         print(bunty)
         for g in bunty:
               if g in self.a:
                  self.data.mark(tb='classroom',column='attendence',value='Present',name=g)
                  print(g," is Present")
               else:
                  self.data.mark(tb='classroom',column='attendence',value='Absent',name=g)
                  print(g," is absent")
      except Error as e:
         dt.data.conn.rollback()
         print(e)
      finally:
         self.showDialog()
         self.fob.close()
if __name__=='__main__':
   mk = Mark()
   mk.markattendence()
'''
def window():
   app = QApplication(sys.argv)
   win = QWidget()
   button1 = QPushButton(win)
   button1.setText("Show dialog!")
   button1.move(50,50)
   button1.clicked.connect(markattendence)
   win.setWindowTitle("Click button")
   win.show()
   sys.exit(app.exec_())
'''

'''
if __name__ == '__main__': 
   window()
   '''
'''
def window():
   app = QApplication(sys.argv)
   win = QWidget()
   button1 = QPushButton(win)
   button1.setText("Show dialog!")
   button1.move(50,50)
   button1.clicked.connect(showDialog)
   win.setWindowTitle("Click button")
   win.show()
   sys.exit(app.exec_())
	
def showDialog():
   msgBox = QMessageBox()
   msgBox.setIcon(QMessageBox.Information)
   msgBox.setText("Message box pop up window")
   msgBox.setWindowTitle("QMessageBox Example")
   msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
   msgBox.buttonClicked.connect(msgButtonClick)

   returnValue = msgBox.exec()
   if returnValue == QMessageBox.Ok:
      print('OK clicked')
   
def msgButtonClick(i):
   print("Button clicked is:",i.text())
	
if __name__ == '__main__': 
   window()
'''
