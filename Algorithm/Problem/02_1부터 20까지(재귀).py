def print_to_n(n):
    if 0 < n:
        print_to_n(n-1)
    print(n)

if __name__ == '__main__':
    print_to_n(20)