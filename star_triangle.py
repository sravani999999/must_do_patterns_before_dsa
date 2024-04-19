n=int(input())
space=" "
star="*"
for i in range(n):
    for j in range(1):
        print(space*(n-(i+1))+(star*(2*i+1)))
    print()

#if n=6
'''


     *

    ***

   *****

  *******

 *********

***********


'''