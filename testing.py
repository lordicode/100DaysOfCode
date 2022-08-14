def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def exponent(n1, n2):
    return n1 ** n2


def modulo(n1, n2):
    return n1 % n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": exponent,
    "%": modulo
}

def calculator():
  num_1 = int(input("Enter first variable: "))

  for key in operations.keys():
      print(key)

  operations_key = input("Pick an operation: ")
  num_2 = int(input("Enter second variable: "))
  answer = operations[operations_key](num_1, num_2)

  print(f"{num_1} {operations_key} {num_2} = {answer}")

  while True:
      c = input("Do you want to continue with the result? Yes or No ")
      if c.lower().strip() == "yes":
          num_1 = answer
          print(f"Num 1 is {answer} ")
          for key in operations.keys():
              print(key)

          operations_key = input("Pick an operation: ")
          num_2 = int(input("Enter second variable: "))
          answer = operations[operations_key](num_1, num_2)

          print(f"{num_1} {operations_key} {num_2} = {answer}")
      else:
          calculator()

calculator()