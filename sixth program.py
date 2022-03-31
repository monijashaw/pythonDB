import pymysql
con=pymysql.connect(host='bna2xw5ovxf216tn5fqu-mysql.services.clever-cloud.com',user='ujbt5gcln4pajohe',password='k4ULcq5fHPUxRi1lFlL0',database='bna2xw5ovxf216tn5fqu')
curs=con.cursor()
curs.execute("select * from MOBILES where company='samsung'")
data=curs.fetchmany()
print(data)
data=curs.fetchmany()
print(data)