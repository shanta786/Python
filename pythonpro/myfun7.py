a=int(input("enter any no."))
def fact(a):
 if a==0:
  return 1
 else: 
  return a*fact(a-1)
print(fact(a))