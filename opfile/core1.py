import sqlite3
from create1 import Create
from read1 import Read
from update1 import Update
from delete1 import Delete

mydb = sqlite3.connect("psql1.db")

mycursor = mydb.cursor()

def checkregistration3():
    print('Available Options: C=Create, R=Read, U=Update, D=Delete E=Exit')
    choice = input('Choose your option = ').upper()
    if choice == 'C':
        t=Create()
        if t==True:
            print("\n","\t","--Please select options--")
            checkregistration3()
    elif choice == 'R':
        t=Read()
        if t==True:
            print("\n","\t","--Please select options--")
            checkregistration3()
    elif choice == 'U':
        t=Update()
        if t==True:
            print("\n","\t","--Please select options--")
            checkregistration3()
    elif choice == 'D':
        t=Delete()
        if t==True:
            print("\n","\t","--Please select options--")
            checkregistration3()
    elif choice == 'E':
        return True
    else:
        print('Wrong Entry')
        checkregistration3()

# checkregistration()      





