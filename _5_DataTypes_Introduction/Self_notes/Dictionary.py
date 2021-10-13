d = {}
print(type(d))
d= dict()
print(type(d))
#d = dict{'a'} #ERROR
#d = dict{'a':1} #error
d = {'a':1,1:5}
#d = {'a':1,1:5,():'emptyy tup',{}:'empty set'} #key should be number,str or tup value can be anything

print(d)