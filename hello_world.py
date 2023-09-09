# Write a program that, when run, greets the user by printing "Hello, world!" on the screen.
# Then it prints a message on the screen asking the user to enter their name. 
# The program greets the user by name by printing the "Hello, " followed by the user's name.


def main() -> None:
    hello()


def hello() -> None:
    print("Hello, world!")
    name: str = input("Please, enter your name: ")
    print("Hello,", name)


if __name__ == "__main__":
    main()