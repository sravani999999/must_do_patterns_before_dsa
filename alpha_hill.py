n=int(input())
space="  "
l=[chr(x) for x in range(65,91)]
if n==1:
    print("A")
else:
    print(space*(n-1)+"A")
    for i in range(2,n+1):
        for j in range(1):
            l1=l[0:i]+l[i-2::-1]
            print(space*(n-i),end="")
            print(*l1)

#if n=6
'''
          A
        A B A
      A B C B A
    A B C D C B A
  A B C D E D C B A
A B C D E F E D C B A

'''