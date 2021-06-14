import cx_Oracle
con=cx_Oracle.connect('SYSTEM/oracle@orcl')
print("connected",con.version)
cur=con.cursor()
cur.execute("drop table db3")
cur.execute("create table db3(cname varchar(20),fname varchar(20),addr varchar(20),qua number,amo number)")
class food:
    def __init__(self,c_name=None,f_name=None,c_address=None,quantity=None,amount=None):
        self.c_name=c_name
        self.f_name=f_name
        self.c_address=c_address
        self.quantity=quantity
        self.amount=amount
    def getc_name(self):
        return self.c_name
    def getf_name(self):
        return self.f_name
    def getc_address(self):
        return self.c_address
    def getquantity(self):
        return self.quantity
cur.execute("""create or replace procedure insert1(
c IN varchar,f IN varchar,address IN varchar,qual IN number,amount IN number
)
IS
BEGIN
insert into db3 values(c,f,address,qual,amount);
commit;
END;""")
price=0
a=food(eval(input("enter cus name")),eval(input("enter food name")),eval(input("enter the address")),int(input("enter the quantity")))
#b=food_order(input("enter cus name"),input("enter food name"),input("enter the address"),int(input("enter the quantity")))
for food in [a]:
    li1=[(food.getc_name(),food.getf_name(),food.getc_address(),food.getquantity())]
    print(li1)
    cus=li1[0][0]
    food1=li1[0][1]
    add1=li1[0][2]
    qua=li1[0][3]
    if (food1=="salad"):
        price=100*qua
    elif (food1=="rice"):
        price=150*qua
    elif (food1=="spaghetti"):
        price=200*qua
    elif (food1=="hamburger"):
        price=200*qua
    elif (food1=="pizza"):
        price=500*qua
    print(price)
    cur.callproc('insert1',[cus,food1,add1,qua,price])
cur.execute("select * from db3")
for i in cur.fetchall():
    print(i)
con.commit()
con.close()
