# Write a convertToFahrenheit() function with a degreeCelsius parameter. 
# This function returns the number of this temperature in degrees Fahrenheit.
# Then write a function named convertToCelsius() with a degreesFahrenheit parameter
# and return a number of this temperature in degrees Celsius.

def main() -> None:
    print(convertToFahrenheit(0)) # -> 32
    print(convertToCelsius(0)) # -> -17.77777777777778

    

def convertToFahrenheit(degreeCelsius: float) -> float:
    fahrenheit: float = degreeCelsius * (9 / 5) + 32
    return fahrenheit

def convertToCelsius(degreesFahrenheit: float) -> float:
    celsius: float = (degreesFahrenheit - 32) * (5 / 9)
    return celsius


if __name__ == "__main__":
    main()



assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15
