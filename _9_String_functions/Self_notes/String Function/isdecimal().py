"""**isdecimal() : returns true if all characters in the string are numeric****"""
s1 = "23081994"
s2 = u"16041991"
s3 = "Aug231994"
s4 = "-259.6"
s5 = "%"
s6 = u"-259.6"
print("------------- isdecimal() -----------------")
print('isdecimal() : returns true if all characters in the string are numeric')
print("23081994 is decimal   :", s1.isdecimal())
print("u16041991 is decimal  :", s2.isdecimal())
print("Aug231994 is decimal  :", s3.isdecimal())
print("-259.6 is decimal     :", s4.isdecimal())
print("% is decimal     :", s5.isdecimal())
print("u'-259.6' is decimal     :", s6.isdecimal())


print("-------------------------------------------------------------------------------------")
