import re
'''
"*"重复0次或多次
"+"1次或多次
"?"0次或者1次
"{m}"重复m次
"{m, n}"重复m到n次
"{m, }"重复最少m次

'''
s = "12345678+9"
p = "\d*"

o = re.match(p, s)
print(o.group())
print(o)
