n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+i-1),end=" ")
    print()

#if n=6
'''
A
B B
C C C
D D D D
E E E E E
F F F F F F

'''