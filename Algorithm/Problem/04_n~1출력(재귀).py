def print_to_n(n):
    print(n)
    if n > 1:
        print_to_n(n - 1)

if __name__ == '__main__':
    print_to_n(20)