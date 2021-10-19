"""increment or decrement will be according to value if it is positive then LHS to RHS and if it is Negative then
RHS to LHS """
name = "Bhaskar Turkar"
print(name[0])
print(name[-1])
print(name[2])
# print(name[15]) IndexError: string index out of range
print(name[0:14:])
print("name[10] :", name[10])
print('name[0:14:10] :', name[0:14:10])
print('name[::-1] :', name[::-1])
print('name[-10:-14:-1] :', name[-10:-14:-1])
print('name[-10:-14:] :', name[-10:-14:])  #
print('name[10:14:-1] :', name[10:14:-1])
"""memory  allocation"""
x = 10
print("Value of x: ", x, id(x))
x = 20
print("Value of x: ", x, id(x))

msg = 'Hello World'
print("Message1 is : ", msg, id(msg))

msg = 'Python'
print("Message1 is : ", msg, id(msg))

x = 10
print(x, id(x))

x = x + 20
print(x, id(x))
msg = 'hello'
print('Mes : ', msg)
msg = msg + 'world'
print('Message2 : ', msg)

x = 'Hello World'
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x[-1] in x:
    print(x[-1])
