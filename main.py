import face_recog as fr
import database as db
from PyQt5 import QtCore,QtGui
from PyQt5.QtGui import QPainter, QPen 
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget, QDialog, QTableWidgetItem, QFileDialog, QMessageBox
import PyQt5
import os
import shutil
from Export import Excel
from PyQt5.Qt import Qt
import accuracytest
from Home import Ui_HomePage
from Dashboard import Ui_dashboard
from Management import Ui_Form
from Signup import Ui_MainWindow
from update import Ui_update
from Login import Ui_loginPage
from upload_ui import Ui_Upload
import sys
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
class LoginScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_loginPage()
        self.ui.setupUi(self)
class UpdateScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_update()
        self.ui.setupUi(self)
class RegisterScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
class HomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HomePage()
        self.ui.setupUi(self)
class ManagementScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
class DashboardScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_dashboard()
        self.ui.setupUi(self)
class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Create stacked widget
        self.stackedWidget = QStackedWidget(self)
        self.setCentralWidget(self.stackedWidget)
        # Create screens and add them to the stacked widget
        self.homeScreen = HomeScreen()
        self.dashboardScreen = DashboardScreen()
        self.managementScreen = ManagementScreen()
        self.RegisterScreen = RegisterScreen()
        self.updateScreen = UpdateScreen()
        self.loginScreen = LoginScreen()
        self.da = None
        self.cellData = None
        self.stackedWidget.addWidget(self.homeScreen)
        self.stackedWidget.addWidget(self.dashboardScreen)
        self.stackedWidget.addWidget(self.managementScreen)
        self.stackedWidget.addWidget(self.RegisterScreen)
        self.stackedWidget.addWidget(self.updateScreen)
        self.stackedWidget.addWidget(self.loginScreen)
        # Connect button signals to switch screens
        self.homeScreen.ui.pushButton.clicked.connect(self.showDashboardScreen)
        self.homeScreen.ui.pushButton_2.clicked.connect(self.showManagement)
        self.homeScreen.ui.pushButton_3.clicked.connect(self.scanner)
        self.dashboardScreen.ui.pushButton_2.clicked.connect(self.showHomeScreen)
        self.managementScreen.ui.pushButton_7.clicked.connect(self.showHomeScreen)
        self.RegisterScreen.ui.comboBox.addItem('BCA')
        self.RegisterScreen.ui.comboBox.addItem('BBA')
        self.RegisterScreen.ui.comboBox.addItem('BCOM')
        self.updateScreen.ui.pushButton_7.clicked.connect(self.showManagement)
        self.RegisterScreen.ui.pushButton_7.clicked.connect(self.showManagement)
        self.loginScreen.ui.pushButton.clicked.connect(self.condition)
        self.managementScreen.ui.pushButton_8.clicked.connect(self.connect)
        self.homeScreen.ui.pushButton_6.clicked.connect(self.showDialog)
        self.homeScreen.ui.pushButton_4.clicked.connect(self.csv)
        # Show the home screen initially
        self.showloginScreen() 
    def condition(self):
        if self.loginScreen.ui.lineEdit.text() == "Admin" and self.loginScreen.ui.lineEdit_2.text() == "123":
            self.showHomeScreen()
        else:
            self.showWarning()
    def showManagement(self):
        self.stackedWidget.setCurrentWidget(self.managementScreen)
        self.stackedWidget.setFixedSize(800,600)
        self.stackedWidget.setFixedHeight(600)
        self.stackedWidget.setFixedWidth(800)
        self.managementScreen.ui.pushButton_4.clicked.connect(self.remove)
        self.managementScreen.ui.pushButton_2.clicked.connect(self.clear1)
        self.managementScreen.ui.pushButton_9.clicked.connect(self.clear2)
    def showHomeScreen(self):
        self.stackedWidget.setCurrentWidget(self.homeScreen)
        self.stackedWidget.setFixedSize(800,600)
        self.stackedWidget.setFixedHeight(600)
        self.stackedWidget.setFixedWidth(800)
    def showRegisterScreen(self):
        self.stackedWidget.setCurrentWidget(self.RegisterScreen)
        self.stackedWidget.setFixedSize(800,600)
        self.stackedWidget.setFixedHeight(600)
        self.stackedWidget.setFixedWidth(800)
        self.RegisterScreen.ui.pushButton_2.clicked.connect(self.signin)
        self.RegisterScreen.ui.pushButton.clicked.connect(self.showUploadScreen)
        self.RegisterScreen.ui.pushButton_3.clicked.connect(self.clear3)
    def signin(self):
        self.name = self.RegisterScreen.ui.lineEdit.text()
        self.course = self.RegisterScreen.ui.comboBox.currentText()[:4]
        self.year = self.RegisterScreen.ui.lineEdit_2.text()  
        self.gender =  self.raddio_select()
        self.Mother = self.RegisterScreen.ui.lineEdit_4.text()
        self.Father = self.RegisterScreen.ui.lineEdit_3.text()
        self.Phone = self.RegisterScreen.ui.lineEdit_5.text()
        self.Email = self.RegisterScreen.ui.lineEdit_6.text()
        self.Address = self.RegisterScreen.ui.textEdit.toPlainText()
        self.Date = self.RegisterScreen.ui.dateEdit.text()
        self.pin = self.RegisterScreen.ui.lineEdit_7.text()
        self.religion = self.RegisterScreen.ui.lineEdit_8.text()
        self.nationality = self.RegisterScreen.ui.lineEdit_9.text()
        self.caste = self.RegisterScreen.ui.lineEdit_10.text()
        self.State = self.RegisterScreen.ui.lineEdit_11.text()
        self.city = self.RegisterScreen.ui.lineEdit_12.text()
        self.age = self.RegisterScreen.ui.lineEdit_13.text()
        year_int = 0
        age_int = 0
        pin_int = 0
        if self.name is None and self.course is None and self.year is None and self.gender is None and self.Mother is None and self.Father is None and self.Phone is None and self.Email is None and self.Address and self.Date is None and self.pin is None and self.religion is None and self.nationality is None and self.caste is None and self.State is None and self.city is None and self.age:
            pass
        if self.year and self.year.isdigit() and self.pin and self.pin.isdigit() and self.age and self.age.isdigit():
            year_int = int(self.year)
            age_int = int(self.age)
            pin_int = int(self.pin)
        self.da.register(tb=self.table, name=self.name,Department=self.course,year=year_int,sex=self.gender,father_name=self.Father,mother_name=self.Mother,phone=self.Phone,email=self.Email,address=self.Address,dob=self.Date,pin=pin_int,religion=self.religion,nationality=self.nationality,caste=self.caste,state=self.State,city=self.city,age=age_int)
    # Proceed with registration using year_int
        self.save(self.a)
    def showTable(self):
        try:
            self.managementScreen.ui.tableWidget.clear()
            results = self.da.showall(self.table)
            column_names = self.da.columns(self.table)
            self.managementScreen.ui.tableWidget.setColumnCount(len(column_names))  # Set the number of columns
            self.managementScreen.ui.tableWidget.setHorizontalHeaderLabels(column_names)  # Set the column names
            self.managementScreen.ui.tableWidget.setRowCount(len(results))  # Set the number of rows in the table widget
            self.managementScreen.ui.tableWidget.cellClicked.connect(self.showSelectedCellData)
            for row_no , row_data in enumerate(results):
                self.managementScreen.ui.tableWidget.insertRow(row_no)
                for col_no , data in enumerate(row_data):
                    self.managementScreen.ui.tableWidget.setItem(row_no,col_no,QTableWidgetItem(str(data)))
        except db.Error as e:
            self.showDialog()
        finally:
            print('Found Successfully')
    def showSelectedCellData(self, row, column):
        item = self.managementScreen.ui.tableWidget.item(row, column)
        if item is not None:
            self.cellData = item.text()
            print("Selected cell data:", self.cellData)
    def remove(self):
        if self.cellData is None or self.cellData == '':
            pass
        else:
            self.da.delete(tb=self.table,name=self.cellData)
            new_file_name = self.cellData+".jpg"  # Change this to your desired new name
            destination_directory = "./photos"
            if os.listdir(destination_directory):
                file_path = os.path.join(destination_directory, new_file_name)
                os.remove(file_path)
    def search(self):
        self.managementScreen.ui.tableWidget.clear()
        a = self.managementScreen.ui.lineEdit_Search.text()
        if a is None and a == '':
            pass
        column_names = self.da.columns(self.table)
        current_column_name = self.managementScreen.ui.comboBox.currentText()
        results = self.da.showallwhere(self.table,where=a,columns=current_column_name)
        self.managementScreen.ui.tableWidget.setColumnCount(len(column_names))  # Set the number of columns
        self.managementScreen.ui.tableWidget.setHorizontalHeaderLabels(column_names)  # Set the column names
        self.managementScreen.ui.tableWidget.setRowCount(len(results))
        for row_no , row_data in enumerate(results):
            self.managementScreen.ui.tableWidget.insertRow(row_no)
            for col_no , data in enumerate(row_data):
                self.managementScreen.ui.tableWidget.setItem(row_no,col_no,QTableWidgetItem(str(data)))
    def clear1(self):
        self.managementScreen.ui.tableWidget.clear()
        self.managementScreen.ui.lineEdit_Search.clear()
        
    def clear2(self):
        self.managementScreen.ui.lineEdit_Tb.clear()
        self.managementScreen.ui.lineEditDb.clear()
        self.managementScreen.ui.comboBox.clear()
        self.managementScreen.ui.tableWidget.clear()
        self.managementScreen.ui.lineEdit_Search.clear()
        self.da.__del__()
    def clear3(self):
        self.RegisterScreen.ui.lineEdit.clear()
        self.RegisterScreen.ui.comboBox.clear()
        self.RegisterScreen.ui.comboBox.addItem('Course')
        self.RegisterScreen.ui.comboBox.addItem('BCA')
        self.RegisterScreen.ui.comboBox.addItem('BBA')
        self.RegisterScreen.ui.comboBox.addItem('BCOM')
        self.RegisterScreen.ui.lineEdit_2.clear()  
        self.RegisterScreen.ui.lineEdit_4.clear()
        self.RegisterScreen.ui.lineEdit_3.clear()
        self.RegisterScreen.ui.lineEdit_5.clear()
        self.RegisterScreen.ui.lineEdit_6.clear()
        self.RegisterScreen.ui.textEdit.clear()
        self.RegisterScreen.ui.dateEdit.clear()
        self.RegisterScreen.ui.lineEdit_7.clear()
        self.RegisterScreen.ui.lineEdit_8.clear()
        self.RegisterScreen.ui.lineEdit_9.clear()
        self.RegisterScreen.ui.lineEdit_10.clear()
        self.RegisterScreen.ui.lineEdit_11.clear()
        self.RegisterScreen.ui.lineEdit_12.clear()
        self.RegisterScreen.ui.lineEdit_13.clear()
        self.RegisterScreen.ui.radioButton.setChecked(False)
        self.RegisterScreen.ui.radioButton_2.setChecked(False)
        self.RegisterScreen.ui.radioButton_3.setChecked(False)
        self.RegisterScreen.ui.label.clear()
        if os.listdir("tmp"):
            print("Folder is not empty.")
            os.remove("./tmp/temp.jpg")
        else:
            print("Folder is empty.")
            pass
    def showDashboardScreen(self):
        self.stackedWidget.setCurrentWidget(self.dashboardScreen)
        self.stackedWidget.setFixedSize(800,600)
        self.stackedWidget.setFixedHeight(600)
        self.stackedWidget.setFixedWidth(800)
        self.dashboardScreen.ui.pushButton_5.clicked.connect(self.connection)
    def showUpdateScreen(self):
        self.stackedWidget.setCurrentWidget(self.updateScreen)
        self.stackedWidget.setFixedSize(800,600)
        self.stackedWidget.setFixedHeight(600)
        self.stackedWidget.setFixedWidth(800)  
    def update(self):
        self.ID = self.updateScreen.ui.lineEdit.text()
        self.updateScreen.ui.comboBox.addItems(self.da.columns(tb=self.table))
        self.columns_comb = self.updateScreen.ui.comboBox.currentText()
        self.old_value =self.updateScreen.ui.lineEdit_2.text()
        self.new_value = self.updateScreen.ui.lineEdit_3.text()
        self.da.update(tb=self.table,id=self.ID,column=self.columns_comb,opp1=self.old_value,opp2=self.new_value)
    def showloginScreen(self):
        self.stackedWidget.setCurrentWidget(self.loginScreen)
        self.stackedWidget.setFixedSize(400,233)
        self.stackedWidget.setFixedHeight(233)
        self.stackedWidget.setFixedWidth(400)
    def showUploadScreen(self):
        UploadPage = QDialog()
        ui = Ui_Upload()
        ui.setupUi(UploadPage)
        ui.pushButton.clicked.connect(self.open_file_dialog)
        ui.pushButton_2.clicked.connect(self.Capture)
        UploadPage.show()
        UploadPage.exec_()
    def Capture(self):
        accuracytest.capture_image()
        self.display_image("./tmp/temp.jpg")
    def raddio_select(self):
        if self.RegisterScreen.ui.radioButton.isChecked():
            return "M"
        elif self.RegisterScreen.ui.radioButton_2.isChecked():
            return "F"
        elif self.RegisterScreen.ui.radioButton_3.isChecked():
            return "Oth"
        else:
            pass
    def connect(self):
        try:
            self.database = self.managementScreen.ui.lineEdit_Tb.text()
            self.table = self.managementScreen.ui.lineEditDb.text()
            if self.database is None and self.table is None:
                pass
            self.da = db.data(self.database)
            if self.da.conn.is_connected():
                a = self.da.showNo(self.table)
                self.managementScreen.ui.pushButton_5.clicked.connect(self.showRegisterScreen)
                self.managementScreen.ui.comboBox.addItems(self.da.columns(tb=self.table))
                self.updateScreen.ui.comboBox.addItems(self.da.columns(tb=self.table))
                self.managementScreen.ui.pushButton_6.clicked.connect(self.showUpdateScreen)
                self.managementScreen.ui.pushButton_3.clicked.connect(self.showTable)
                self.managementScreen.ui.pushButton.clicked.connect(self.search)
                self.managementScreen.ui.lcdNumber.display(a)
        except db.Error as e:
            print(e)
        finally:
            print("successfully connect")
    def connection(self):
        try:
            self.database = self.dashboardScreen.ui.Databaseline.text()
            self.table = self.dashboardScreen.ui.Tableline.text()
            if self.database is None and self.table is None:
                pass
            self.da = db.data(self.database)
            if self.da.conn.is_connected():
                self.present = self.da.showAttendencetNo(self.table,att='Present')
                self.absent = self.da.showAttendencetNo(self.table,att='Absent')
                self.dashboardScreen.ui.comboBox.addItems(self.da.columns(tb=self.table))
                self.dashboardScreen.ui.pushButton_6.clicked.connect(self.create_piechart_3)
                self.dashboardScreen.ui.pushButton.clicked.connect(self.showsingle)
                self.dashboardScreen.ui.PresentNumber.display(self.present)
                self.dashboardScreen.ui.PresentNumber.setStyleSheet("QLCDNumber { background-color: green; }")
                self.dashboardScreen.ui.AbsentNumber.display(self.absent)
                self.dashboardScreen.ui.AbsentNumber.setStyleSheet("QLCDNumber { background-color: red; }")
                self.dashboardScreen.ui.tableWidget.clear()
                results = self.da.showall(self.table)
                column_names = self.da.columns(self.table)
                self.dashboardScreen.ui.tableWidget.setColumnCount(len(column_names))  # Set the number of columns
                self.dashboardScreen.ui.tableWidget.setHorizontalHeaderLabels(column_names)  # Set the column names
                self.dashboardScreen.ui.tableWidget.setRowCount(len(results))  # Set the number of rows in the table widget
                self.dashboardScreen.ui.tableWidget.cellClicked.connect(self.showSelectedCellData)
                for row_no , row_data in enumerate(results):
                    self.dashboardScreen.ui.tableWidget.insertRow(row_no)
                    for col_no , data in enumerate(row_data):
                        self.dashboardScreen.ui.tableWidget.setItem(row_no,col_no,QTableWidgetItem(str(data)))
        except db.Error as e:
            print(e)
        finally:
            print("successfully connect")
    
    def showsingle(self):
        self.dashboardScreen.ui.tableWidget.clear()
        a =self.dashboardScreen.ui.comboBox.currentText()
        results = self.da.showonly(tb=self.table,a=a)
        column_names = self.da.columns(self.table)
        self.dashboardScreen.ui.tableWidget.setColumnCount(len(column_names))  # Set the number of columns
        self.dashboardScreen.ui.tableWidget.setHorizontalHeaderLabels(column_names)  # Set the column names
        self.dashboardScreen.ui.tableWidget.setRowCount(len(results))  # Set the number of rows in the table widget
        for row_no , row_data in enumerate(results):
            self.dashboardScreen.ui.tableWidget.insertRow(row_no)
            for col_no , data in enumerate(row_data):
                self.dashboardScreen.ui.tableWidget.setItem(row_no,col_no,QTableWidgetItem(str(data)))
    def create_piechart_3(self):
        if hasattr(self, "chartview"):
            self.layout().removeWidget(self.chartview)
            self.chartview.setParent(None)
            self.chartview = None
        a = self.absent
        b = self.present
        series = QPieSeries()
        series.append("Absent", a)
        series.append("Present", b)
        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Pie Chart of Attendance")
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        self.chartview = chartview
        self.dashboardScreen.ui.verticalLayout_2.addWidget(self.chartview)
    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
        file_dialog.fileSelected.connect(self.display_image)
        file_dialog.exec_()
    def csv(self):
        CS = Excel()
        CS.Load()
        CS.AddCSV()
    def display_image(self, file_path):
        pixmap =  QtGui.QPixmap(file_path)
        self.RegisterScreen.ui.label.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio))
        self.a = file_path
    def save(self,file_path):
        new_file_name = self.RegisterScreen.ui.lineEdit.text()+".jpg"  # Change this to your desired new name
        destination_directory = "./photos"  # Change this to your desired destination directory

        # Construct the new file path
        new_file_path = os.path.join(destination_directory, new_file_name)

        # Copy the image file to the new directory with the new name
        os.makedirs(destination_directory, exist_ok=True)  # Create the destination directory if it doesn't exist
        shutil.copy(file_path, new_file_path)
    
# Display a message box indicating that we have successfully copied and renamed our photo!
    def showDialog(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Are You Sure want to Exit")
        msgBox.setWindowTitle("QMessageBox Example")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.buttonClicked.connect(self.msgButtonClick)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            if self.da is not None :
                self.cleanup()
            sys.exit()
    def showWarning(self):
      msgBox = QMessageBox()
      msgBox.setIcon(QMessageBox.Information)
      msgBox.setText("Wrong password wrong admin name")
      msgBox.setWindowTitle("QMessageBox Example")
      msgBox.setStandardButtons(QMessageBox.Ok )
      msgBox.buttonClicked.connect(self.msgButtonClick)
      returnValue = msgBox.exec()
      if returnValue == QMessageBox.Ok:
         print('OK clicked')
    def showScan(self):
      msgBox = QMessageBox()
      msgBox.setIcon(QMessageBox.Information)
      msgBox.setText("Scanned Successfully")
      msgBox.setWindowTitle("QMessageBox Example")
      msgBox.setStandardButtons(QMessageBox.Ok )
      msgBox.buttonClicked.connect(self.msgButtonClick)
      returnValue = msgBox.exec()
      if returnValue == QMessageBox.Ok:
         print('OK clicked')
    def msgButtonClick(self,i):
      print("Button clicked is:",i.text())    
    def cleanup(self):
        # Perform cleanup operations here
        if self.da is not None :
            self.da.__del__() # Replace with the appropriate cleanup method for the 'da' object
    
    def scanner(self):
        self.scan = fr.FaceRecognizer()
        self.scan.load_samples()
        self.scan.main()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    app.exec_()

