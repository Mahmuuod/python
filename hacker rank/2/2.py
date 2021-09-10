def inte(arr):
    for i in range(len(arr)):
        arr[i]=int(arr[i])










n=int(input())
while n<2 or n>10:
   n=int(input())

a=list(input().split(" "))
while len(a)!=n:
     a=list(input().split(" "))


inte(a)

flag=False

for i in range(n):
    if a[i]< -100 or a[i]>100:
            flag=True




while flag:
    a=list(input().split(" "))
    inte(a)
    for i in range(len(a)):
        if a[i]< -100 or a[i]>100:
            flag=True
            break;
        else:
            flag=False


a.sort(reverse=True)

for i in range(len(a)-1):
    if a[i]==a[i+1]:
        continue
    else:
     print(a[i+1])
     break




