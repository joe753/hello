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

    dooodb_count = "select count(*) from Subject"
    cur.execute(dooodb_count)
    dooo_count = cur.fetchall()
    
    dooodb_samp = "select id from Subject order by rand() limit 5"
    cur.execute(dooodb_samp)
    dooo_samp = cur.fetchall()
    print (dooo_samp[0])


conn_dadb = get_conn('dadb')


with conn_dadb:
    cur = conn_dadb.cursor()
    cur.execute('truncate table Subject')
    sql = "insert into Subject (id,name, prof, classroom) values (%s, %s, %s, %s)"
    dadb_count = "select count(*) from Subject"
    dadb_samp = "select * from Subject order by rand() limit 5"
    cur.executemany(sql, row)

    cur.execute(dadb_count)
    da_count = cur.fetchall()
    
    cur.execute(dadb_samp)
    da_samp = cur.fetchall()
    
    conn_dadb.commit()
    print("Rowcount ==>>>>", cur.rowcount , "---------", dooo_count, da_count)




