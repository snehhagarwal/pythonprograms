l=[3,6,9,12,4,54,45]
for i in range(1,len(l)):
    small=l[i]
    for j in range(i-1,-1,-1):
        if l[j]>small:
            l[j+1]=l[j]
            l[j]=small
            print("\nlist after pass",i)
            for j in range(0,len(l)):
                   print(l[j],end=' ')
