# Quick

## 퀵 정렬 알고리즘(Quick Sort Algorithm)

- 현존하는 **정렬 알고리즘 중에서 가장 빠르다**고 알려져 있다.
- **빠른 속도와 함께 구현하기가 단순**하며 사용하는 **메모리가 적기 때문에 주로 사용**된다.
- **정렬 방법**
  - 퀵 정렬의 **기본 개념은 정렬할 리스트에서 하나를 선택해서 이것을 기준으로 양쪽으로 나눈**다.
  - 기준이 된 가운데 데이터를 **비교해서 기준이 되는 데이터보다 작으면 왼쪽으로 크면 오른쪽**으로!
  - 이를 **반복**한다.

```python
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

if __name__ == '__main__':
    list = []
    for i in range(10):
        list.append(random.randint(1, 10))

    print('<정렬 전>')
    print(list)
    print('<정렬 후>')
    quick_sort(list)
    print(list)
```

```
<정렬 전>
[1, 1, 4, 4, 4, 9, 10, 2, 8, 9]
<정렬 후>
[1, 1, 2, 4, 4, 4, 8, 9, 9, 10]
```

- 이미 데이터가 정렬되어 있는 최선의 경우나 데이터가 역으로 정렬되어 있는 경우, 오히려 성능이 많이 저하된다.