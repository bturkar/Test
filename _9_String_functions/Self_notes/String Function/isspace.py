"""**isspace() : returns true if all characters in the string are whitespaces***"""
str1 = "bhaskar turkar"
str2 = "bhaskar\tturkar"
str3 = "  "
str4 = "cdf"
print("------------- isspace() -----------------")
print('isspace() : returns true if all characters in the string are whitespaces')
print("bhaskar turkar is space   :", str1.isspace())
print("bhaskar\tturkar is space  :", str2.isspace())
print("' ' is space  :", str3.isspace())
print("cdf is space  :", str4.isspace())
print("-------------------------------------------------------------------------------------")
