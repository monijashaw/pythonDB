import pymysql
con=pymysql.connect(host='bna2xw5ovxf216tn5fqu-mysql.services.clever-cloud.com',user='ujbt5gcln4pajohe',password='k4ULcq5fHPUxRi1lFlL0',database='bna2xw5ovxf216tn5fqu')
curs=con.cursor()
a=int(input("Enter product id: "))
curs.execute("select * from MOBILES where prodid=%d"%a)
data=curs.fetchone()
if data:
    print(data)
else:
    print("product id does not exist in tables")
i='yes'
while i.upper()=='YES':
    b=int(input("Enter product id that you want to delete from table: "))
    curs.execute("delete from MOBILES where prodid=%d"%b)
    print("data deleted successfully")
    i=input("Do you want to delete(yes/no): ")

