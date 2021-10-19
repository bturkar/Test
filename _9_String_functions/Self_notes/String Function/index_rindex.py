"""*******************index() : returns the index (within mentioned limits)
              else raises exception but find() will gives -1***************************"""
print("*************index()***********")

str1 = "bhaskar turkar"
print("index of s in str1 : ", str1.index('s'))
print("index of sk in str1 : ", str1.index("s", 2))
print("index of sk in str1,if present between index 2 & 14 : ", str1.index("s", 2, 14))
# print("index of b in str1,if present between index 3 & 14", str1.index("b", 3, 14)) #ERROR SUBSTRING NOT FOUND
# print("index of s in str1,if present after index 13", str1.index("s", 14)) #ERROR SUBSTRING NOT FOUND
# print("-------------------------------------------------------------------------------------")
print("*************rindex()***********")
"""rindex will start searching from RHS and gives index of first occurrence of str from left side"""
str1 = "bhaskar"
print("Will search a from LHS first occurrence is at from LHS:", str1.index('a'))
print("Will search a from RHS first occurrence is at from LHS:", str1.rindex('a'))
print(str1.index('ska'))
print(str1.rindex('ska'))
print("""for repeated character """)
str1 = "bhaskarska"
print(str1.index('ska'))
print(str1.rindex('ska'))