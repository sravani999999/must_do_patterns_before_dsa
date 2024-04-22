n=int(input())
c=0
k=0
for i in range(1,n+1):
    c=0
    k=0
    for j in range(i):
        if i%2!=0:
            c+=1
            if c%2!=0:
                print(1,end=" ")
            else:
                print(0,end=" ")
        else:
            k+=1
            if k%2!=0:
                print(0,end=" ")
            else:
                print(1,end=" ")
    print()

#if n=5
'''
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1


'''