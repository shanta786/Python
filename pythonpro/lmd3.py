def table(n):
 return lambda a:a*n
n=int(input("enter any no."))
b=table(n)
for i in range(1,11):
 print(n,"x",i,"=",b(i))