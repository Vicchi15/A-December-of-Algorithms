sp=input("Enter a word along with its quantity:")
sp=sp.split()
w=sp[0]
q=sp[1]
if q.isdigit()==False:
        print("Invalid")
        exit(0)
def singular_plural(w,q):
    if int(q)>1:
        if w[-1]=='f':
            w=w[:-1]
            w+='ves'
        else:
            w+='s'
        print(w)
    else:
        if w[-3:]=='ves':
            w=w[:-3]
            w+='f'
        if w[-1]=='s':
            w=w[:-1]
       
        print(w)
        
    
        
        
singular_plural(w,q)
