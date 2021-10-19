"""******strip() : Performs both lstrip() and rstrip() on string********"""
s1 = "    hello world  "
s2 = "***bhaskar turkar************"
s3="bhaskar"
print("------------- strip() -----------------")
print('strip() : Performs both lstrip() and rstrip() on string')
print("strip of " " hello world          :", s1.strip(" "))
print("strip of * in ***Wow! what a ***bhaskar turkar************    :", s2.strip("*"))
print("strip of bhaskar                                              :",s3.strip())
print("-------------------------------------------------------------------------------------")
