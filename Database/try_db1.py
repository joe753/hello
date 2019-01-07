import pymysql
import random


fam_names = list("김이박현하오우장정연마피고강구임허")
first_names = list("성현정민현희진영래주혜도영진선재현호시우인성마무별솔온하라")


def make_name():
    sung = random.choice(fam_names)
    name = "".join(random.sample(first_names, 2))
    return (sung + name) 

# def make_addr():


data = []
for i in range (0,100):
    data.append(make_name())

numbers = list('0123456789' * 4)
def make_number():
    num = "".join(random.sample(numbers, 4))
    return (num)

make_number()
def res_number ():
    return ("010-" + "{}-{}".format(make_number(),make_number()))



def make_email():
    mail = ('naver.com','google.com','daum.net','yahoo.co.kr')
    alphabet = ('abcdefghijklmnopqrstuvwxyz0123456789' * 6 )
    email = "".join(random.sample(alphabet, random.randrange(7,11)))
    return ("{}@{}".format(email,random.choice(mail)))



def year():
    thousand = random.randrange(1,3)
    hundred = random.randrange(10)
    ten = random.randrange(10)
    one = random.randrange(10)
    if thousand == 1:
        hundred = 9

    elif thousand == 2 : 
        hundred = 0
        ten = random.randrange(2)
        one = random.randrange(10)
    a = ("{}{}{}{}".format(thousand,hundred,ten,one))
    return (a)

def month_day():
    month_1 = random.randrange(1,13)
    
    
    if month_1 == 2:
        day = random.randrange(1,29)
    elif month_1 < 8 and month_1 % 2 == 0:
        day = random.randrange(1,31)
    elif month_1 > 8 and month_1 % 2 == 1:
        day = random.randrange(1,31)
    elif month_1 < 8 and month_1 % 2 == 1:
        day = random.randrange(1,32)
    else :
        day = random.randrange(1,32)

    if len(str(month_1)) == 1:
        month_1 = '{}{}'.format(0,month_1)
    if len(str(day)) == 1:
        day = '{}{}'.format(0,day)

    return ("{}{}".format(month_1,day))

def birthday():
    return ("{}{}".format(year(),month_day()))


def addr():
    si = ('서울','강원','전북','경기','경남','제주','충북')
    return random.choice(si)

data = []

for i in range (100):
    data.append((make_name(), res_number(), make_email(), birthday(), addr())) 





conn = pymysql.connect(host='localhost', user='dooo', password='gusdnr75', port=3306, db='dooodb', charset='utf8')

with conn:
    cur = conn.cursor()
    sql = "insert into New_Student(name, tel, email, birthday, addr) values (%s,%s,%s,%s,%s) "
    cur.executemany (sql, data)
    conn.commit()

    




 

