import pymysql
con=pymysql.connect(host='bna2xw5ovxf216tn5fqu-mysql.services.clever-cloud.com',user='ujbt5gcln4pajohe',password='k4ULcq5fHPUxRi1lFlL0',database='bna2xw5ovxf216tn5fqu')
curs=con.cursor()
prid=int(input("Enter your productid: "))
curs.execute("select * from MOBILES where prodid=%d"%prid)
data=curs.fetchone()
if data:
    pric=int(input("enter the New price of mobile: "))
    curs.execute("update MOBILES set price=%d where prodid=%d"%(pric,prid))
    con.commit()
    print("Mobile data updated successfully")
else:
    print("mobile does not exist")
con.close() 





