def write_file():
    with open("a.csv", "w", encoding='utf8') as file:
        file.write("이름,성별,나이\n")
        file.write("이현욱,남,26\n")
        file.write("이현민,남,28\n")

def read_file():
        with open("a.csv", "r") as file:
            for line in file:
                print (line)
write_file()
read_file()