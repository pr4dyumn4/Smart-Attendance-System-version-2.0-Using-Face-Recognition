import mysql.connector as mc
from mysql.connector import Error
from PyQt5.QtWidgets import QMessageBox
class data:
    def __init__(self, db):
        self.conn = mc.connect(
            host='localhost',
            user='root',
            password='1864',
            port='3306',
            database=db
        )
        if self.conn.is_connected():
            self.cur = self.conn.cursor(buffered=True)
            self.showconnection()
            print('Database connected')
    def register(self, tb, name, age, Department, email, year, sex, father_name, mother_name, phone, address, dob, pin, religion, nationality, caste, state, city):
        sql = ('INSERT INTO {} (name, age, Department, email ,year ,sex ,father_name ,mother_name ,phone ,address ,dob ,pin ,religion ,nationality ,caste ,state ,city) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'.format(tb))
        val = (name, int(age), Department, email, int(year), sex, father_name, mother_name, phone, address, dob, int(pin), religion, nationality, caste, state, city)
        self.cur.execute(sql, val)
        print(self.cur.rowcount, "record inserted.")
        self.showRegister()
        self.conn.commit()
    def update(self, tb, id, opp1, opp2, column):
        if column in ['age','year','pin']:
            sql = (f"UPDATE {tb} SET {column} = {opp1}, {column}= {opp2} WHERE sid = {id};")
        else:
            sql = (f"UPDATE {tb} SET {column} = '{opp1}', {column}= '{opp2}' WHERE sid = {id};")
        self.cur.execute(sql)
        print(self.cur.rowcount, "record updated.")
        self.showUpdate()
        self.conn.commit()
    def mark(self, tb, column, value, name):
        sql = "UPDATE {} SET {}=%s WHERE name=%s".format(tb, column)
        val = (value, name)
        try:
            self.cur.execute(sql, val)
            self.conn.commit()
            print(self.cur.rowcount, "record updated.")
            #self.showMark()
        except Error as e:
            print("Error updating record:", e)
    def delete(self, tb, name):
        sql = ("delete from {} where name='{}'".format(tb, name))
        self.cur.execute(sql)
        print(self.cur.rowcount, "record delete.")
        self.showDelete()
        self.conn.commit()
    def showall(self, tb):
        sql = ("select * from {}".format(tb))
        self.cur.execute(sql)
        b = self.cur.fetchall()
        return list(b)
    def showNo(self, tb):
        sql = "SELECT COUNT(*) FROM {}".format(tb)
        self.cur.execute(sql)
        result = self.cur.fetchone()
        total_rows = result[0]
        return total_rows
    def showAttendencetNo(self, tb,att):
        sql = "SELECT COUNT(*) FROM {} where attendence='{}'".format(tb,att)
        self.cur.execute(sql)
        result = self.cur.fetchone()
        total_rows = result[0]
        return total_rows
    def showallwhere(self, tb,columns,where):
        if where in ['none','None','null','NULL','Null','NONE']:
                self.cur.execute("select * from {} where {} is NULL;".format(tb,columns))
        elif columns in ['sid','year','age']:
                s = where
                got = ("select * from {} where {} = {};".format(tb,columns,int(s)))
                self.cur.execute(got)
        elif columns in ['attendence']:
                a = str(where)
                got = ("select * from {} where {} = '{}';".format(tb,columns,a.title()))
                self.cur.execute(got)
        elif columns in ['Department','sex']:
                b = str(where)
                got = ("select * from {} where {} = '{}';".format(tb,columns,b.upper()))
                self.cur.execute(got)
        elif columns in ['name','father_name','mother_name','religion','nationality','caste','state','city']:
                c = str(where)
                got = ("select * from {} where {} = '{}';".format(tb,columns,c.lower()))
                self.cur.execute(got)
        else:
                d = str(where)
                got = ("select * from {} where {} = '{}';".format(tb,columns,d))
                self.cur.execute(got)
        result = self.cur.fetchall()
        return list(result)
    def columns(self, tb):
        sql = ("select * from {}".format(tb))
        self.cur.execute(sql)
        b = self.cur.column_names
        return list(b)
    def showonly(self ,tb, a):
        op = self.columns(tb=tb)
        if a in op:
            sql = (f"select {a} from {tb}")
            self.cur.execute(sql)
            b = self.cur.fetchall()
        return list(b)
    def showconnection(self):
      msgBox = QMessageBox()
      msgBox.setIcon(QMessageBox.Information)
      msgBox.setText("Connected Successfully")
      msgBox.setWindowTitle("QMessageBox Example")
      msgBox.setStandardButtons(QMessageBox.Ok )
      msgBox.buttonClicked.connect(self.msgButtonClick)
      returnValue = msgBox.exec()
      if returnValue == QMessageBox.Ok:
         print('OK clicked')
    def showdisconnection(self):
      msgBox = QMessageBox()
      msgBox.setIcon(QMessageBox.Information)
      msgBox.setText("disconnected Successfully")
      msgBox.setWindowTitle("QMessageBox Example")
      msgBox.setStandardButtons(QMessageBox.Ok )
      msgBox.buttonClicked.connect(self.msgButtonClick)
      returnValue = msgBox.exec()
      if returnValue == QMessageBox.Ok:
         print('OK clicked')
    def showRegister(self):
      msgBox = QMessageBox()
      msgBox.setIcon(QMessageBox.Information)
      msgBox.setText("Registerd Successfully")
      msgBox.setWindowTitle("QMessageBox Example")
      msgBox.setStandardButtons(QMessageBox.Ok )
      msgBox.buttonClicked.connect(self.msgButtonClick)
      returnValue = msgBox.exec()
      if returnValue == QMessageBox.Ok:
         print('OK clicked')
    def showUpdate(self):
      msgBox = QMessageBox()
      msgBox.setIcon(QMessageBox.Information)
      msgBox.setText("updated Successfully")
      msgBox.setWindowTitle("QMessageBox Example")
      msgBox.setStandardButtons(QMessageBox.Ok )
      msgBox.buttonClicked.connect(self.msgButtonClick)
      returnValue = msgBox.exec()
      if returnValue == QMessageBox.Ok:
         print('OK clicked')
    def showDelete(self):
      msgBox = QMessageBox()
      msgBox.setIcon(QMessageBox.Information)
      msgBox.setText("Removed Successfully")
      msgBox.setWindowTitle("QMessageBox Example")
      msgBox.setStandardButtons(QMessageBox.Ok )
      msgBox.buttonClicked.connect(self.msgButtonClick)
      returnValue = msgBox.exec()
      if returnValue == QMessageBox.Ok:
         print('OK clicked')  
   
    def msgButtonClick(self,i):
      print("Button clicked is:",i.text())
    def __del__(self):
        self.cur.close()
        self.conn.close()
        self.showdisconnection()
if __name__ == "__main__":
    def main():
        dt = data('college')
        dt.mark(tb='classroom',column='attendence',value='Present',name='pradyumna')
    main() 