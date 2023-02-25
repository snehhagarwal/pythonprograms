l=[34,65,76,1,23,43,2]
i=0
cnt=1
while i<len(l)-1:
    if l[i]>l[i+1]:
       l[i],l[i+1]=l[i+1],l[i]
       i=0
       continue
       print("\nelement after pass:",cnt)
    for j in range(0,len(l)):
           print(l[j],end=' ')
    cnt=cnt+1
    i=i+1
