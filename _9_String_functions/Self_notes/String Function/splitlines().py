"""**********splitlines() : splits at line breaks & returns lists*************"""
s1 = "hello world"
s2 = "name \n address\n age \n salary"
print("------------- splitlines() -----------------")
print('splitlines() : splits at line breaks & returns lists ')
print("Original String:", s1)
print("Splitting lines for the original string is:", s1.splitlines())
print("-----------------------------------------------")
print("Original String                             :", s2)
print("Splitting lines (splitlines(True))for the original string is  :", s2.splitlines(True))
print("Splitting lines (splitlines(False)) for the original string is  :", s2.splitlines(False))
print("Splitting lines for the original string is  :", s2.splitlines(2))
print("Splitting lines for the original string is  :", s2.splitlines(0))
print("Splitting lines for the original string is  :", s2.splitlines(3))
print("-------------------------------------------------------------------------------------")
