# Write a function called calculator that takes in 2 numbers 
# and an operator and returns the result of the calculation.


def main() -> None:
    print(calculator(5, 5, "*"))


def calculator(num1: int, num2: int, operand: str) -> str:
    match operand:
        case "+":
            return str(num1 + num2)
        case "-":
            return str(num1 - num2)
        case "*":
            return str(num1 * num2)
        case "/":
            return str(num1 / num2)
        case _:
            return "Invalid operator"


if __name__ == "__main__":
    main()