import random

def selected_sort(random_list):
    for i in range(len(random_list) - 1):
        min_idx = i
        for j in range(i + 1, len(random_list)):
            if random_list[j] < random_list[min_idx]:
                min_idx = j
        random_list[i], random_list[min_idx] = random_list[min_idx], random_list[i]

if __name__ == '__main__':
    list = []
    for i in range(10):
        list.append(random.randint(1, 10))
    print('<정렬 전>')
    print(list)
    selected_sort(list)
    print('<정렬 후>')
    print(list)