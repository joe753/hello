

class Student:
    def __init__(self, line):
        name, gender, age, score, address = line.strip().split(',')
        self.name = name
        self.gender = gender
        self.age = age
        self.score = int(score)
        self.address = address
    
    def pri_age (self):
        for i in self.age:
            self.pri_age = self.age[0] + '0대'    

    def make_grades(self):    
        if self.score >= 90:
            self.grade = 'A'
        elif self.score >= 80:
            self.grade = 'B'
        elif self.score >= 70:
            self.grade = 'C'
        elif self.score >= 60:
            self.grade = 'D'
        else : 
            self.grade = 'F'

    def pri_address(self):
        lst_address = list(self.address.split(' '))
        self.pri_address = lst_address[-3] +' ' + lst_address[-2]
     

    def to_english_gender (self):
        if self.gender == '남':
            self.gender  = 'M'
        elif self.gender == '여':
            self.gender = 'F'
   
    def __str__(self):
        self.pri_age()
        self.make_grades()
        self.to_english_gender()
        self.pri_address()      
        return "{}**\t{}\t{}\t{}\t{}".format(self.name[0], self.gender, self.pri_age, self.grade, self.pri_address)

    

    
       

students = []   

with open('students.csv', 'r', encoding='utf8') as file:
    for i, line in enumerate(file):
        if i == 0: continue
        students.append(Student(line))


