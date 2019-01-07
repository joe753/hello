
import mig_util as mu

conn = get_oracle_conn('conn')

with conn:
   # cursor를 만들어줍니다
   cursor = connection.cursor()

   sql = '''select * from Departments where department_id = :dept_id'''

   #cursor.execute(sql, dept_id=30)
   cursor.execute(sql, (30,))

   rows = cursor.fetchall()

for row in rows:
   print(row)