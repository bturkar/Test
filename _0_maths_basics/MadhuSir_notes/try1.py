l=[8,3,4,3,2,1]
count=0
for i in l:
   if len(l)>i:
      d=l[i]-l[i+1]
      if d==1 or -1:
         print(d)
         break
for i in l:
   if len(l)>i:
      d1=l[i]-l[i+1]
      if d1==d :
          count+=1
print(count)

