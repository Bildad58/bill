#simple calcualtor with match case

from unittest import result


def main():
    #prompt the user to input a number

    num1 = input("Enter the first number:")
    num2 = input("Enter the second number:")
    #prompt the user to input the operation they would likke to use
    operation = input("Enter operation of choice (+, -, *, /):")
    #formulate a match case statement

    def Operation(math):
        #matching case statement
        match math:
            case "+" : return "num1" + "num2"
            case "*" : return "num1" * "num2"
            case "/" : return "num1" / "num2"
            case "-" : return "num1" - "num2"
            case _ : return  "no such operation"
    #print result 
        result()
        Print("The result is:" , result)

if __name__ == "__main__":
    main()


