n=int(input())
space=" "
star="* "
c=(n*2)+2
for i in range(1,n+1):
    for j in range(1):
        print(star*(i)+space*(c)+star*(i))
        c-=4

    k=c+8
for i in range(n-1,0,-1):
    for j in range(1):
        print(star*(i)+space*(k)+star*(i))
        k+=4

#if n=3
'''


*         * 
* *     * * 
* * * * * * 
* *     * * 
*         * 


'''
