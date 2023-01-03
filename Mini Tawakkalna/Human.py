#This class is used to make an object of a person if said person is in the DB we discard him
#We access our DB from here


import sqlite3
import csv


class Person:
    def __init__(self,fn,ln,sex,id,yob,tov,dt,pn): #Focus on the pos of ID and SEX in DB it was reversed.

        self.firstName = fn
        self.lastName = ln
        self.id = id
        self.sex = sex
        self.yob = yob
        self.tov = tov
        self.dt = dt
        self.pn = pn
    #OVERRIDE
    def __str__(self): # Just to make sure the person is made perfectly
        return self.firstName + self.lastName + "   "+self.id +self.sex +self.yob + self.tov +self.dt+self.pn


class dataBase: #This class will be used to access the data base if needed
    #To avoid any problems we force the program to access/create a new default DB.
    conn = sqlite3.connect("MainDB.db")
    # conn.execute('DROP TABLE IF EXISTS RealTry')
    try:
        conn.execute(''' CREATE TABLE "RealTry"(
                   FirstName TEXT NOT NULL,
                   LastName TEXT NOT NULL,
                   Sex TEXT NOT NULL,
                   ID NOT NULL,
                   YOB TEXT NOT NULL,
                   TOV TEXT NOT NULL,
                   DT TEXT NOT NULL,
                   PhoneNO TEXT NOT NULL,PRIMARY KEY (ID, DT));
                   ''')
        print("Table created successfully")
    except sqlite3.OperationalError:
        pass

    finally:
        conn.close()  # Every time we open it we must exit.


    conn.close()  # Every time we open it we must exit.

    def insertInto(self,fn,ln,sex,ID,YOB,TOV,DT,PN): # A simple insert into the DB We don't know if the data is valid. ^^
        conn = sqlite3.connect("MainDB.db")
        cur = conn.cursor()
        cur.execute('''
         INSERT INTO RealTry VALUES (?,?,?,?,?,?,?,?)
         ''', (fn, ln, sex, ID, YOB, TOV, DT, PN))
        conn.commit()
        conn.close()
        return True


    def printDB(self):
        #print("Running")
        conn = sqlite3.connect("MainDB.db") # DATABASE NAME
        cursor = conn.execute("SELECT FirstName,LastName,Sex,ID,YOB,TOV,DT,PhoneNO from Realtry") #^^

        for row in cursor:
            print(row)
        conn.close()# As usual we open the close.
    def checkDuplicate(self,ID,DT): # Will return false if said ID is in the DB twice, we allow a max of two duplicates. ( If we
        conn = sqlite3.connect('MainDB.db')
        cursor = conn.execute("SELECT FirstName,LastName,Sex,ID,YOB,TOV,DT,PhoneNO from Realtry") # Name of our Table
        occor = 1 # It is 1 since if there is no duplicate "occor" will equal 1. If there is one duplicate it will equal 2. If there is two duplicates it will equal three which will return false
        dupli = 1
        # Don't forget that we haven't inserted anything in the DB yet, we are checking nothing more.

        for row in cursor:
            if ID == row[3]:
                occor += 1
                dateandTime = row[6]
                if(dateandTime == DT ):
                    print()
                    return -1
                if(occor == 3):
                    #print("Duplicates more than 3 spotted")
                    return -5



        conn.close()#We clsoe after opening

        return 1 # 1 means true /accepted

    def printStatus(self,ID):
        conn = sqlite3.connect('MainDB.db')
        cursor = conn.execute("SELECT ID from Realtry")  # Name of our Table
        shots = 0
        for row in cursor:

            if (ID == row[0]):
                shots += 1
        return shots


# test = dataBase()
# test.printDB()
# test.insertInto("F","1","1","1","1","1","1","1")
# test.insertInto("F","1","1","1","1","1","1","1")
# print(test.printStatus("1"))
# test.printDB()

#print(test.checkDuplicate('self?',"1115030312"))
