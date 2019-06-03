import sys
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from firebase import firebase
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


firebase = firebase.FirebaseApplication('https://reservationapp-2019.firebaseio.com/')
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("PyQt button example - pythonprogramminglanguage.com")

        submit = QPushButton('Submit ', self)
        submit.clicked.connect(self.clickMethod)
        submit.resize(280,32)
        submit.move(60, 250)

        self.reservationName = QLineEdit(self)
        self.reservationName.move(120, 50)
        self.reservationName.resize(150,20)
        #Date edit for check in
        self.checkInDateEdit = QtWidgets.QDateEdit(self)
        self.checkInDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.checkInDateEdit.setMaximumDate(QtCore.QDate(7999, 12, 28))
        self.checkInDateEdit.setCalendarPopup(True)
        self.checkInDateEdit.move(100,100)
        #Date edit for check-out
        self.checkOutDateEdit = QtWidgets.QDateEdit(self)
        self.checkOutDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.checkOutDateEdit.setMaximumDate(QtCore.QDate(7999, 12, 28))
        self.checkOutDateEdit.setCalendarPopup(True)
        self.checkOutDateEdit.move(230,100)

        self.rooms = QtWidgets.QSpinBox(self)
        self.rooms.setRange(1,9)
        self.rooms.move(60,150)
        self.adultsInRoom=QtWidgets.QSpinBox(self)
        self.adultsInRoom.setMinimum(1)
        self.adultsInRoom.move(160,150)
        self.childrenInRoom=QtWidgets.QSpinBox(self)
        self.childrenInRoom.setMinimum(1)
        self.childrenInRoom.move(260,150)

        self.reservationEmail = QLineEdit(self)
        self.reservationEmail.move(120, 220)
        self.reservationEmail.resize(160,20)
    def clickMethod(self):
        print('Your name: ' + self.reservationName.text())
        print('Your check In Date: ' + self.checkInDateEdit.text())
        print('Your check Out Date: ' + self.checkOutDateEdit.text())
        print('Your adults In Room: ' + self.adultsInRoom.text())
        print('Your Children In Room: ' + self.childrenInRoom.text())
        print('Your reservationEmail: ' + self.reservationEmail.text())

        result = firebase.post('/Reservation/', {"reservation":self.reservationEmail.text()+","+self.reservationName.text()+","+self.checkInDateEdit.text()+","+self.checkOutDateEdit.text()+"," +self.adultsInRoom.text()+","+self.childrenInRoom.text()})
        print(result)
        email_send=self.reservationEmail.text()
        email_user='Stanley-lam12@outlook.com'
        msg=MIMEMultipart()
        # me == the sender's email address
        msg['Subject'] = 'Reservation'
        msg['From'] = email_user
        msg['To'] = email_send
        content= "Dear...."
        msg.attach(MIMEText(content,'plain'))
        text= msg.as_string()
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,"A13499220k")
        server.sendmail(email_user,email_send,text)
        server.quit()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
