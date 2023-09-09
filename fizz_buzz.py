# Fizz buzz is a word game you can implement in a single program. 
# It became famous as a screening question in coding interviews to quickly determine
# if candidates had any programming ability whatsoever, so being able to solve it 
# quickly leads to a good first impression.

def main() -> None:
    fizzBuzz(35)

def fizzBuzz(upTo: int) -> None:
    for number in range(1, upTo + 1):
        if number % 3  == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:
            print("Fizz", end=" ")
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(number, end=" ") 



if __name__ == "__main__":
    main()