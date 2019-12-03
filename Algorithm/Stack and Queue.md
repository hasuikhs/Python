# Stack과 Queue

## 1. Stack

- Stack이란 바닥부터 데이터를 차곡차곡 쌓는 개념
- 이와 같은 방식을 **LIFO(Last In First Out)**이라고 함
- `push` 와 `pop`이 기본

```python
def push(item):
    stack.append(item)
    
def pop():
    return stack.pop()

if __name__ == '__main__':
    stack = []
    push(1)
    push(2)
    push(3)
    push(4)
    print("현재 stack의 모습")
    print(stack)
    
    while stack:
        print(f'POP > {pop()}')
```

```
현재 stack의 모습
[1, 2, 3, 4]
POP > 4
POP > 3
POP > 2
POP > 1
```

## 2. Queue

- 처음으로 저장한 데이터를 처음 사용하는 방식
- 이와 같은 방식을 **FIFO(First In First Out)**라고 함
- `put`과 `get`이 기본

```python
def put(item):
    queue.append(item)

def get():
    return queue.pop()

if __name__ == '__main__':
    queue = []
    put(1)
    put(2)
    put(3)
    put(4)

    print('현재 queue의 모습')
    print(queue)

    while queue:
        print(f'GET > {get()}')
```

```
현재 queue의 모습
[1, 2, 3, 4]
GET > 4
GET > 3
GET > 2
GET > 1
```

