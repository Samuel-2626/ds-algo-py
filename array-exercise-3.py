# Create a list of all odd numbers between 1 and a max number. 
# Max number is something you need to take from a user using input() function

number: int = int(input("Give me number: "))

odd_numbers: list[int] = []

for n in range(1, number):
    if n % 2 == 1:
        odd_numbers.append(n)

print(odd_numbers)

