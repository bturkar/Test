print("****** encode() ******")
print('decode() : Decodes the string using the codec registered for encoding..')
s = 'bhaskar turkar'
print("decoded string        :", s)
print("encoded string        :", s.encode())
print("encoded string        :", s.encode('UTF-8'))
# print("encoded string        :", s.encode('strict'))   ERROR

print("encoded string        :", s.encode('UTF-8', 'strict'))
print("-------------------------------------------------------------------------------------")

print("******decode() ***********")
s = 'bhaskar turkar'
s1 = s.encode()
print('decode() : Returns the encoded version of the string.')
print("encoded string        :", s1)
print("decoded string        :", s1.decode())
print("decoded string        :", s1.decode('UTF-8'))
# print("decoded string        :", s1.decode('strict'))   ERROR

print("decoded string        :", s1.decode('UTF-8', 'strict'))
print("-------------------------------------------------------------------------------------")
