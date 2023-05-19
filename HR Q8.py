nos=input().split()
for i in range (0,len(nos)):
    nos[i]=int (nos[i])
s=sum(nos)
print(str(s-max(nos))+" "+str(s-min(nos)))
# we get min by subtracting total sum - max(nos) vice versa for min