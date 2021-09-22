def square(x, y):
    return x * y

if __name__ == '__main__':
    a = [1, 4, 6]
    b = [10, 20, 100]

    # [10, 80, 600]と出力される
    print(list(map(square, a, b)))
