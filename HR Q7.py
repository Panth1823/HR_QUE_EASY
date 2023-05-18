N=int(input())
ari=input().split()
posi={"pos":0,"neg":0,"zero":0}
for i in ari:
    if int(i)>0:
        posi["pos"]+=1
    elif int(i)<0:
        posi["neg"]+=1
    else:
        posi["zero"]+=1

print(format(posi["pos"]/N ,'.6f'))
print(format(posi["neg"]/N ,'.6f'))
print(format(posi["zero"]/N ,'.6f'))