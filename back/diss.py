#prompt the user to input the following
sport = input("Enter sport of choice:")
age = int(input("Enter your age:"))
access = input("Enter your authority:")

#use the match case statement
match sport:
    case 'football':
        if age >= 18 < 35:
            print("Fully permitted to play")
        elif age < 18:
         print("partially permitted to play")
        else:
         print("No permission granted") 
    case 'basketball':
        if age >= 18 < 35:
           print("Fully permitted to play")
        elif age <18 :
           print("partially permitted to play")
        else:
           print("No permission granted")
    case 'Tennis':
      if age >=18 < 35:
         print("Fully permitted to play")
      elif age < 18:
         print("partially permitted to play")
      else:
         print("No permission granted")
    case 'rugby':
      if age >= 18 < 35:
          print("Fully permitted to play")
      elif age <18 :
         print("partially permitted to play")
      else:
         print("No permission granted")
      case _ :
      print("No sport found")
      
match access:
   case member:
      if age >= 18:
         print("full authority")
      else:
         print("No access")
    

        

      



         


        
    
    