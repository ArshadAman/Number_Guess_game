#python 3.7.1
print ("Welcome To Guessing Game\nYou Have to Guess the Right Number.\nYou Have 10 attempts after that\nYou will loose\n")

gno=55
hint=0

while(True):
  if(hint==10):
    print ("You Failed!","You have no Attempts left")
    print("The Number Was",gno)
    break
  else:
    n=int(input("Guess The Number- "))
    if(n<gno):
      print("\nOops! Try Again\n\n","Hint:- Try Greater Number\n")
      hint+=1
      print("Attempts Left: ",10-hint,"\n")
      continue 
      
    elif (n>gno):
      print ("\nOops! Try Again\n\n","Hint :-Try Smaller Number\n")
      hint+=1
      print("Attempts Left: ",10-hint,"\n")
      continue 
     
    else:
      print ("\nCongo! You Guessed it Right\n","Attempts:- ",hint)
      break
