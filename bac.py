abc = list('abcdefghijklmnopqrstuvwxyz')
print(abc)
i = 0
while i < len(abc):
    abc[i] = '*'
    i = i + 3
print(abc)
abcd = ''
i = 0
while i < len(abc):
    abcd = abcd + abc[i]
    i = i + 1
print(abcd)
abc = abcd.split('*')
print(abc)
i = 0
abcd = ''
while i < len(abc):
    abcd = abcd + abc[i]
    i = i + 1
print(abcd)
abc = list(abcd)
print(abc)



