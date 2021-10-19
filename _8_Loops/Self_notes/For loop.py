"""for for string"""
name = "Bhaskar"
for i in name:
    print(i, sep=" ")
for i in name:
    print(i, end="")
print('')
"""for on list"""
li = [1, 2, 3, "bhaskar"]
for i in li:
    print(i)
li = [[1, 2, 3, [7, 9], (9, 6)], {'a': 'f', 'b': 'k'}, 3, {"bhaskar", 'hi', 'bye'}]
print('')
li_updated = []
for i in li:
    li_updated.append(i)
print(li_updated)

"""for on tuple"""
tup = (1, 2, 3, ["bhaskar", "Turk"], {5, 8, 3, 'u'})
for i in tup:
    print(i)
"""Dictionary"""
# d={'name':'bhaskar', 'age':27,'mob':99600264562, 21:25, 'add': 'nagpur', {'a':1, 'b':2}:'dict inside dic'} #error dic
d = {'name': 'bhaskar', 'age': 27, 'mob': 99600264562, 21: 25, 'add': 'nagpur'}

for k in d.keys():
    print(k)
for v in d.values():
    print(v)
for kv in d.items():
    print(kv)
"""set"""
s = {1, 5, 6, 2, 3, 5, 8}
for i in s:
    print(i)
print('number between 1 to 100 divisible by 7')
for i in range(1, 101):
    if i % 7 == 0:
        print(i, end=' ')
print(' ')
print('lowest 5 number between 1 to 100 divisible by 7')
count = 0
for i in range(1, 101):
    if i % 7 == 0:
        print(i, end=' ')
        count += 1
    if count == 5:
        break
print(' ')
print('lowest 5 number between 1 to 100 divisible by 7 displaced count')
count = 0
for i in range(1, 101):
    if i % 7 == 0:
        print(i, end=' ')
        count += 1
        if count == 5:
            break
print(' ')
print('lowest 5 number between 1 to 100 divisible by 7 continue****************************ex5')
count = 0
for i in range(1, 101):
    if count == 5:
        continue
    if i % 7 == 0:
        print(i, end=' ')
        count += 1
print(' ')
print('lowest 5 number between 1 to 100 divisible by 7 continue****************************ex6')
count = 0
for i in range(1, 101):
    if count == 5:
        break
    if i % 7 == 0:
        print(i, end=' ')
        count += 1
print(' ')
print('lowest 5 number between 1 to 100 divisible by 7 continue****************************ex7')
count = 0
for i in range(1, 101):
    if count == 5:
        pass
    if i % 7 == 0:
        print(i, end=' ')
        count += 1
print(' ')
print('lowest 5 number between 1 to 100 divisible by 7 continue****************************ex8')

print(' ')
print('lowest 5 number between 1 to 100 divisible by 7')
count = 0
for i in range(1, 101):
    if i % 7 == 0:
        print(i, end=' ')
        count += 1
    if count == 5:
        break
print(' ')
print('lowest 5 number between 1 to 100 divisible by 7 continue****************************ex9')
count = 0
for i in range(1, 101):
    if i % 7 == 0:
        print(i, end=' ')
        count += 1
    if count == 5:
        pass

print(' ')
print('lowest 5 number between 1 to 100 divisible by 7 continue****************************ex10')
count = 0
for i in range(1, 101):
    if i % 7 == 0:
        print(i, end=' ')
        count += 1
    if count == 5:
        continue
print("*******************************")
for i in range(0, 4):
    for j in range(0, 4 - i):
        print(4 - j, end=" ")
    print('')
print("*******************************")
for i in range(0, 4):
    for j in range(0, 4-i):
        print(4-j-i, end=" ")
    print('')
"""******************************************"""
l=[1,2,3,5]
l.reverse()
print(l)