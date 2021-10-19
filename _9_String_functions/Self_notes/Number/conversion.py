"""
Type conversions
-----------------
int()
float()
complex()
bool()
--------
str()
list()
tuple()
dict()
set()
"""
# Boolean
# True nonZero non None
# False 0 None
x = 0
print("Normal val : ", x, type(x))
x = bool(0)
print("Boolean val : ", x, type(x))

y = 1
print("Normal val : ", y, type(y))
x = bool(y)
print("Boolean val : ", x, type(x))
