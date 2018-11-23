import sqlite3
import random

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")

results = []
for full_name in range (0,100):
    sung = random.choice(fam_names)
    for i in range(1):
        a = random.choice(first_names)
        b = random.choice(first_names)
        lsts = (sung + a + b,)
        results.append(lsts)

datum = tuple(results)

conn = sqlite3.connect('test.db')

data = (datum)


with conn:
    cur = conn.cursor()
    sql = "insert into Student(name) values (?)"
    cur.executemany(sql, data)

    conn.commit()

print (results)