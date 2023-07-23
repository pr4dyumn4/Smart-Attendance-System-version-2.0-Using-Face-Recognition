from database import data
import pandas as pd
import datetime
from PyQt5.QtWidgets import QMessageBox
import matplotlib.pyplot as plt
class Excel:
    def __init__(self):
        super().__init__()
        da = data(db='college')
        self.a = da.showall(tb='classroom')
        self.all_Sid = []
        self.all_name = []
        self.all_age = []
        self.all_Department = []
        self.all_email = []
        self.all_year = []
        self.all_attendence = []
        self.all_sex = []
        self.all_father_name = []
        self.all_mother_name = []
        self.all_phone = []
        self.all_address = []
        self.all_dob = []
        self.all_pin = []
        self.all_religion = []
        self.all_nationality = []
        self.all_caste = []
        self.all_state = []
        self.all_city = []

    def Load(self):
        for sid,name, Department,  year,attendence, sex, father_name, mother_name, email, phone, address, dob, pin, religion, nationality, caste, state, city,age in self.a:
            self.all_Sid.append(sid)
            self.all_name.append(name)  # Append the student name to the 'all_name' list
            self.all_age.append(age)  # Append the student age to the 'all_age' list
            self.all_Department.append(Department)  # Append the student department to the 'all_Department' list
            self.all_email.append(email)  # Append the student email to the 'all_email' list
            self.all_year.append(year)  # Append the student year to the 'all_year' list
            self.all_sex.append(sex)  # Append the student sex to the 'all_sex' list
            self.all_father_name.append(father_name)  # Append the student's father's name to the 'all_father_name' list
            self.all_mother_name.append(mother_name)  # Append the student's mother's name to the 'all_mother_name' list
            self.all_phone.append(phone)  # Append the student phone number to the 'all_phone' list
            self.all_address.append(address)  # Append the student address to the 'all_address' list
            self.all_dob.append(dob)  # Append the student date of birth to the 'all_dob' list
            self.all_pin.append(pin)  # Append the student PIN to the 'all_pin' list
            self.all_religion.append(religion)  # Append the student religion to the 'all_religion' list
            self.all_nationality.append(nationality)  # Append the student nationality to the 'all_nationality' list
            self.all_caste.append(caste)  # Append the student caste to the 'all_caste' list
            self.all_state.append(state)  # Append the student state to the 'all_state' list
            self.all_city.append(city)  # Append the student city to the 'all_city' list
            self.all_attendence.append(attendence)

    def AddCSV(self):
        data = {
            'StudentID':self.all_Sid,
            'Name': self.all_name,
            'Age': self.all_age,
            'Department': self.all_Department,
            'Email': self.all_email,
            'Year': self.all_year,
            'Sex': self.all_sex,
            'Father Name': self.all_father_name,
            'Mother Name': self.all_mother_name,
            'Phone': self.all_phone,
            'Address': self.all_address,
            'Date of Birth': self.all_dob,
            'PIN': self.all_pin,
            'Religion': self.all_religion,
            'Nationality': self.all_nationality,
            'Caste': self.all_caste,
            'State': self.all_state,
            'City': self.all_city,
            'attendence': self.all_attendence
        }
        df = pd.DataFrame(data)
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'attendance_{current_date}.csv'

        df.to_csv(filename, index=False)
        print(f'CSV file "{filename}" created successfully.')


    def showDialog(self):
      msgBox = QMessageBox()
      msgBox.setIcon(QMessageBox.Information)
      msgBox.setText("Exported Successfully It is in CSV file")
      msgBox.setWindowTitle("QMessageBox Example")
      msgBox.setStandardButtons(QMessageBox.Ok )
      msgBox.buttonClicked.connect(self.msgButtonClick)
      returnValue = msgBox.exec()
      if returnValue == QMessageBox.Ok:
         print('OK clicked')
    def msgButtonClick(self,i):
      print("Button clicked is:",i.text())
    
if __name__ == '__main__':
    CS = Excel()
    CS.Load()
    CS.AddCSV()
