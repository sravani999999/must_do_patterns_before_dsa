n=int(input())
if n==1:
    print("*")
else:
    space=" "
    star="*"
    print(star*n)
    for i in range(n-2):
        print(star+space*(n-2)+star)
    print(star*n)
#if n=6
'''



******
*    *
*    *
*    *
*    *
******



'''
