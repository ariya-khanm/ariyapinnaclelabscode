def perform_addition(num1, num2):
  """Adds two numbers and returns the result."""
  return num1 + num2

def perform_subtraction(num1, num2):
  """Subtracts two numbers and returns the result."""
  return num1 - num2

def perform_multiplication(num1, num2):
  """Multiplies two numbers and returns the result."""
  return num1 * num2

def perform_division(num1, num2):
  """Divides two numbers and handles division by zero."""
  if num2 == 0:
    return "Error: Cannot divide by zero."
  else:
    return num1 / num2

def calculate():
  """Prompts the user for input, performs the selected operation, and displays the result."""
  print("Welcome to the Simple Calculator!")

  while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4'):
      try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
      except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

      if choice == '1':
        result = perform_addition(num1, num2)
        print(f"{num1} + {num2} = {result}")
      elif choice == '2':
        result = perform_subtraction(num1, num2)
        print(f"{num1} - {num2} = {result}")
      elif choice == '3':
        result = perform_multiplication(num1, num2)
        print(f"{num1} * {num2} = {result}")
      else:
        result = perform_division(num1, num2)
        print(result)  # Handles division by zero error message

    elif choice == '5':
      print("Exiting calculator.")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
  calculate()