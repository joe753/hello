import pymysql

def get_conn(db):
    return pymysql.connect(
        host='localhost',
        user='dooo',
        password='gusdnr75',
        port=3306,
        db=db,
        charset='utf8')


conn_dooodb = get_conn('dooodb')

row = 0

with conn_dooodb:
    cur = conn_dooodb.cursor()
    sql = "select id, name, prof, classroom from Subject"
    cur.execute(sql)
    row = cur.fetchall()
    

print (row)

conn_dadb = get_conn('dadb')


with conn_dadb:
    cur = conn_dadb.cursor()
    cur.execute('truncate table Subject')
    sql = "insert into Subject (id,name, prof, classroom) values (%s, %s, %s, %s)"
    cur.executemany(sql, row)
    print("Rowcount ==>>>>", cur.rowcount )
    conn_dadb.commit()