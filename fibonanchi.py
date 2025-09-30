def print_fibonachi(n):
    a, b = 0, 1
    print(a)
    print(b)
    for i in range(2, n):
        c=a+b
        print(c , end=' ')
        a, b = b, c
print_fibonachi(7)
#output=0,1,1,2,3,5,8
