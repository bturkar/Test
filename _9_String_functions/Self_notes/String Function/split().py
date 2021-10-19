"""*******split() : separates with spaces into lists***********"""
s1 = "hello  world"
s2 = "bhaskar "
print("-------------split() -----------------")
print('split() : separates with spaces into lists ')
print("Original String:", s1)
print("Splitting hello world:", s1.split())
print("-----------------------------------------------")
print("Original String                    :", s2)
print("Splitting  bhaskar  :", s2.split("a"))
print("Splitting  bhaskar  :", s2.split("a",1))
print("Splitting  bhaskar  :", s2.split("a",3))
print("-------------------------------------------------------------------------------------")
