# Write two functions, isOdd() and isEven(), with a single numeric parameter name number.
# The isOdd() function returns True if number is odd and False if number is even.
# The isEven() function returns the True if number is even and False if number is odd.
# Both functions return False for numbers with fractional parts, such as 3.14 or -4.5.
# Zero is considered an even number.

def main() -> None:
    print(isOdd(42)) # -> False
    print(isOdd(9999)) # -> True
    print(isOdd(-10)) # -> False
    print(isOdd(-11)) # -> True
    print(isOdd(3.1415)) # -> False
    print(isOdd(0)) # -> False
    print(isEven(0)) # -> True
    print(isEven(42)) # -> True
    print(isEven(9999)) # -> False
    print(isEven(-10)) # -> True
    print(isEven(-11)) # -> False
    print(isEven(3.1415)) # -> False



def isEven(number: float) -> bool:
    return number % 2 == 0

def isOdd(number: float) -> bool:
    return number % 2 == 1


if __name__ == "__main__":
    main()


assert isOdd(42) == False
assert isOdd(9999) == True
assert isOdd(-10) == False
assert isOdd(-11) == True
assert isOdd(3.1415) == False
assert isEven(42) == True
assert isEven(9999) == False
assert isEven(-10) == True
assert isEven(-11) == False
assert isEven(3.1415) == False
assert isEven(0) == True
assert isOdd(0) == False