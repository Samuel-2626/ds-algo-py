# In English, ordinal numerals have suffixes such as the "th" in "30th" or "nd" in "2nd".
# Write an ordinalSuffix() function with an integer parameter named number and returns a 
# string of the number with its ordinal suffix. For example, ordinalSuffix(42) should 
# return the string '42nd'




def main() -> None:
    print(ordinalSuffix(1))


def ordinalSuffix(number: int) -> str:

    number_without_prefix: str = str(number)



    if number_without_prefix == "11" or number_without_prefix == "12" or number_without_prefix == "13":
        return number_without_prefix + "th"
    if number_without_prefix[-1] == "1":
        return  number_without_prefix + "st"
    elif number_without_prefix[-1] == "2":
        return number_without_prefix + "nd"
    elif number_without_prefix[-1] == "3":
        return number_without_prefix + "rd"
    else:
        return number_without_prefix + "th"   



if __name__ == "__main__":
    main()



assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'
