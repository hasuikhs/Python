import random

def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)

def binary_search(random_list, wanted_data):
    first = 0
    last = len(random_list) - 1

    while first <= last:
        mid = (first + last) // 2

        if random_list[mid] == wanted_data:
            return mid
        elif random_list[mid] < wanted_data:
            first = mid + 1
        else :
            last = mid -1

    return None

if __name__ == '__main__':
    list = []
    for i in range(10):
        list.append(random.randint(1, 10))

    print('<정렬 전>')
    print(list)
    print('<정렬 후>')
    quick_sort(list)
    print(list)
    index = binary_search(list, 4)

    if index:
        print(list[index])
    else:
        print('찾는 숫자가 없어요')

    binary_search_recursive(list, 4)