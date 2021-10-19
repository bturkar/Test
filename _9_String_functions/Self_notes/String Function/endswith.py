"""***************endswith()***********************"""
str1 = 'Bhaskar Turkar'
print("-------- endswith() -----------")
print('endswith() : returns true if end with mentioned suffix.')

print("original  string                        :", str1)

print("If the Normal String ends with ar or not:", str1.endswith("ar"))
print("If the Normal String ends with r or not :", str1.endswith("r", 2, 8))
print("If the Normal String ends with gor not  :", str1.endswith("g", 3, 12))
print("If the Normal String ends with r or not :", str1.endswith("r", 2))
print("If the Normal String ends with r or not :", str1.endswith("r"))
print("-------------------------------------------------------------------------------------")
