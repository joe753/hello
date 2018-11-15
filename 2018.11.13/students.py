class Students:
    def __init__(self, name, gender, age, score):
        self.name = name
        self.gender = gender
        self.age = age
        self.score = score

    def __str__(self):
        return "{} / {} / {} / {}".format(self.name, self.gender, self.age, self.score)



def write_file():
    with open ("students.csv", "w", encoding = 'utf8') as file:
        file.write ("이름, 성별, 나이, 성적\n")
        file.write ("이현욱, 남, 26, 95\n")
        file.write ("김현수, 남, 25, 43\n")
        file.write ("최민지, 여, 27, 66\n")
        file.write ("김현진, 여, 29, 77\n")
        file.write ("정인수, 남, 21, 84\n")
        file.write ("허은지, 여, 31, 32\n")
        file.write ("하해리, 여, 25, 46\n")
        file.write ("이지현, 여, 24, 79\n")
        file.write ("손흥민, 남, 27, 99\n")
    
write_file()


# stu_score = list(write_file())  
# print (stu_score)
# def print_students():
#     print ("----------------------")
#     for s in stu_score:
#         print(s)

# stu_score = sorted(stu_score, key = lambda stu: stu.score)
# write_file()


