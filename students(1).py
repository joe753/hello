class Student:
    def __init__(self, name, gender, age, score):
        self.name = name
        self.gender = gender
        self.age = age
        self.score = score
        if score > 90:
            self.grade = 'A'
        elif score > 80:
            self.grade = 'B'
        elif score > 70 :
            self.grade = 'C'
        elif score > 60 :
            self.grade = 'D'
        else : 
            self.grade = 'F'   

    def __str__(self):
        pri_name = self.name[0] + '**'
        return "{} / {} / {} / {}".format(pri_name, self.gender, self.age, self.grade)

students = [Student("이현욱", "남", 26, 88),
    Student("김현수", "남", 25, 94),
    Student("최민지", "여", 27, 53),
    Student("김현진", "여", 29, 64),
    Student("정인수", "남", 21, 77),
    Student("허은지", "여", 31, 84),
    Student("하해리", "여", 25, 42),
    Student("이지현", "여", 24, 59),
    Student("손흥민", "남", 27, 92)]
        

def print_students():
    print ("----------------------")
    for s in students:
        print(s)

students = sorted(students, key = lambda stu: stu.score)
print_students()

sum = 0
for s in students:
    sum += s.score   
print("\n{}".format(sum))

aver = sum / len(students)
print ("{}\n".format(aver))

for s in students:
    if s.score > aver:
        print ("{}, {}".format(s.name, s.score))