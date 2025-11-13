class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        sum = self.num1 + self.num2
        return sum

    def subtract(self):
        diff = self.num1 - self.num2
        return diff

    def multiply(self):
        product = self.num1 * self.num2
        return product

    def division(self):
        if self.num2 == 0:
            return "Can't be divided by 0"

        divide = self.num1 / self.num2
        return divide


def get_user_input():

    while True:
        try:
            print("Enter two numbers below")
            user_input1 = int(input("Enter the first number:"))
            user_input2 = int(input("Enter the second number:"))

            num1 = user_input1
            num2 = user_input2

            return num1, num2
        except ValueError:
            print("Invalid Input")


def get_operator_choice():
    print("1, add or +")
    print("2, minus or -")
    print("3, multiply or *")
    print("4, divide or /")

    choice = (
        input("Enter the number or symbol of your choice (e.g., 1, add or +): ")
        .strip()
        .lower()
    )
    return choice


if __name__ == "__main__":
    n1, n2 = get_user_input()

    if n1 is not None and n2 is not None:

        my_calculator = Calculator(n1, n2)
        choice = get_operator_choice()

        result = None
        operation = ""

        if choice in ("1", "add", "+"):
            result = my_calculator.add()
            operation = "+"
        elif choice in ("2", "minus", "-"):
            result = my_calculator.subtract()
            operation = "-"
        elif choice in ("3", "multiply", "*"):
            result = my_calculator.multiply()
            operation = "*"
        elif choice in ("4", "divide", "/"):
            result = my_calculator.division()
            operation = "/"
        else:
            print("\n Invalid choice. Please select a number or symbol from the list.")

        if result is not None and operation:
            print("--- Final Result ---")
            print(f"{n1} {operation} {n2} = {result}")

    print("Calculation Done")
