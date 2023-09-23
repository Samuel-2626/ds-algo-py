# Write a function called reverseString that takes in a string 
# and returns the reverse of that string. In this section, 
# we are really focusing on loops without using any built-in methods, 
# so try that first. If you get stuck, you can always use the 
# built-in methods to solve the problem.


def main() -> None:
    print(reverse_string("12345"))

def reverse_string(string: str) -> str:

    reversed_word: str = ""
    
    for char in reversed(range(len(string))):
        reversed_word += string[char]

    return reversed_word



if __name__ == "__main__":
    main()