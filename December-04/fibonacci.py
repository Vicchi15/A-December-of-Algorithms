no=int(input("Enter the number"))
def fib_series(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n<0:
        print("Negative no,can't find the series.")
    else:
        return(fib_series(n-1)+fib_series(n-2))
    
result=fib_series(no)
print("The {}th number in the fibonacci series is:{}".format(no,result))
