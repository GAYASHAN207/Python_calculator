while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
    

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  def select_op(choice):
      if choice=='#':return(-1)
      elif choice=='+':return(1)
      elif choice=='-':return(2)
      elif choice=='*':return(3)
      elif choice=='/':return(4)
      elif choice=='^':return(5)
      elif choice=='%':return(6)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()

  n1=input('Enter first number: ')
  print(n1)
  if '$'in list(n1):
      continue
  if n1=='#':
      print('Done. Terminating')
      exit()
  n2=input('Enter second number: ')
  print(n2)
  if '$' in list(n2):
      continue
  if n2=='#':
      print('Done. Terminating')
      exit()
  if (select_op(choice)==1):
      x=float(n1)
      y=float(n2)
      print(x,'+',y,'=',x+y)
  if (select_op(choice)==2):
      x=float(n1)
      y=float(n2)
      print(x,'-',y,'=',x-y)
  if (select_op(choice)==3):
      x=float(n1)
      y=float(n2)
      print(x,'*',y,'=',x*y)
  if (select_op(choice)==4):
      try:
          x=float(n1)
          y=float(n2)
          print(x,'/',y,'=',x/y)
      except:
          print('float division by zero')
          print(x,'/',y,'=','None')
  if (select_op(choice)==5):
      x=float(n1)
      y=float(n2)
      print(x,'^',y,'=',x^y)
  if (select_op(choice)==6):
      x=float(n1)
      y=float(n2)
      print(x,'%',y,'=',x%y)
        
