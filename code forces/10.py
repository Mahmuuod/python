def inta(l):
    for i in range(len(l)):
        l[i]=int(l[i])




l=list()


for j in range(5):
    l.append(input().split(" ") ) 

    
for i in range(5):
    inta(l[i])


for i in range(5):
    for j in range(5):
        if l[i][j]==1:
            print(abs(j-2)+abs(i-2))

