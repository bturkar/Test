li = []
print(type(li))
print(li)
li = [1, 'fg', '*']
print(li)
li = [[], [1, 8, 6], (1,)]
print(li)
li = [[], (1, 5), {1, 1, 2}, {'a': 7, 'b': 9}]
print(li)
'''***********************************************'''
# TUPLE
tup = ()
print(type(tup))
print()
print(tup)
tup = (1, 'fg', '*')
print(li)
tup = ([], [1, 8, 6], (1,))
print(tup)
tup = [[100, 200], [], (1, 5), {1, 1, 2}, {'a': 7, 'b': 9}, ()]
print(tup[0], 'before update')
tup[0][0] = 'added element in list'
print(tup[0], 'after update')
print(tup[1], 'before update')
tup[1].append('Added element in empty list')
print(tup[1], 'after update')

print(tup[2],'before update')
#tup[2]=tup[2]+(1,5,6)  #ERROR
tup[2]=(1,5,6)     #ERROR
print(tup[2],'after update')
print(tup[3],'before update')
#tup[3][0]='added element in SET'
print(type(tup[3])
#tup[3].add('Deed element in set')='added element in SET'
#print(tup[3],'after update')
