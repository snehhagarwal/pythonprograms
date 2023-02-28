x=input("enter:")
a=0
c=0
for i in x:
    if i==" ":
      a=a+1
for i in x:
   if i.isalnum():
        c=+1
print("the number of words are:",len(x)-a)    
print("the number of characters are:",len(x))
print("percentage is:",(c/len(x))*100)
