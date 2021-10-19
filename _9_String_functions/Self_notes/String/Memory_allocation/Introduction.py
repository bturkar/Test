"""string float(s1='1.2') value can not be converted to integer directly because of . so convert
    string float to float(float(s1)) and then to integer (int(float(s1))) """
str1 = "bhaskar"
str2 = "123"
str3 = "11.5"
print(type(str1), type(str2), type(str3))
print(int(str2)+100)
print(int(float(str3)+100))
print(float(str2)+500)
print(str1+str2)
print(type(int(str2)))
# print(type(int(str3)))   #ERROR
print(type(int(float(str3))))
print(type(float(str3)))