import mig_util as mu

conn_dooodb = mu.get_mysql_conn('dooodb')
conn_dadb = mu.get_mysql_conn('dadb')
table = 'Subject'

# read from source db
with conn_dooodb:
    dooo_cnt = mu.get_count(conn_dooodb, table)

with conn_dadb:
    da_cnt = mu.get_count(conn_dadb, table)

print("dooodb =", dooo_cnt, ", dadb =", da_cnt)
if dooo_cnt == da_cnt:
    print("OK")

else:
    print("Not Valid Count!! dooodb =", dooo_cnt, ", dadb =", da_cnt)
