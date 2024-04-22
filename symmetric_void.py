n=int(input())
space=" "
star="* "
c=0
for i in range(1,n+1):
    for j in range(1):
        print(star*(n-i+1)+space*(c)+star*(n-i+1))
        c+=4
    print()
k=c-4
for i in range(n,0,-1):
    for j in range(1):
        print(star*(n-i+1)+space*(k)+star*(n-i+1))
        k-=4
    print()

#if n=5
'''
* * * * * * * * * *

* * * *     * * * *

* * *         * * *

* *             * *

*                 *

*                 *

* *             * *

* * *         * * *

* * * *     * * * *

* * * * * * * * * *

'''