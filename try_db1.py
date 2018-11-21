
import random

fam_names = list("김")
first_names = list("성현정민현희진영래주혜도영진선재현호시우인성마무별솔온하라")


def make_name():
    sung = random.choice(fam_names)
    name = "".join(random.sample(first_names, 2))
    return (sung + name,) 


data = []
for i in range (0,100):
    data.append(make_name())

print (data)