x=input("Enter the word along with its key:")
x=x.split()
word=x[0]
n=int(x[1])
str=""
for i in word:
    i=chr(ord(i)+n)
    str+=i
print("Encoded output for '{}' is:{}".format(x[0],str))
