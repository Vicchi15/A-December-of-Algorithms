x=input("Input a no with even no of digits")
l=len(x)
l=int(l/2)
first=list(x[:l])
sec=list(x[l:])
def sum(a):
    sum1=0
    for i in a:
        sum1+=int(i)
    return sum1

s1=sum(first)
s2=sum(sec)
if(s1==s2):
    print("true")
print("false")
