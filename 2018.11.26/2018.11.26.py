import re
line = "Beautiful is better than ugly."
matches = re.findall("Beautiful", line)
# print(matches)


matches2 = re.findall("beautiful", line, re.IGNORECASE)
# print(matches2)


zen2 = """Although never is often better than * right * now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea - - let's do more of those!"""

m = re.findall("^If", zen2, re.MULTILINE,)
m2 = re.findall("idea\.", zen2, re.MULTILINE)
m22 = re.findall("idea.*", zen2, re.MULTILINE)
m3 = re.findall("idea.$", zen2, re.MULTILINE)
print(m, m2, m22, m3)


import re

string = "Two aa too"

# m = re.findall("t[ow]o", string)
m = re.findall("t[ow]o", string, re.IGNORECASE)
# print(m)


m = re.findall("t[^w]o", string, re.IGNORECASE)
# print(m)

import re

string = "123?45yy7890 hi 999 heLLo"

m1 = re.findall("[A-z]", string)
m2 = re.findall("[0-9]{1,3}", string)
m3 = re.findall("[1-5]{1,4}", string)

print("m1=", m1)
# print("m2=", m2)
# print("m3=", m3)


