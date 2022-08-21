n=int(input("enter any no."))
def sum(n):
 if n<=1:
  return 1
 else:
  return n+sum(n-1)
print(sum(n))