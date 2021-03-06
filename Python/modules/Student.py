g_grades = ['A', 'B', 'C', 'D', 'F']
g_grades.reverse()


class Student:
    grade = ''
    def __init__(self, line):
        name, gender, age, score = line.strip().split(',')
        self.name = name
        self.gender = gender
        self.age = age
        self.score = int(score)
    
    def __str__(self):
        return "{}**\t{}\t{}\t{}".format(self.name[0], self.gender, self.age, self.grade)

    def make_grade(self):
        if self.score < 50 :
            self.grade = 'F'
        else: 
            self.grade = g_grades[ self.score // 10 - 5 ]

