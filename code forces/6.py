
flag1=False

def inta(s):
    for i in range(len(s)):
        s[i]=int(s[i])

def check(l):
    for i in l:
        inta(i)
    flag=False
    for i in l:
        for j in i:
            if j !=1 and j!=0:
                flag=True
                l=list()
                break
            else:
                flag=False
    
    for i in range(len(l)):
        if len(l[i]) !=3:
            flag=True
            l=list()
            break
        else:
            flag=False
    return flag




n=int(input())

while n>1000 or n <1:
    n=int(input())


l=list()
for i in range(n):
    l.append(input().split(" "))



while check(l):
    l=list()
    for i in range(n):
        l.append(input().split(" "))
    
sum=0
for  i in l:
    count=0
    for j in i:
        if j==1:
            count=count+1
    if count>1:
        sum=sum+1
    
print(sum)