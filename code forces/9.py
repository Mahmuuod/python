x=0
n=int(input())
l=list()
for i in range(n):
    l.append(input())
for i in l:
    if i=='X++'or i=='++X':
        x=x+1
    elif i=='X--' or i=='--X':
        x=x-1

print(x)