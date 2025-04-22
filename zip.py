#zip function

l=[1,44,65,4,3]
l1=[3,6,3,3]

for a,b in zip(l,l1):
  print(a,b)

print(" ")

# withou zip function
t=len(l1)
for h in range(t):
  print(l[h],l1[h])