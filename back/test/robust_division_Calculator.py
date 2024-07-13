def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denom = float(denominator)
        result = numerator/ denom
        return f"The result is {result}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Both numerator and denominator must be numeric."

# Testing the function
print(safe_divide(10, 2))         # Should print "The result is 5.0"
print(safe_divide(10, 0))         # Should print "Error: Division by zero is not allowed."
print(safe_divide("ten", 2))      # Should print "Error: Both numerator and denominator must be numeric."
print(safe_divide(10, "two"))     # Should print "Error: Both numerator and denominator must be numeric."
print(safe_divide("10", "2.5"))   # Should print "The result is 4.0"
