import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     database='bank',
                                     user='root',
                                     password='Pranav@19')
if connection.is_connected():
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)
a2=connection.cursor()
a=input("acc_no")
b=input("branch")
c=int(input("balance"))
query1="insert into account(account_number,branch_name,balance)values(%s,%s,%s)"    
query2=(a,b,c)
a2=connection.cursor()
a2.execute(query1,query2)
query="select * from account"
a1=connection.cursor()
a1.execute(query)
r=a1.fetchall()

for row in r:
    print("account_no=",row[0])
    print("branch name",row[1])
    print("balance",row[2])
connection.commit()
