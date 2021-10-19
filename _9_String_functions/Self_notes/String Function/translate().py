"""**translate() : Translates string according to translation table str(256 chars), removing those in the del string*"""
print("-------------translate() -----------------")
print('translate(): Translates string according to translation table str(256 chars), removing those in the del string.')
trans_string = "India is my country."
# trans_table = maketrans("aioshc","@!0$#(")
print("Original String is:")
print(trans_string)
print("\n")
print("Translated String is:")
print(trans_string.translate(str.maketrans("Iiact", "1l@($")))
print("-------------------------------------------------------------------------------------")
