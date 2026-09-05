# Store input numbers from the user
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Convert the inputs to float to allow both whole numbers and decimals
sum_result = float(num1) + float(num2)

# Display the sum using an f-string
print(f"The sum of {num1} and {num2} is {sum_result}")

