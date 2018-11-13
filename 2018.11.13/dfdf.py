def write_file():
    with open("sd.csv", "w", encoding='utf8') as file:
        file.write("이름,성별,나이\n")
        file.write("이현욱,남,26\n")
        file.write("이현민,남,28\n")

write_file()