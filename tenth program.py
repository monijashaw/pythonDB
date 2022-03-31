import pymysql
con=pymysql.connect(host='bna2xw5ovxf216tn5fqu-mysql.services.clever-cloud.com',user='ujbt5gcln4pajohe',password='k4ULcq5fHPUxRi1lFlL0',database='bna2xw5ovxf216tn5fqu')
curs=con.cursor()
curs.execute("alter table MOBILES add purpose varchar(50)")
print("table altered successfully")
con.close()
