import random

def bubble_sort(random_list):
    for i in range(len(random_list) - 1):
        for j in range(1, len(random_list) - i):
            if random_list[j - 1] > random_list[j]:
                random_list[j - 1], random_list[j] = random_list[j], random_list[j - 1]

if __name__ == '__main__':
    list = []
    for i in range(10):
        list.append(random.randint(1, 10))

    print('<정렬 전>')
    print(list)
    print('<정렬 후>')
    bubble_sort(list)
    print(list)