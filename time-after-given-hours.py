h=int(input("enter no of hours between 1 to 12:"))
n=int(input("no. of hours ahead:"))
sum=h+n
if sum<12 :
    print("time after those no. of hours:",sum,"0,clock")
elif sum>12:
    print("time after those no. of hours:",sum-12,"0'clock") 
