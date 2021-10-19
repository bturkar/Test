"""*zfill(width) : Returns original string leftpadded with zeros to a total of width characters; intended for
numbers, zfill() retains any sign given (less one zero).**"""
print("------------- zfill() -----------------")
print('zfill() : adds 0 at start to make up the length')
s1 = 'hello world'
print("zfill of hello world is      :", s1.zfill(len(s1) + 2))
print("zfill(20) of hello world is  :", s1.zfill(20))
print("-------------------------------------------------------------------------------------")
