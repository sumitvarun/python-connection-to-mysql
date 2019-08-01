import mysql.connector
import time

#create class, for connecting mysql to python
class office:
    mydb= mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="db2"
    )
    mycursor=mydb.cursor()
    def dept(self):
        print("connecting the server please")
        for i in range(5):
            print(".",end="")
            time.sleep(0.50)#time sleep for pause the task for given time.
            print()
            print("server is connected")
            #query section, for inserting query into database
            query="insert into employee(cus_id,cus_firstname,cus_lastname,cus_age,cus_mobile,cus_salary)value(%s, %s, %s, %s, %s, %s)"
            id= int(input("/n/n cus id"))
            firstname= input("cus firstname")
            lastname= input("cus lastname")
            age= int(input("cus age"))
            mobile= int(input("cus mobile"))
            salary= int(input("cus salary"))
            val=(id,firstname,lastname,age,mobile,salary)
            self.mycursor.execute(query,val)
            self.mydb.commit()
            print("query saved sucessfully")
            print("do you want continue:")
            choice=int(input("enter your choice"))
            if(choice==1):#conditons,choice selection
                self.dept()
            elif(choice==2):
                print("thanks for using")
            else:
                print("you enter wrong option")
            
off=office()
off.dept()
