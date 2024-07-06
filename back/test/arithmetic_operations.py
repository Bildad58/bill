def perform_operation(num1, num2, operation):
    if operation =='add':
        return num1 + num2
    
    elif operation == 'subtract':
        return num1 - num2
    
    elif operation =='multiply':
        return num1 * num2 
    
    elif operation == 'divide':
        if num2 == 0:
            return 
        else:
            return num1 / num2
       
    else:
       print("Invalid number and operation:")

num1 = float(input("Enter number of choice:"))
num2 = float(input("Enter number of choice:"))
operation =input("Enter operation operator of choice:")

result = perform_operation(num1, num2, operation)
print(f"Result: {result}")

perform_operation(num1, num2, operation)

      