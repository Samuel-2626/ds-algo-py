# Write a function called countOccurrences() that takes in a string 
# and a character and returns the number of occurrences of that character in the string.


def main() -> None:
    print(count_occurrences("Apple", "p"))

def count_occurrences(word: str, char: str) -> int:
    count: int = 0
    for letter in range(len(word)):
        if word[letter] == char:
            count += 1
        
    return count


if __name__ == "__main__":
    main()