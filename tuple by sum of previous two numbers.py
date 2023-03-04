fb=(0,1,1)
for i in range(6):
    fb=fb+(fb[i+1]+ fb[i+2],)
print(fb)
