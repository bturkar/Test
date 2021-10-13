s=()
print(type(s))
s=set()
print(type(s))
s={}
print(type(s))

s={1,2,2}
print(type(s))
s={()}
# s={[]} #ERROR LIST CAN NOT BE A ELEMENT IN SET
#S={[1,2]}  #ERROR
#s={[1,2,3]} ERROR LIST CAN NOT BE ELEMNT IN LIST
s={(1,2)}
#s={{1,2}} error
#s={{'a':1,'b':5}}   ERROR
print(type(s))
print(s)
s
dict={'Bhavesh':33, 'Bhaskar':34}
a='Bhaskar'
print(dict[a])
