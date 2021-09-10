l=list(input().split(" "))
m=int(l[0])
n=int(l[1])
a=m*n

for i in range(16*16):
    if a%2==0:
        print(int(a/2))
        break
    else:
        a=a-1


        