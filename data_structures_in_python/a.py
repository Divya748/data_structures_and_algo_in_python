from itertools import combinations
n=int(input("enter the values"))
list1=[]
for i in range(n):
    a=int(input("enter the list of elements"))
    list1.append(a)
m=0
if n>5:
    comb=combinations(list1,5)
    list2=list(comb)
    for i in list2:
        x=1
        for j in i:
            x=j*x
        if m<x:
            m=x
    if m<0:
        print(m%(10**9+7))
    else:
        print(m)
else:
    x=1
    for i in list1:
        x=i*x
    if x<0:
        print(x%(10**9+7))
    else:
        print(x)


    
