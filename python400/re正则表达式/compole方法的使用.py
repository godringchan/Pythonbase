import re

s = r"first123456line"
relex = re.compile(r"\D+")
o = relex.match(s)
o2 = relex.search(s)

print(o)
print(o2)
