d={}
for i in range (11):
    key=input("enter the roll number:")
    value=input("enter the name of student:")
    d[key]=value
print(d)
a=d.values()
print(a)
for i in a:
    if len(i)==5:
        print(i)
