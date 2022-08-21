a=1
sum=0
while a<1000:
 b=a
 while b!=0:
  r=b%10
  sum=sum+r**3
  a=int(b/10)
 if sum==b:
  print("Armstrong no. are")
  print(b)
 sum=0
