import random

def insertion_sort(random_list):
    for i in range(1, len(random_list)):
        for j in range(i, 0, -1):
            if random_list[j] < random_list[j - 1]:
                random_list[j], random_list[j - 1] = random_list[j - 1], random_list[j]

if __name__ == '__main__':
    list = []
    for i in range(10):
        list.append(random.randint(1, 10))
    print('<정렬 전>')
    print(list)
    insertion_sort(list)
    print('<정렬 후>')
    print(list)