'''
Example of how generic exception handling may be done.
'''
__author__ = 'Keith Wright'
# Assign numerator by default to 1000
numerator = 1000

# Receive user_input for a number to use as denominator as a 'str'
user_input = input('Number to divide 1000 by: ')

# Convert user_input to a floating point value for the denominator
try:
    # Put statements that may cause exceptions in the try clause

    # Will cause ValueError with non-numeric values as user_input
    denominator = float(user_input)
    
    # Will cause ZeroDivisionError with zero (0) value as user_input
    result = numerator / denominator

except Exception:
    # Display an error message
    print("Bad input or infinity")
else:
    # Show the successful result 
    # Display the calculation and the result
    print ('{:d} divided by {: .3f} equals {:+4.5f}'.format(numerator, denominator, result))
finally:
    # Display at message after exiting the try block
    print("We are finished")

