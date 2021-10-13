a, b, c = 10, 30, 20
if a>b:
    max = 'a'
    if a < c:
        max = 'c'
else:
    max = 'b'
    if b < c:
        max = 'c'
print(max)
