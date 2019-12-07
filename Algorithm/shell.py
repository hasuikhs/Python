import random

def shell_sort(random_list):
    interval = len(random_list) // 2
    while interval > 0:
        for i in range(interval):
            for index in range(i, len(random_list), interval):
                position = index
                currentValue = random_list[index]
                while position >= interval and random_list[position - interval] > currentValue:
                    random_list[position] = random_list[position - interval]
                    position -= interval
                random_list[position] = currentValue
        interval = interval // 2


if __name__ == '__main__':
    list = []
    for i in range(10):
        list.append(random.randint(1, 10))

    print('<정렬 전>')
    print(list)
    print('<정렬 후>')
    shell_sort(list)
    print(list)