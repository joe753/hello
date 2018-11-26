import re

string = "aaaaaaa<hr>This"

pattern = re.compile("<.*>")         #cf. re.compile("<.*>")

mm = re.findall(pattern, string)
print (mm)