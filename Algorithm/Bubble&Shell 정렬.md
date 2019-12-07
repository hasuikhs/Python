# Bubble & Shell Sort

## 1. 거품 정렬 알고리즘(Bubble Sort Algorithm)

- 순차적으로 **바로 옆에 있는 데이터와 비교해서 옆의 데이터가 크면 자신과 위치를 변경**
- 이같은 방식으로 데이터의 **처음부터 끝까지 반복**한다.

```python
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
```

```
<정렬 전>
[7, 1, 10, 9, 5, 6, 5, 7, 10, 10]
<정렬 후>
[1, 5, 5, 6, 7, 7, 9, 10, 10, 10]
```

## 2. 셸 정렬 알고리즘(Shell Sort Algorithm)

- 셸 정렬은 기본 구조는 **삽입 정렬 알고리즘과 비슷**하지만 비교도 안될 정도로 우수하다.

```python
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
```

```
<정렬 전>
[1, 9, 10, 3, 2, 9, 2, 6, 9, 10]
<정렬 후>
[1, 2, 2, 3, 6, 9, 9, 9, 10, 10]
```

