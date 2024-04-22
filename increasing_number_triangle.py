n=int(input())
c=0
for i in range(1,n+1):
    for j in range(i):
        c+=1
        print(c,end=" ")
    print()

#if n=5
'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15


'''