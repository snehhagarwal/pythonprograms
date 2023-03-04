l=["hi","my","name","sneha","agarwal"]
t=()
for i in l:
    x=len(i)
    t=t+(x,)
a=max(t)
for i in l:
    if a==len(i):
        print(i)
