n=int(input("Enter the no of elements in a list:"))
input1=input("Enter a list:")
input1=input1.split()
x=input("Enter a guess no:")
l=0
r=n-1
def binarysearch(input1,l,r,x):
    if(r>=l):
        m=int((r-l)/2)
        mid=int(l+m)
        if(input1[mid]==x):
            return mid
        if(input1[mid]>x):
            return binary_search(input1,l,mid-1,x)
        
        return binary_search(input1,mid+1,r,x)
    return -1
       
    
a=binarysearch(input1,l,r,x)
print(a)
