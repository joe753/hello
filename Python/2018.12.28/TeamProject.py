import mig_util2 as mm


# -------------검증 1번-------------------
conn_dooodb = mm.get_mysql_conn('dooodb')
with conn_dooodb:
    dooo_cnt_emp = mm.get_count(conn_dooodb, 'Employee')
    dooo_cnt_dept = mm.get_count(conn_dooodb, 'Department')
    dooo_cnt_job = mm.get_count(conn_dooodb, 'Job')
    dooo_cnt_jobhis = mm.get_count(conn_dooodb, 'Job_history')

connection = mm.get_oracle_conn()
with connection:
    ora_cnt_emp = mm.get_count(connection, 'Employees')
    ora_cnt_dept = mm.get_count(connection, 'Departments')
    ora_cnt_job = mm.get_count(connection, 'Jobs')
    ora_cnt_jobhis = mm.get_count(connection, 'Job_history')

#--------------------------------검증 2번 함수화------------------------------------



ora_emp_column = 'employee_id, first_name, last_name, email, phone_number, hire_date, job_id, round(salary), round(commission_pct * 100), manager_id, department_id'
mys_emp_column = 'id, first_name, last_name, email, phone_number, hire_date, job_id, round(salary), round(commission_pct * 100), manager_id, department_id'

ora_dept_column = 'department_id, department_name, manager_id'
mys_dept_column = 'id, department_name, manager_id'       

ora_job_column = 'job_id, job_title, min_salary, max_salary'
mys_job_column = 'id, job_title, min_salary, max_salary'

ora_jobhis_column = 'employee_id, start_date, end_date, job_id, department_id'
mys_jobhis_column = 'employee_id, start_date, end_date, job_id, department_id'

counts = [(dooo_cnt_emp, ora_cnt_emp), (dooo_cnt_dept, ora_cnt_dept), (dooo_cnt_job, ora_cnt_job), (dooo_cnt_jobhis, ora_cnt_jobhis) ]
ora_column = [ora_emp_column, ora_dept_column, ora_job_column, ora_jobhis_column]
ora_table = ['Employees', 'Departments', 'Jobs', 'Job_history' ]
mys_column = [mys_emp_column, mys_dept_column, mys_job_column, mys_jobhis_column]
mys_table = ['Employee', 'Department', 'Job', 'Job_history' ]
mys_id = ['id', 'id', 'id', 'employee_id']

for k in range(0,4):
    if counts[k][0] != counts[k][1]:
        print("=================== ", mys_table[k], " Failed=======================")
        break
    else:
        print ("Mysql ==>> " , counts[k][0], "Oracle ==>> " , counts[k][1] )
        mm.valid (ora_column[k], ora_table[k] , mys_column[k], mys_table[k], mys_id[k] )


# if  dooo_cnt_emp != ora_cnt_emp:
#     print("========================Employee Failed==================================")
#     exit()
# else:
#     print("OK", "Dooo-->" , dooo_cnt_emp, "Oracle--->", ora_cnt_emp)
#     mm.valid (ora_emp_column, 'Employees' , mys_emp_column, 'Employee', 'id' )


# if dooo_cnt_dept != ora_cnt_dept:
#     print("========================Department Failed==================================")
#     exit()
# else:
#     print("OK", "Dooo-->" , dooo_cnt_dept, "Oracle--->", ora_cnt_dept)
#     mm.valid (ora_dept_column, 'Departments' , mys_dept_column, 'Department', 'id' )


# if dooo_cnt_job != ora_cnt_job:
#     print("========================Job Failed==================================")
#     exit()
# else:
#     print("OK", "Dooo-->" , dooo_cnt_job, "Oracle--->", ora_cnt_job)
#     mm.valid (ora_job_column, 'Jobs' , mys_job_column, 'Job' , 'id')


# if dooo_cnt_jobhis != ora_cnt_jobhis:
#     print("=======================Job_history Failed==================================")
#     exit()
# else:
#     print("OK", "Dooo-->" , dooo_cnt_jobhis, "Oracle--->", ora_cnt_jobhis)
#     mm.valid (ora_jobhis_column, 'Job_history' , mys_jobhis_column, 'Job_history', 'employee_id' )


# if dooo_cnt_job != ora_cnt_job:
#     print("========================Job Failed==================================")
#     exit()
# else:
#     print("OK", "Dooo-->" , dooo_cnt_job, "Oracle--->", ora_cnt_job)
#     connection = mm.get_oracle_conn()
#     with connection:
#         curs = connection.cursor()
#         rand = '''select * from (
#             select job_id, job_title, min_salary, max_salary from jobs order by DBMS_RANDOM.RANDOM)
#                 where rownum <= 5  '''
#         curs.execute(rand)
#         rand_oracle_job = curs.fetchall()
#         job_id = []
#         for i in range(0,5):
#             job_id.append(rand_oracle_job[i][0])



#     conn_dooodb = mm.get_mysql_conn('dooodb')
#     with conn_dooodb:
#         cur = conn_dooodb.cursor()
#         vr = '''select 
#                 id, job_title, min_salary, max_salary
#                 from Job where id = %s'''
#         vr_dooodb = []
#         for i in job_id:
#             (cur.execute(vr, i))
#             vr_dooodb.append(cur.fetchone())
            
#         if rand_oracle_job == list(vr_dooodb):
#             print("-Oo----------------------------------------------====OK")







# if dooo_cnt_jobhis != ora_cnt_jobhis:
#     print("========================Job_history Failed==================================")
#     exit()
# else:
#     print("OK", "Dooo-->" , dooo_cnt_jobhis, "Oracle--->", ora_cnt_jobhis)
#     connection = mm.get_oracle_conn()
#     with connection:
#         curs = connection.cursor()
#         rand = '''select * from (select 
#             employee_id, start_date, end_date, job_id, department_id from job_history order by DBMS_RANDOM.RANDOM)
#                 where rownum <= 5 '''
#         curs.execute(rand)
#         rand_oracle_jobhis = curs.fetchall()
#         jobhis_id = []
       
#         for i in range(0,5):
#             jobhis_id.append((rand_oracle_jobhis[i][0], rand_oracle_jobhis[i][3]))




#     conn_dooodb = mm.get_mysql_conn('dooodb')
#     with conn_dooodb:
#         cur = conn_dooodb.cursor()
#         vr = '''select 
#                 employee_id, start_date, end_date, job_id, department_id
#                 from Job_history where employee_id = %s and job_id = %s'''
#         vr_dooodb = []
#         for i in jobhis_id:
#             cur.execute(vr, (i[0],i[1]))
#             vr_dooodb.append(cur.fetchone())
            
#         if rand_oracle_jobhis == list(vr_dooodb):
#             print("oracle------> \n", rand_oracle_jobhis,"\n", "sql-------- \n", vr_dooodb)
#             print("-Oo----------------------------------------------====OK")










# # -------------------------검증 2번-------------------------------
# connection = mm.get_oracle_conn()
# with connection:
#     curs = connection.cursor()
#     rand = '''select * from (
#             select  employee_id, first_name, last_name, email, phone_number, hire_date, job_id, round(salary), round(commission_pct * 100), manager_id, department_id 
#             from Employees order by DBMS_RANDOM.RANDOM)
#             where rownum <= 5 '''
#     curs.execute(rand)
#     rand_oracle_employee = curs.fetchall()



# a = []
# for i in range(0,5):
#     a.append(rand_oracle_employee[i][0])



# conn_dooodb = mm.get_mysql_conn('dooodb')
# with conn_dooodb:
#     cur = conn_dooodb.cursor()
#     vr = '''select 
#               id, first_name, last_name, email, phone_number, hire_date, job_id, round(salary), round(commission_pct * 100), manager_id, department_id
#             from Employee where id = %s'''
#     vr_dooodb = []
#     for i in a:
#         (cur.execute(vr, i))
#         vr_dooodb.append(cur.fetchone())
        

# if rand_oracle_employee == list(vr_dooodb):
#     print("-Oo----------------------------------------------====OK")