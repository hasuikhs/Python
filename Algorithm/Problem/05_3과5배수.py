def function(n):
    i = 1
    while i <= n:
        if (i % 3 == 0) & (i % 5 == 0):
            print(f'{i}는 3과 5의 배수')
        i += 1

if __name__ == '__main__':
    function(100)
        