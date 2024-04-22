n=int(input())
space=" "
star="*"
for i in range(n,-1,-1):
    for j in range(1):
        print(space*(n-i)+(star*(2*(i-1)+1)))
    print()

#if n=5
'''


*********

 *******

  *****

   ***

    *

    
'''