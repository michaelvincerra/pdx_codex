
def even_squares(num: int):
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    squares = [x**2 for x in a]
    count = 0
    for i in squares:
        if i > 1:
            result = i / 33
            count =+ 1
            print(float(result))



even_squares(1)