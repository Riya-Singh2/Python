
l=[]
while True:
  c=int(input(
    '''
   1.Push Element
   2. Dqueue Element
   3. front Element
   4. last Element
   5.Display Queue
   6. Exit
 
    '''
  ))
  if c==1:
    n=input("Enter the value: ")
    l.append(n)
    print(l)
  elif c==2:
    if len(l)==0:
       print("empty List")
    else:
       del l[0]
       
       print(l)
  elif c==3:
      if len(l)==0:
       print("empty List")
      else:
        print("first front Element" , l[0])
  elif c==4:
     if len(l)==0:
       print("empty List")
     else:
        print("first front Element" , l[-1])
  elif c==5:
      print("Display Queue")
  elif 6:
    break;
else:
  print("invalid OPeration")
