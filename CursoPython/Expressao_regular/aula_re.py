import re

string = 'Este é um teste de expressao teste regulares'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'ABC', string))

regular = re.compile(r'teste')
print(regular.search(string))
print(regular.findall(string))
print(regular.sub('CDE', string))
