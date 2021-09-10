n=int(input())
string=list()
while n<1 or n>100:
    n=int(input())

for i in range(n):
   string.append(input())

for i in range(n):
    if len(string[i])>10:
        string[i]=string[i][0:1]+str(len(string[i])-2)+string[i][len(string[i])-1:len(string[i])]





for i in string:
    print(i)