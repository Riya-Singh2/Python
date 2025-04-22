import random

cnum=random.randrange(1,101)

n1=int(input("Enter the num1 : "))
if n1>cnum:
  print("number is high")
elif n1<cnum:
  print("number is low")
else:
  print("equel number")

