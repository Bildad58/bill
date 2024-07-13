print("Starting operation.....")
try:
  a = int(input("Enter a number: "))
  b = int(input("Enter a number: "))

  print(a/bd)

except ZeroDivisionError:
   print("This number cannot be divided by zero!")
except ValueError:
   print("Please input only numbers!!")
# except NameError:
#    print("The name is unavailable")
except  TypeError:
   print("Please follow instruction")
except Exception as c:
   print("Sorry, something went wrong!")
finally:
   print("Finishing operation....")


