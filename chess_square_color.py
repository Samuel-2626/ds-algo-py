# Write a getChessSquareColor() function that has parameters column and row. 
# The function either returns 'black' or 'write' depending on the color at the
# specified column and row. Chess boards are 8 X 8 spaces in size, and the columns
# and rows in this program begin at 0 and end at 7. If the arguments for column or row
# are outside the 0 - 7 range, the function returns a blank string.
# Note that chess boards always have a white square in the top left corner.



def main() -> None:
    ...

def getChessSquareColor(column: int, row: int) -> str:
    if column < 1 or row < 1:
        return ''
    elif column > 8 or row > 8:
        return ''
    elif column == row:
        return 'white'
    else:
        return 'black'



if __name__ == "__main__":
    main()


assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''