n=10
insq="NYYYNNYYYY"
outsq="YYNYYNYYNY"
inlist=[]
outlist=[]
for i in range(n):
    if insq[i]=="N":
        inlist.append(0)
    else:
        inlist.append(1)
for i in range(n):
    if outsq[i]=="N":
        outlist.append(0)
    else:
        outlist.append(1)
print(inlist)
print(outlist)
metric=[]
for i in range(n):
    metric.append([])
    for j in range(n):
        if abs(j-i)>1:
            metric[i].append("N")
        elif i==j:
            metric[i].append("Y")
        else:
            if outlist[i]*inlist[j]==0:
                metric[i].append("N")
            else:
                metric[i].append("Y")
for i in range(n):
    print("".join(map(str,metric[i])))