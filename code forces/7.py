
def inta(l):
    for i in range(len(l)):
        l[i]=int(l[i])

def check(l,n):
    inta(l)
    flag=False
    for i in l:
        if i > 100 or i < 0:
            flag= True
            break
        else:
            flag= False
    if len(l)!=n:
        flag= True
    else:
        flag= False   
    return flag    

def check2(n):
    inta(n)
    if n[0]>50 or n[0]<1 or n[1]>n[0]:
        return True
    else:
        return False
        
        


n=input().split(" ")

while check2(n):
    n=input().split(" ")

l=input().split(" ")




while check(l,int(n[0])):
    l=input().split(" ")

count=0
for i in range(len(l)):
    if l[i] >= l[n[1]-1] and l[i] != 0:
        count=count+1
print(count)

