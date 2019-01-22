import csv
import codecs
import pymysql

fp = codecs.open("melon_add_likecnt.csv", "r", encoding="utf-8")
reader = csv.reader(fp, delimiter=',', quotechar='"')


def get_conn(db):
   return pymysql.connect(
       host='localhost',
       user='dooo',
       password='gusdnr75',
       port=3306,
       db=db,
       charset='utf8')

sql_truncate = "truncate table Meltop"
sql_insert = "insert into Meltop (rank, title, singer, likecnt) values (%s, %s, %s, %s) "
isStart = True

def save(lst):
    try:
        conn = get_conn('dooodb')
        conn.autocommit = False
        cur = conn.cursor()
        cur.executemany(sql_insert, lst)
        print("Affected RowCount is", cur.rowcount, "/", len(lst))
        conn.commit()

    except Exception as err:
        conn.rollback()
        print("Error!!", err)

    finally:
        try:
            cur.close()
        except:
            print("Error on close cursor")
        try:
            conn.close()
        except Exception as err2:
            print("Fail to connect!!", err2)



save(lst)



