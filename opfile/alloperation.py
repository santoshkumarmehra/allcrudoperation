from crud import checkregistration1
from core2 import checkregistration
from core1 import checkregistration3

def operation():
    while True:
        print("--Select database--"'\n'"1:MySQL Database\n2:SQlite3 Database\n3:Postgres Database\n4:Exit")
        x=input("Enter no = ")
        if x=='1':
            checkregistration1()
        elif x=='2':
            checkregistration()
        elif x=='3':
            checkregistration3()
        elif x=='4':
            return True
        else:
            print('\t',"--Select correctly--")

operation()
