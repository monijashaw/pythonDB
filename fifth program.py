from sqlite3 import DatabaseError
import pymysql
con=pymysql.connect(host="bna2xw5ovxf216tn5fqu-mysql.services.clever-cloud.com",database="bna2xw5ovxf216tn5fqu",user="ujbt5gcln4pajohe",password="k4ULcq5fHPUxRi1lFlL0")
curs=con.cursor()
mnm=input("Enter the modelname: ")
curs.execute("select * from MOBILES where modelname='%s'"%mnm)
data=curs.fetchone()
if data:
   print(data)
else:
    print("not found")   
con.close()
