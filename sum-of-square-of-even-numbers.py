# Let's start off with a fairly simple challenge, but one that uses a few different 
# array methods. Write a function called sumOfEvenSquares that takes an array of numbers 
# and returns the sum of the squares of the even numbers in the array.

from functools import reduce


def main() -> None:
    print(sum_of_even_squares([-1, 0, 1, 2, 3, 4]))    



def sum_of_even_squares(arr: list[int]) -> int:

    # [1, 2, 3, 4, 5]

    even_num: list[int] = list(filter(lambda num: True if num % 2 == 0 else False, arr))

    square_even_num: list[int] = list(map(lambda num: num ** 2, even_num)) 

    total: int = reduce(lambda total, num: total + num, square_even_num)

    return total




if __name__ == "__main__":
    main()