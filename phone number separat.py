x=input("enter the phone number:")
if len(x)==12:
    if x[0:3].isdigit() and x[4:7].isdigit() and x[8:12].isdigit():
        if x[0:12:4]=="-":
            print("the number is valid")
else:
    print("number not valid")

