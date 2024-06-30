import pymysql as mysql
def ConnectionPool():
    db=mysql.connect(host="localhost",port=3306,user="root",password="merasql",db="motokart")
    cmd=db.cursor()
    return (db,cmd)
