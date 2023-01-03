
# This is our main file. This project is made by our team.
# We will never access the DB from here for security and encapsulations reasons.

# Any msgs that declare where is the bug shall never be seen by an end user.
# Any code that ends with ^^ means it has been unit tested
import datetime
import Human
import csv
import sqlite3

DB = Human.dataBase()  # An object to access DB


def createPerson():  # Here we simply create a person. This person will not be stored till check-in returns true.^^  READ ME:
    # I reversed between id and sex ( It won't matter but still you must know). And it is too late to change.

    firstName = str(input("Enter first name: "))
    lastName = str(input("Enter last name: "))
    sex = str(input("Enter gender: "))
    id = str(input("Enter Id: "))
    yearOfBirth = str(input("Enter Year of birth: "))
    typeOfVaccine = str(input("Enter Type of Vaccine: "))
    dateAndTime = str(input("Enter Date&time "))
    phoneNumber = str(input("Enter phone number: "))
    newPerson = Human.Person(firstName, lastName, sex, id, yearOfBirth, typeOfVaccine, dateAndTime, phoneNumber)
    return newPerson


### WE DON"T ACCEPT whitespace of any kind ( This will make it easier to manage)
# If .... etc will return false if it isn't accepted ( There will be a msg to show what is wrong exactly)
# If a method returns 1 means whatever inserted is accepted otherwise it will return a negative number (You need to see the implementation to know what each number means)

def checkIn(person): #^^ if all of the flags return true then person should be accepted in DB.
    print()
    fn = True
    ln = True
    pid = True
    sex = True
    yob = True
    tov = True
    dt = True
    pn = True

    if (checkInName(person.firstName) != 1):  #We check first name ^^
        fn = False
    if (checkInName(person.lastName) != 1):  # We check 2nd name. ^^
        ln = False


    if (checkSex(person.sex) != 1):  # Will check if the user inserted M or F ( May get removed if we force the user to chose between 2) Works perfectly^^
        sex = False

    if (checkId(person.id) != 1):  # we have yet to see if duplicate or not we just made sure that given id is valid. Works perfectly^^
        pid = False
    if  (DB.checkDuplicate(person.id,person.dt) != 1): # We are not injecting anything in our DB we are just checking
        pid = False

    if (checkDOB(person.yob) != 1):  # will check if the user enter valid YOB or not. Works perfectly^^
        yob = False
    if (checkTypeOfVac(person.tov) != 1):  # Will check if the user enter valid vac or not. ^^
        tov = False
    if (checkDate(person.dt) != 1): #Will check date and time and AM or PM This part of code was thoroughly tested. but it is tooo big to be declared perfect yet.
        dt = False
    if (phoneNumber(person.pn) != 1): # Will check phoneNumber
        pn = False
    return fn, ln, pid,sex,yob,tov,dt,pn # Every error will have it is own msg. WE HAVE NOT stored this person yet.


def checkInName(name):  #-1 for white space. -2 for alphabets. ^^
    try:
        if not (name.isalnum()):  # Check if there is whitespace.
            print("Can't have whitespace in your name")
            return -1
        elif (name.isalpha()):
            return 1
        else:
            print("Name can only be made of alphabets.")
            return -2
    except:
        print("A problem does exist in checkInName. This part of code shall never be triggered.")  # WILL NEVER TRIGGER
        exit()  # We will exit to make sure that the integrity of our DB isn't damaged.


def checkId(id):  #-1 for whitespaces. -2 for digits. -3 for length.  Works perfectly^^

    try:

        if not (id.isalnum()):  # Check if there is whitespace.
            print("can't have whitespaces in an id.")
            return -1
        elif not (id.isdigit()):  # check if all digits or not
            print("Id is only made of digits.")
            return -2
        elif (len(id) != 10):  # check if ID is 10 digits
            print('IDs are only made of 10 digits, kindly check your info.')
            return -3
        else:
            return 1
    except:
        print(
            "A problem does exist in checkID. This part of code in theory shall never be triggered. ")  # WILL NEVER TRIGGER
        exit()  # We will exit to make sure that the integrity of our DB isn't damaged.


def checkSex(sex):  #We only accept letter M or F as an input.  -1 for whitespaces. -2 for alphabets. -3 if the input is not F or M. ^^
    try:
        if not (sex.isalnum()):  # Check if there is whitespace.
            print("You can't have whitespace as your gender .")
            return -1
        elif not (sex.isalpha()):
            print("You can only enter alphabets")
            return -2
        elif (sex.lower() == 'f' or sex.lower() == 'm'):
            return 1
        else:
            print("We only allow for m and f as inputs")
            return -3

    except:
        print("A problem does exist in checkSex. This part of code in theory shall never be triggered.")
        exit()  # We will exit to make sure that the integrity of our DB isn't damaged.


def checkDOB(yob):  #-1  for whitespace. -2 for digits. -3 for length. -4 if less than or Equal 1900  or bigger  than or Equal 2003 ^^
    b = 1900
    c = 2003

    try:
        if not (yob.isalnum()):  # Check if there is whitespace.
            print("Can't have whitespace in your Year of birth.")
            return -1
        elif not (yob.isdigit()):  # Check if all digits or not.
            print("Please enter your year of birth as  digits")
            return -2
        elif (len(yob) != 4):  # check if it is made of 4 digits or not.
            print("Please enter a valid year. Try using the Gregorian calendar as your base. MUST BE 4 digits.")
            return -3

        elif (b < int(yob) and int(yob) < c):
            return 1
        else:
            print("Please enter a year bigger than 1900 and less than 2003")
            return -4

    except:
        print("A problem do exist in checkDOB. This part of code shall never be triggered.")
        exit()  # We will exit to make sure that the integrity of our DB isn't damaged.


def checkTypeOfVac(tov):  # -1 for invalid input. ^^
    vac1 = "pfizer"
    vac2 = "astrazeneca"
    vac3 = "moderna"
    vac4 = "j&j"
    try:
        if not (tov.lower() == vac1 or tov.lower() == vac2 or tov.lower() == vac3 or tov.lower() == vac4):
            print("Invalid type of vac, kindly check your info")
            return -1
        else:
            return 1

    except:
        print("A problem do exist in typeOfVac. This msg should never be triggered.")  # will never trigger
        exit()  # To keep the integrity of our DB.


def checkDate(dateAndTime):  #It works ^^. -1 time problem. -2 when we know there is problem but can't locate it ( Inputed in invalid way). -3 If under 2019
    isvalid = 1 # This was supposed to be a flag ( but we changed it)
    # It is vital that isvalid stays since finally will be executed regardless.
    try:

        date = dateAndTime[:dateAndTime.index(" ")]  # We separate date
        time = dateAndTime[dateAndTime.index(" ") + 1:]  # The rest
        if not (time.find("A") != -1 or time.find("a") != -1 or time.find("P") != -1 or time.find("p") != -1):  # We make sure if there is the format of AM or PM
            print("There is problem with the time.")
            isvalid = -1
            return -1
        elif not (
                time[time.find("A") + 1] == 'M' or time[time.find("A") + 1] == 'm' or time[time.find("a") + 1] == 'M' or
                time[time.find("a") + 1] == 'm' or
                time[time.find("P") + 1] == 'M' or time[time.find("P") + 1] == 'm' or time[time.find("p") + 1] == 'M' or
                time[time.find("p") + 1] == 'm'):
            print("There is problem with the time.")
            isvalid= -1
            return -1

        elif not (time[len(time) - 2:len(time) - 1] == "A" or time[len(time) - 2:len(time) - 1] == "P"
                  or time[len(time) - 2:len(time) - 1] == "p" or time[ len(time) - 2:len(   time) - 1] == "a"):
            print("There is problem with the time.")
            isvalid = -1
            return -1

        day, month, year = date.split('/')
    except ValueError:
        print("Incorrect time or date")
        isvalid = -2
        return -2
    except IndexError:  # I don't see anyway where it can triggers
        print("Incorrect time or date")
        isvalid = -2
        return -2
    except:
        print("An unexpected failure has occurred. (First part of checkDate)")
        isvalid = -1
        return -1
    try:
        time = time[:time.index(" ")]
        timeFormat = "%H:%M"
        datetime.datetime.strptime(time, timeFormat)
        datetime.datetime(int(year), int(month), int(day))
        if(int(year) < 2019):
            isvalid = -3
            return -3
    except ValueError:
        isvalid = -2
        return -2

    except:
        print("CheckDate got a problem. This msg should be never triggered")
        exit()  # We exit to defend the DB integrity

    finally:#must be checked !!
        if (isvalid == 1):
            return checkTime(time) # Last check because our setup is made for 24:00 time format
        else:
            return isvalid


def checkTime(time): # ^^ To check time sepretly. -1 if time got a problem.
    try:
        firstPart = time[:time.find(":")]
        length = len(firstPart)

        if (length == 2):
            start = firstPart[0]
            end = firstPart[1]
            if (int(start) > 1):
                return -1
            else:
                if(int(end) > 2):
                    return -1
                else:
                    return 1
        elif(length == 1):
            end = firstPart[0]
            if (int(end) < 1):
                return -1
            else:
                return 1
        else:
            return -1

    except :
        print("I Can't see this going wrong even if you try")
        exit()

def phoneNumber(pn): # -1 for white spaces. -2 for digits. -3 and -4 if the format are not respected. - 5 for length. ^^
    if not (pn.isalnum()):
        print("Can't have white space in your Phone Number.")
        return -1

    elif not(pn.isdigit()):
        print("Must be digits")
        return -2
    if  (pn[0] != "0"):
        print("First number not accepted")
        return -3
    if(pn[1] != "5"):
        print("Please Follow this Format: 05XXXXXXXX")
        return -4
    if(len(pn) != 10):
        print("Must be 10 numbers")
        return -5
    else:
        return 1

def checkInDB(person): #^^
    if all((checkIn(person))):
        DB.insertInto(person.firstName,person.lastName,person.sex,person.id,person.yob,person.tov,person.dt,person.pn)
        return 1
    else:
        print("Person not accepted!")
        return -1

def importCSV(name): # This code will simply import data if they are not valid he won't insert then in DB nothing more.
    # Will return 1 if there is no exception. ( AKA user didn't import something that isn't CSV). Will return -1 otherwise.

    try:
        with open(name) as csv_file:
            reader = csv.reader(csv_file)
            counter = 0
            for row in reader:
                counter = counter + 1
                fn = row[0]
                fn = fn.replace("'", "")
                ln = row[1]
                ln = ln.replace("'", "")
                sex = row[2]  # Switch is here I simply made the mistake in CSV nothing more
                sex = sex.replace("'", "")
                ID = row[3]
                ID = ID.replace("'", "")
                YOB = row[4]
                YOB = YOB.replace("'", "")
                TOV = row[5]
                TOV = TOV.replace("'", "")
                DT = row[6]
                DT = DT.replace("'", "")
                PN = row[7]
                PN = PN.replace("'", "")
                a = Human.Person(fn, ln, sex, ID, YOB, TOV, DT,  PN)

                if (DB.checkDuplicate(ID,DT) != 1):  # We are not injecting anything in our DB we are just checking
                    return str(counter),DB.checkDuplicate(ID,DT),"Primary keys duplicated"

                elif(checkInName(fn) != 1):
                    return str(counter), checkInName(fn),"FirstName"

                elif(checkInName(ln) != 1):
                    return str(counter), checkInName(ln),"SecondName"

                elif (checkSex(sex) != 1):  # Will check if the user inserted M or F ( May get removed if we force the user to chose between 2) Works perfectly^^
                    return str(counter),checkSex(sex),"Sex"

                elif (checkId(ID) != 1):  # we have yet to see if duplicate or not we just made sure that given id is valid. Works perfectly^^
                    return str(counter),checkId(ID),"ID"

                elif (checkDOB(YOB) != 1):  # will check if the user enter valid YOB or not. Works perfectly^^
                    return str(counter),checkDOB(YOB),"YOB"
                elif (checkTypeOfVac(TOV) != 1):  # Will check if the user enter valid vac or not. ^^
                    return str(counter),checkTypeOfVac(TOV),"TOV"
                elif (checkDate(DT) != 1):  # Will check date and time and AM or PM This part of code was thoroughly tested. but it is tooo big to be declared perfect yet.
                    return str(counter),checkDate(DT),"DT"
                elif (phoneNumber(PN) != 1):  # Will check phoneNumber
                    return str(counter),phoneNumber(PN),"PN"
                else:
                    checkInDB(a)  # We switch places between sex and ID Because I messed it up!!!!
        return 1
    except IndexError:
        print("Seems your csv file does have a problem.")
        return -100
    except:
        return -1

def exportCSV(name): # Simply will execute.  Won't return anything.
    try:
        conn = sqlite3.connect("MainDB.db")
        cursor = conn.execute("SELECT * FROM RealTry ")
        with open(name+'.csv', 'w') as export:
            # fields = ['FirstName', 'LastName', 'Sex', 'ID', 'YOB', 'TOV', 'DT', 'PhoneNo']
            csv_writer = csv.writer(export, lineterminator='\n')
            # csv_writer.writerow(fields)
            for row in cursor:
                csv_writer.writerow(list(row))
        return 1
    except:
        return -1



# ----------------------------------------------------------

# Unit testing

#print(createPerson())

#print(checkInName(""))

#print(checkId(""))

#print(checkSex(""))

#print((checkDOB("")))

#print(checkTypeOfVac("J&J"))

#print(checkDate("21/12/2019 01:59 aM")) #// Follow this format Every space must be respected.

#print(checkTime("01:59 aM"))

#print(phoneNumber(""))
#----------------------------------------------------------------
#We are still doing unit testing but since a lot of functions relys on the rest we treat them as one ( This is not the same as system testing).
#
# checkInDB(Human.Person('Fahd', 'ahmado', 'M', '1812020270', '1999', 'Pfizer', '12/10/2021 10:30 AM', '0507977225'))
# print(DB.checkDuplicate("1812020270","12/10/2021 10:33 AM"))
# DB.printDB()
#
# #exportCSV("FirstExp.csv")
# #print("Done")
DB.printDB()
#
# print()
# print(importCSV("FirstEXP.csv"))
# print("Done")
# DB.printDB()
# print("---------------")
# exportCSV("FirstExp.csv")
#
# print()
#----------------------------------------------------------------
print(importCSV('ss'))
