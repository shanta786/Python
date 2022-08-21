a=int(input("enter any no."))
f=1
i=1
if a<0:
 print("factorial not possible")
elif a==0:
 print("factorial of zero is 0")
else:
 while i<=a:
  f=f*i
  i+=1
 print("the factorial is")
 print(f)