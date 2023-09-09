# Write four functions for this exercise. The functions area() and perimeter() have
# length and width parameters and the functions volume() and surfaceArea() have
# length, width, and height parameters. This functions return the area, perimeter,
# volume, and surface area, respectively.

def main() -> None:
    ...

def area(length: int, width: int) -> int:
    return length * width

def perimeter(length: int, width: int) -> int:
    return length + width + length + width

def volume(length: int, width: int, height: int) -> int:
    return length * width * height

def surfaceArea(length: int, width: int, height: int) -> int:
    return (length * width * 2) + (length * height * 2) + (width * height * 2)

if __name__ == "__main__":
    main()

assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surfaceArea(10, 10, 10) == 600
assert surfaceArea(9999, 0, 9999) == 199960002
assert surfaceArea(5, 8, 10) == 340
