"""
if False -->  False
if None  -->  False
if 0     -->  False

if True    --> True
if not None -> True
if -5      -->  True
"""
val = True
print("boolean value ??", val, type(val))
val2 = "True"
print("type of 'True' ??", val2, type(val2))
x = 0
print(x, type(x))
x = bool(0)
print(x, type(x))

x = None
print(x, type(x))
x = False
print(x, type(x))
