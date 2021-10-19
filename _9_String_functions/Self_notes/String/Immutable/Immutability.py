"""immutable : string, number(int,float), boolean(T/F), tuple """
"""mutable : list, set, dict"""
x = 10
print("First  :", x, id(x))
x = 20
print("Second :", x, id(x))

x = 10
print(x)
x = x + 10
print(x, id(x))

msg = 'Hello'
print("Message : ", msg)
msg = 'World'
print("Message : ", msg)

msg = 'Hello'
print("Message : ", msg)
msg = msg + 'World'
print("Message : ", msg)
