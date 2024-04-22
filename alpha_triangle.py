n=int(input())
l=[chr(x) for x in range(65,91)]
for i in range(1,n+1):
    for j in range(i):
        print(l[n-j-1],end=" ")
    print()

#if n=5
'''
E
E D
E D C
E D C B
E D C B A

'''