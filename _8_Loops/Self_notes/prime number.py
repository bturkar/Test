num1 = 500
num2 = 600
while num1 < num2:
    for i in range(2, int(num1/2)):
        if num1 % i == 0:
            break
    else:
        print(num1)
    num1 += 1

print("Pattern")
num1 = 4
while num1 > 0:
    for i in range(0, 4):
        print(4-i)
    num1 -= 1

print("*******************************")
for i in range(0, 4):
    for j in range(0,4-i):
        print(4-j, end=" ")
    print('')



