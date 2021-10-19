"""Sequence operation"""
name = 'bhaskar turkar'
for i in name:
    print(i, end=' ')
print(' ')
print('-------------------------------')
for i in name[::]:
    print(i, end=' ')
print(' ')
print('-------------------------------')
for i in name[::-1]:
    print(i, end=' ')
print(' ')
print('-------------------------------')
"""************indexing****************"""
name = 'Hello World'
print('name[1]     :', name[1])
print('name[1:]    :', name[1:])
print('name[1::]   :', name[1::])
print('name[1::-1] :', name[1::-1])
print(' ')
print('-------------------------------')
"""************addition****************"""

s1 = 'Bhaskar'
s2 = 'Turkar'
print('addition', s1 + s2)
print(' ')
print('-------------------------------')
"""************multiplication****************"""

print('Multiplication', s1 * 7)
print('-------------------------------')
"""*************membership***************"""
name = 'Bhaskar'
print("'B' in name     :", 'B' in name)
print("'b' in name     :", 'b' in name)
print("'r' in name     :", 'r' in name)
print("'R' not in name :", 'R' not in name)
print("'Bha' in name   :", 'Bha' in name)
print("'Bha' not in name :", 'Bha' not in name)
print("'a' in Bhaskar   :", 'a' in 'Bhaskar')
print("'BHA' not in 'Bhaskar :", 'BHA' not in 'Bhaskar')

print('-------------------------------')
"""*************len()***************"""
name = 'bhaskar'
print(len(name))
print(len('bhaskar'))
print('-------------------------------')
"""*************max():depend on ASCII code***************"""
name = 'bhaskar'
print(max(name))
print(max('bhaskar'))
print(max('Bhaskar'))
print('-------------------------------')
"""*************min():depend on ASCII code***************"""
name = 'bhaskar'
print(min(name))
print(min('bhaskar'))
print(min('Bhaskar'))
print('-------------------------------')
