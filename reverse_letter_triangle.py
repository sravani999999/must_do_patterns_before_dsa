n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()

#if n=5
'''
A B C D E
A B C D
A B C
A B
A

'''