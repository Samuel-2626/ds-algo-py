# Write three functions for this exercise. First, write a writeToFile() function with
# two parameters for the filename of the file and the text to write into the file.
# Second, write an appendToFile() function, which is identical to writeToFile() except 
# that the file opens in append mode instead of write mode. Finally, write a readFromFile()
# function with one parameter for the filename to open. This function returns the full text
# contents of the file as a string.


def main() -> None:
    ...
    

def writeToFile(filename: str, content: str) -> None:
    with open(filename, "w") as my_file:
        my_file.write(content)


def appendToFile(filename: str, content: str) -> None:
    with open(filename, "a") as my_file:
        my_file.write(content)


def readFromFile(filename: str) -> str:
    with open(filename) as my_file:
        file_content = my_file.read()

    return file_content




if __name__ == "__main__":
    main()


writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'
