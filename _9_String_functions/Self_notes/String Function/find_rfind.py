"""find()"""
print('find() : Searches the string for a specified value and returns the starting position of where it was found')
str = 'hello world'
print('index of o gives first occurrence: ', str.find('o'))
print('index of o gives first occurrence between index 0 to 5: ', str.find('o', 0, 5))
print('index of o gives first occurrence beyond index 5: ', str.find('o', 5))
print('index of o gives first occurrence between 5 to 10: ', str.find('o', 5, 10))
print('-------------------------------------------------\n-----------\n-----------')
print('***********************rfind()******************************')

"""difference between find and rfind is that in find() search start from LHS and in rfind() search starts from RHS
but in both output index will be from LHS"""

"""rfind() : returns the index (within mentioned limits)  returns -1 if not found.
     searches from last i.e. from RHS and gives index from left side"""
str1 = "bhaskar turkar"
print("index of r from the last of str1 is                            :", str1.rfind("r"))
print("index of e from the right in between index 1 and 12 of str1 is :", str1.rfind("k", 1, 12))
print("index of e from the right in between index 1 and 12 of str1 is :", str1.rfind("k", 12))
print("index of e from the right in between index 1 and 12 of str1 is :", str1.rfind("k", 1))


print("-------------------------------------------------------------------------------------")



