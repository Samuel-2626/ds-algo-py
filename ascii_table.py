# Write a printASCIITable() function that displays the ASCII number and its corresponding
# text character, from 32 to 126. (These are called the printable ASCII characters).


def main() -> None:
    printASCIITable()


def printASCIITable() -> None:
    for number in range(32, 126 + 1):
        print(number, chr(number))


if __name__ == "__main__":
    main()