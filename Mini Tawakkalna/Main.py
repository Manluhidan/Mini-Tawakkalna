import sys
import Tawaklna
import Human
from MainScreen import Ui_MainWindow
from CheckIn import Ui_CheckIN
from ImmunityCheck import Ui_ImmunityCheck
from Import import Ui_Import
from Export import Ui_Export
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QMainWindow, QMessageBox, QFileDialog


class mainscreen(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mainscreen, self).__init__()
        self.setupUi(self)
        self.Check_in.clicked.connect(self.gotocheckin)
        self.ImCheck.clicked.connect(self.gotimmunitycheck)
        self.Import.clicked.connect(self.gotoimport)
        self.Export.clicked.connect(self.gotoexport)

    def gotocheckin(self):
        page = Checkin()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotimmunitycheck(self):
        page = ImmunityCheck()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoimport(self):
        page = Import()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoexport(self):
        page = Export()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Checkin(QMainWindow, Ui_CheckIN):
    def __init__(self):
        super(Checkin, self).__init__()
        self.setupUi(self)
        self.Checked_in.clicked.connect(self.checkedin)
        self.Go_Back.clicked.connect(self.gotomainscreen)

    def checkedin(self):
        count = 0
        self.error_2.setText("")
        self.error_3.setText("")
        self.error_4.setText("")
        self.error_5.setText("")
        self.error_6.setText("")
        self.error_7.setText("")
        self.error_8.setText("")
        self.error_9.setText("")

        person = Human.Person
        person.firstName = self.fnameField.text()
        person.lastName = self.lnameField.text()
        person.id = self.idField.text()
        person.sex = self.genderField.text()
        person.yob = self.ybField.text()
        person.tov = self.tvField.text()
        person.dt = self.dtField.text()
        person.pn = self.pnField.text()

        # Error First Name
        if Tawaklna.checkInName(person.firstName) == -1:
            self.error_2.setText("Can't have whitespace in your name.")
        elif Tawaklna.checkInName(person.firstName) == -2:
            self.error_2.setText("Name can only be made of alphabets.")
        else:
            count += 1

        # Error Last Name
        if Tawaklna.checkInName(person.lastName) == -1:
            self.error_3.setText("Can't have whitespace in your name.")
        elif Tawaklna.checkInName(person.lastName) == -2:
            self.error_3.setText("Name can only be made of alphabets.")
        else:
            count += 1

        # Error ID
        if Tawaklna.checkId(person.id) == -1:
            self.error_4.setText("can't have whitespaces in an id.")
        elif Tawaklna.checkId(person.id) == -2:
            self.error_4.setText("Id is only made of digits.")
        elif Tawaklna.checkId(person.id) == -3:
            self.error_4.setText("IDs are only made of 10 digits, kindly check your info.")
        else:
            count += 1

        # Error Gender
        if Tawaklna.checkSex(person.sex) == -1:
            self.error_5.setText("You can't have whitespace as your gender.")
        elif Tawaklna.checkSex(person.sex) == -2:
            self.error_5.setText("You can only enter alphabets.")
        elif Tawaklna.checkSex(person.sex) == -3:
            self.error_5.setText("We only allow for M and F as inputs.")
        else:
            count += 1

        # Error year of birth
        if Tawaklna.checkDOB(person.yob) == -1:
            self.error_6.setText("Can't have whitespace in your Year of birth.")
        elif Tawaklna.checkDOB(person.yob) == -2:
            self.error_6.setText("Please enter your year of birth as  digits.")
        elif Tawaklna.checkDOB(person.yob) == -3:
            self.error_6.setText("Please enter a valid year. Try using the Gregorian calendar as your base. MUST BE 4 digits.")
        elif Tawaklna.checkDOB(person.yob) == -4:
            self.error_6.setText("Please enter a year bigger than 1900 and less than 2003.")
        else:
            count += 1

        # Error Type of Vac
        if Tawaklna.checkTypeOfVac(person.tov) == -1:
            self.error_7.setText("Invalid type of vac, kindly check your info.")
        else:
            count += 1

        # Error Date and Time
        db = Human.dataBase()
        if Tawaklna.checkDate(person.dt) == -1:
            self.error_8.setText("There is problem with the time.")
        elif Tawaklna.checkDate(person.dt) == -2:
            self.error_8.setText("Incorrect time or date.")
        elif Tawaklna.checkDate(person.dt) == -3:
            self.error_8.setText("Must be above 2018.")
        elif (db.checkDuplicate(person.id,person.dt) == -1):
            self.error_8.setText("You can' take 2 shots at same time !")
        else:
            count += 1

        # Error Phone Number
        if Tawaklna.phoneNumber(person.pn) == -1:
            self.error_9.setText("Can't have white space in your Phone Number.")
        elif Tawaklna.phoneNumber(person.pn) == -2:
            self.error_9.setText("Must be digits.")
        elif Tawaklna.phoneNumber(person.pn) == -3:
            self.error_9.setText("First number not accepted.")
        elif Tawaklna.phoneNumber(person.pn) == -4:
            self.error_9.setText("Please Follow this Format: 05XXXXXXXX.")
        elif Tawaklna.phoneNumber(person.pn) == -5:
            self.error_9.setText("Must be 10 numbers.")
        else:
            count += 1
        if count == 8 and Tawaklna.checkInDB(person) == 1:
            msg = QMessageBox()
            msg.setWindowTitle("Checked in")
            msg.setWindowIcon(QIcon('tawakkalna.png'))
            msg.setText("Successfully Checked in!")
            msg.setIcon(QMessageBox.Information)
            msg.buttonClicked.connect(self.gotomainscreen)
            run = msg.exec_()
        else:
            if count == 8 and Tawaklna.checkInDB(person) == -1:
                msg = QMessageBox()
                msg.setWindowTitle("Checked in")
                msg.setWindowIcon(QIcon('tawakkalna.png'))
                msg.setText("This Person is Fully Vaccinated!")
                msg.setIcon(QMessageBox.Information)
                msg.buttonClicked.connect(self.gotomainscreen)
                run = msg.exec_()

    def gotomainscreen(self):
        main = mainscreen()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

class ImmunityCheck(QMainWindow, Ui_ImmunityCheck):
    def __init__(self):
        super(ImmunityCheck, self).__init__()
        self.setupUi(self)
        self.Check.clicked.connect(self.Immunity_Check)
        self.Go_Back.clicked.connect(self.gotomainscreen)

    def Immunity_Check(self):
        count = 0
        person = Human.Person
        person.id = self.idField.text()

        if Tawaklna.checkId(person.id) == -1:
            self.error.setText("can't have whitespaces in an id.")
        elif Tawaklna.checkId(person.id) == -2:
            self.error.setText("Id is only made of digits.")
        elif Tawaklna.checkId(person.id) == -3:
            self.error.setText("IDs are only made of 10 digits, kindly check your info.")
        else:
            count += 1

        db = Human.dataBase()
        shots = db.printStatus(person.id)
        if count == 1:
            if shots == 1:
                self.Vaccinated()
                msg = QMessageBox()
                msg.setWindowTitle("Immunity Check")
                msg.setWindowIcon(QIcon('tawakkalna.png'))
                msg.setText("Vaccinated ( with a single shot ).")
                msg.setIcon(QMessageBox.Information)
                msg.buttonClicked.connect(self.gotomainscreen)
                run = msg.exec_()
            elif shots == 2:
                self.FullyVaccinated()
                msg = QMessageBox()
                msg.setWindowTitle("Immunity Check")
                msg.setWindowIcon(QIcon('tawakkalna.png'))
                msg.setText("Fully Vaccinated ( with two shots ).")
                msg.setIcon(QMessageBox.Information)
                msg.buttonClicked.connect(self.gotomainscreen)
                run = msg.exec_()
            else:
                self.Unvaccinated()
                msg = QMessageBox()
                msg.setWindowTitle("Immunity Check")
                msg.setWindowIcon(QIcon('tawakkalna.png'))
                msg.setText("Not Vaccinated yet")
                msg.setIcon(QMessageBox.Information)
                msg.buttonClicked.connect(self.gotomainscreen)
                run = msg.exec_()

    def FullyVaccinated(self):
        Green = QPixmap('Green.png')
        self.Color.setPixmap(Green)

    def Vaccinated(self):
        Yellow = QPixmap('Yellow.png')
        self.Color.setPixmap(Yellow)

    def Unvaccinated(self):
        Red = QPixmap('Red.png')
        self.Color.setPixmap(Red)

    def gotomainscreen(self):
        page = mainscreen()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Import(QMainWindow, Ui_Import):
    def __init__(self):
        super(Import, self).__init__()
        self.setupUi(self)
        self.Import_bot.clicked.connect(self.importFile)
        self.Go_Back.clicked.connect(self.gotomainscreen)
        self.browse_bot.clicked.connect(self.browseFiles)

    def importFile(self):
        fileName = self.importField.text()
        imported = Tawaklna.importCSV(fileName)
        if imported == 1:
            msg = QMessageBox()
            msg.setWindowTitle("Import File")
            msg.setWindowIcon(QIcon('tawakkalna.png'))
            msg.setText("File Imported Successfully.")
            msg.setIcon(QMessageBox.Information)
            msg.buttonClicked.connect(self.gotomainscreen)
            run = msg.exec_()
        elif imported == -100:
            msg = QMessageBox()
            msg.setWindowTitle("Import File")
            msg.setWindowIcon(QIcon('tawakkalna.png'))
            msg.setText("Seems your csv file does have a problem.")
            msg.setIcon(QMessageBox.Information)
            msg.buttonClicked.connect(self.gotomainscreen)
            run = msg.exec_()
        elif imported == -1:
            msg = QMessageBox()
            msg.setWindowTitle("Import File")
            msg.setWindowIcon(QIcon('tawakkalna.png'))
            msg.setText("File not found !")
            msg.setIcon(QMessageBox.Information)
            msg.buttonClicked.connect(self.gotomainscreen)
            run = msg.exec_()
        else:
            # First name error
            if (imported[2] == 'Primary keys duplicated'):
                self.error.setText("Primary keys duplicated. Line: "+imported[0])

            elif imported[2] == 'FirstName':
                if imported[1] == -1:
                    self.error.setText("Can't have whitespace in your name. Line: "+imported[0])
                else:
                    self.error.setText("Name can only be made of alphabets. Line: "+imported[0])
            # Last name error
            elif imported[2] == 'SecondName':
                if imported[1] == -1:
                    self.error.setText("Can't have whitespace in your name. Line: "+imported[0])
                else:
                    self.error.setText("Name can only be made of alphabets. Line: "+imported[0])
            # ID error
            elif imported[2] == 'ID':
                if imported[1] == -1:
                    self.error.setText("can't have whitespaces in an id. Line: "+imported[0])
                elif imported[1] == -2:
                    self.error.setText("Id is only made of digits. Line: "+imported[0])
                else:
                    self.error.setText("IDs are only made of 10 digits, kindly check your info. Line: "+imported[0])
            # Gender error
            elif imported[2] == 'Sex':
                if imported[1] == -1:
                    self.error.setText("You can't have whitespace as your gender. Line: "+imported[0])
                elif imported[1] == -2:
                    self.error.setText("You can only enter alphabets. Line: "+imported[0])
                else:
                    self.error.setText("We only allow for M and F as inputs. Line: "+imported[0])
            # year of birth error
            elif imported[2] == 'YOB':
                if imported[1] == -1:
                    self.error.setText("Can't have whitespace in your Year of birth. Line: "+imported[0])
                elif imported[1] == -2:
                    self.error.setText("Please enter your year of birth as  digits. Line: "+imported[0])
                elif imported[1] == -3:
                    self.error.setText(
                        "Please enter a valid year. Try using the Gregorian calendar as your base. MUST BE 4 digits. Line: "+imported[0])
                else:
                    self.error.setText("Please enter a year bigger than 1900 and less than 2003. Line: "+imported[0])
            # Type of Vac error
            elif imported[2] == 'TOV':
                if imported[1] == -1:
                    self.error.setText("Invalid type of vac, kindly check your info. Line: "+imported[0])
            # Date and Time error
            elif imported[2] == 'DT':
                if imported[1] == -1:
                    self.error.setText("There is problem with the time. Line: "+imported[0])
                elif imported[1] == -2:
                    self.error.setText("Incorrect time or date. Line: "+imported[0])
                else:
                    self.error.setText("Must be above 2018. Line: "+imported[0])
            # Phone Number error
            elif imported[2] == 'PN':
                if imported[1] == -1:
                    self.error.setText("Can't have white space in your Phone Number. Line: "+imported[0])
                elif imported[1] == -2:
                    self.error.setText("Must be digits. Line: "+imported[0])
                elif imported[1] == -3:
                    self.error.setText("First number not accepted. Line: "+imported[0])
                elif imported[1] == -4:
                    self.error.setText("Please Follow this Format: 05XXXXXXXX. Line: "+imported[0])
                else:
                    self.error.setText("Must be 10 numbers. Line: "+imported[0])

    def browseFiles(self):
        Open = QFileDialog.getOpenFileName(self,'Open File','','CSV Files (*.csv)')
        self.importField.setText(Open[0])

    def gotomainscreen(self):
        page = mainscreen()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Export(QMainWindow, Ui_Export):
    def __init__(self):
        super(Export, self).__init__()
        self.setupUi(self)
        self.Export_bot.clicked.connect(self.exportFile)
        self.Go_Back.clicked.connect(self.gotomainscreen)
        self.browse_bot.clicked.connect(self.browseFiles)

    def exportFile(self):
        fileName = self.exportField.text()
        if fileName == '':
            msg = QMessageBox()
            msg.setWindowTitle("Export File")
            msg.setWindowIcon(QIcon('tawakkalna.png'))
            msg.setText("Something went wrong !")
            msg.setIcon(QMessageBox.Information)
            msg.buttonClicked.connect(self.gotomainscreen)
            run = msg.exec_()
        else:
            Tawaklna.exportCSV(fileName)
            msg = QMessageBox()
            msg.setWindowTitle("Export File")
            msg.setWindowIcon(QIcon('tawakkalna.png'))
            msg.setText("File Exported Successfully.")
            msg.setIcon(QMessageBox.Information)
            msg.buttonClicked.connect(self.gotomainscreen)
            run = msg.exec_()

    def browseFiles(self):
        Save = QFileDialog.getSaveFileName(self,'Save File')
        self.exportField.setText(Save[0])

    def gotomainscreen(self):
        page = mainscreen()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex()+1)



#Main
app = QApplication(sys.argv)
MS = mainscreen()
widget = QStackedWidget()
widget.setWindowTitle('Tawakkalna')
widget.setWindowIcon(QIcon('tawakkalna.png'))
widget.addWidget(MS)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")