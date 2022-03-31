import pymysql
con=pymysql.connect(host="bna2xw5ovxf216tn5fqu-mysql.services.clever-cloud.com",database="bna2xw5ovxf216tn5fqu",user="ujbt5gcln4pajohe",password="k4ULcq5fHPUxRi1lFlL0")
curs=con.cursor()
curs.execute("select * from MOBILES")
data=curs.fetchall()
for rec in data:
    print(rec)
con.close()