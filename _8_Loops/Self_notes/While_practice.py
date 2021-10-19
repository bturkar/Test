k = 0
while k < 5:
    print(k)
    k += 1
# num1 = int(input('enter num1 : '))
num1 = 1
# num2 = int(input('enter num2 : '))
num2 = 5
while num1 < num2:
    print('num1 :', num1)
    num1 += 1
"""Ex 1"""
# num1 = int(input('enter num1 : '))
num1 = 10
# num2 = int(input('enter num2 : '))
num2 = 20
while True:
    if num1 < num2:
        print('num1 :', num1)
        num1 += 1
        if num1 == 2:
            print('num1 is 2')
        else:
            print('num1 is not 2')
    else:
        break
"""Example =="""

num = 0
while True:
    if num < 5:
        print(num)
    else:
        break
    num += 1
"""Example"""
print('Ex=2')
flag = True
k = 0
while flag:
    print(flag)
    flag = False
    if not flag:
        break
"""Ex=3"""
print('Ex=3')
flag = True
k = 0
while not flag:  # while false will not run
    print(flag)
    flag = False
    if not flag:
        break
"""print number from 1 to 5"""
i = 1
while i < 6:
    print(i)
    i += 1
"""print number from 1 to 6 except 3"""
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
"""while with else"""
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
"""ex"""
# Program to add n natural number


# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
s = 0
i = 1

while i <= n:
    s = s + i
    i = i + 1  # update counter

# print the sum                                  while with else
print("The sum is", s)

#
counter = 0

while counter < 3:
    print("In loop")
    counter = counter + 1
else:
    print("out of loop")

"""sum of 8 natural number"""
count = 0
while count < 9:
    print('The count is:', count)
    count = count + 1

print("Good bye!")

"""print number from 4 to 0 except 2   while with continue"""
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')

"""while with break"""
n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
    else:
        print('Loop done.')
print("Program to find prime number between 500 to 600")
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
num1=4
while num1>0:
    for i in range(0,4):
        print(4-i)
    num1 -= 1

print("************************gggggggggg*******************")
p=0
while p<4:
    while (k-p)<4:
        print(k-p)
        k += 1
    p += 1