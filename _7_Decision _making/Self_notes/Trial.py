a = 20
b = 20
if a == b:
    print('a and b are equal')
print('if block ended')
c = 10
d = 45
print(c > 8 and d > 40)
print(c > 8 and d < 45)
print(c < 8 and d == 45)
print(c < 8 and d > 45)
print(c > 8 or d > 40)
print(c > 8 or d < 45)
print(c < 8 or d == 45)
print(c < 8 or d > 45)
'''***********************************************************************'''
print(True if [] else False)

'''*********And condition*************************************************'''

c = 10
d = 45
if c > 8 and d > 40:
    print('T & T')
elif c > 8 and d < 45:
    print('T and F')
elif c < 8 and d == 45:
    print('F and T')
elif c < 8 and d > 45:
    print('F and F')

'''********************************************************************'''
num1 = 20
num2 = 30
if num1 >= num2:
    print('number 1 is greater than number 2')
else:
    print('number 2 is greater than number 1')
'''*****************************************************************'''
if None:
    print('hi')
else:
    print('hi')
'''********************************************************************'''
if not None:
    print('hi')
else:
    print('hi')
'''*************************************************************************'''
c = 10
d = 45
if c > 8 or d > 40:
    print('T & T')
elif c > 8 or d < 45:
    print('T and F')
elif c < 8 or d == 45:
    print('F and T')
elif c < 8 or d > 45:
    print('F and F')
'''***************************************************************************'''
if not 0:
    print('hi')
else:
    print('hi')
'''*****************************************************************'''
if 100:
    print('hi')
'''******************************************************************'''

'''******************************************************************'''

x = 2
y = 8
if x < y:
    st = "x is less than y"
else:
    st = 'false'
print(st)
'''***********************************************************************'''
x, y = 8, 4

if x < y:
    st = "x is less than y"
else:
    st = "x is greater than y"
print(st)
'''****************************************************************************'''
x, y = 8, 8

if x < y:
    st = "x is less than y"

elif x == y:
    st = "x is same as y"

else:
    st = "x is greater than y"
print(st)

'''*******************************************************************************'''
x = 10
y = 8
st = "x is less than y" if (x < y) else "x is greater than or equal to y"
print(st)

'''**********************************************************************************'''
total = 100
country = "AU"
if country == "US":
    if total <= 50:
        print("Shipping Cost is  $50")
elif total <= 100:
    print("Shipping Cost is $25")
elif total <= 150:
    print("Shipping Costs $5")
else:
    print("FREE")
if country == "AU":
    if total <= 50:
        print("Shipping Cost is  $100")
else:
    print("FREE")
'''*************************************************************'''
if None:
    print('True')
else:
    print('False')
# else:
#   print('Error')   #error
'''*************************************'''
a = 9
if a == 10:
    print('first if statement ')
elif a > 10:
    print('first elif')
elif a < 10:
    print('second elif')

num = '143'
res = 314
hun = 0
dec = 0
dg = 0
