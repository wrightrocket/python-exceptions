''' This demonstrates for practice how to do simple single exception handling '''

# Assign a list of strings to the colors variable

colors = ["red", "blue", "green"]

# Add error handling by using try block of code

try:
    # Try to print the sixth element in the colors list

    print(colors[5])

# Catch the IndexError to handle it as the known exception

except IndexError:

    # Print an error message

    print("You can't print the sixth element in a three element list!")
