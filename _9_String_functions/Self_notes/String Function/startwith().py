"""***************startswith()***********************"""
s1 = 'Bhaskar Turkar'
print("-------- startswith() -----------")
print('startswith() : returns true if end with mentioned suffix.')

print("original  string                        :", s1)
print("If the Normal String ends with ar or not:", s1.startswith("B"))
print("If the Normal String ends with ar or not:", s1.startswith("b"))
print("If the Normal String ends with ar or not:", s1.startswith("b",0,3))
print("If the Normal String ends with r or not :", s1.startswith("r", 6, 8))
print("If the Normal String ends with gor not  :", s1.startswith("ska", 3, 12))
print("If the Normal String ends with r or not :", s1.startswith("a", 2))
print("If the Normal String ends with r or not :", s1.startswith("r"))
print("-------------------------------------------------------------------------------------")
