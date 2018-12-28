import pymysql

def get_conn(db):
    return pymysql.connect(
        host='localhost',
        user='dooo',
        password='gusdnr75',
        port=3306,
        db=db,
        charset='utf8')

## dooodb에 접속

conn_dooodb = get_conn('dooodb')

with conn_dooodb:
    cur = conn_dooodb.cursor()
    cur.execute ("select id, name, tel, email, birthday, addr, regedt , gender, dept from Student")
    select = cur.fetchall()

print (select)


## HyunOuk에 접속
conn_HyunOuk = get_conn('HyunOuk')

row = 0

with conn_HyunOuk:
    cur = conn_HyunOuk.cursor()
    cur.execute ("drop table HyunOuk.Student")
    make_tb = "Create table HyunOuk.Student like dooodb.Student"
    cur.execute(make_tb)
    cur.execute("alter table HyunOuk.Student drop column subjects")
    insert_HO = ("insert into HyunOuk.Student (id, name, tel, email, birthday, addr, regedt , gender, dept) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    update = ("update HyunOuk.Student set name = '이현욱' where id = 1000")
    cur.executemany (insert_HO, select)
    print ("Row Count ======>>>>", cur.rowcount )
    conn_HyunOuk.commit()

    
