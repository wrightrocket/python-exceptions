'''
Example of why exception handling may be needed.
'''
__author__ = 'Keith Wright'
# Assign numerator by default to 1000
numerator = 1000

# Receive user_input for a number to use as denominator as a 'str'
user_input = input('Number to divide 1000 by: ')

# Convert user_input to a floating point value for the denominator
denominator = float(user_input)
# Will cause ValueError if non-numeric value input for user_input

# Calculuator result as numerator divided by denominator
result = numerator / denominator
# Will cause ZeroDivisionError if a value of zero provided for user_input

# Display the calculation and the result
print ('{:f} divided by {:f} equals {:f}'.format(numerator, denominator, result))
