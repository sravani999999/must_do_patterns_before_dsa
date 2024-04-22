n=int(input())
space=" "
l=[x for x in range(1,21)]
for i in range(1,n+1):
    for j in range(1):
        s=l[0:i:1]
        print(*s,end="")
        print(space*(((n+2)-((i-1)*2))*2),end=" ")
        s=l[i-1::-1]
        print(*s,end="")
    print()
#if n=5
'''
1                 1
1 2             2 1
1 2 3         3 2 1
1 2 3 4     4 3 2 1
1 2 3 4 5 5 4 3 2 1

'''