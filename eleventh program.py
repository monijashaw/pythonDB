import pymysql
con=pymysql.connect(host='bna2xw5ovxf216tn5fqu-mysql.services.clever-cloud.com',user='ujbt5gcln4pajohe',password='k4ULcq5fHPUxRi1lFlL0',database='bna2xw5ovxf216tn5fqu')
curs=con.cursor()
modelname=input("Enter your modelname: ")
curs.execute("select * from MOBILES where modelname='%s'"%modelname)
data=curs.fetchone()
if data:
    pur=input("enter the purpose of buying the  mobile: ")
    curs.execute("update MOBILES set purpose='%s' where modelname='%s'"%(pur,modelname))
    con.commit()
    print("Mobile data updated successfully")
else:
    print("mobile does not exist")
con.close() 



