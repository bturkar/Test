"""****replace(old, new [max]) : replace with given char****"""
s1 = "Hello Bhaskar"
print('-------------replace() -----------------')
print('replace() : replace with given char')
print("Replace a with @ in 'Hello Bhaskar' only once          :", s1.replace("a", "@", 1))
print("Replace all a's with @ in hello bhaskar              :", s1.replace("a", "@"))
print("Replace all a's with @ and r with & in Hello Bhaskar :", (s1.replace("a", "@")).replace("r", "&"))
print("replace ' ' by 'Q' ",s1.replace(' ',' Q'))
print("replace ' ' by 'Q' ",s1.replace('',' Q'))
print("if element to be replaced is not found then no effect")
print("replace ' ' by 'Q' ",s1.replace('  ',' Q'))  # no effect as no three white space are available


print("-------------------------------------------------------------------------------------")
