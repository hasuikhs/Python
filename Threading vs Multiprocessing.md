# Threading vs Multiprocessing

> - Python은 인터프리터 언어로 기본적으로 Single-Thread에서 순차적으로 동작

## 1. Threading

- Python에서는 threading 모듈을 사용하여 thread를 구현

```python
import threading

def thread_func(arg1, arg2):
    total = 0
    for i in range(arg1, arg2):
        total += i
        
if __name__ == "__main__":
    a, b = 0, 100
    th1 = threading.Thread(target=thread_func, args=(a, b))
    
    th1.start()
    th1.join()
```

- thread를 생성할때 target에는 함수명 args에는 인자를 적음
  - 단 인자가 하나인 함수는 `(arg1, )` 이렇게 인자를 하나 적고 콤마를 적어야 오류가 나지 않음

## 2. Multiprocessing

- multiprocessing 모듈은thread 대신 process를 만들어 병렬로 동작
- 위 코드를 process로 구현하면 다음과 같음

```python
import processing

def process_func(arg1, arg2):
    total = 0
    for i in range(arg1, arg2):
        total += i
        
if __name__ == "__main__":
    a, b = 0, 100
    pr1 = processing.Process(target=process_func, args=(a, b))
    
    pr1.start()
    pr1.join()
```

- multiprocessing 모듈은 threading 모듈과 구현 방식이 거의 같아서 쉽게 변경 가능
- process는 각자가 고유한 메모리 영역을 가지기 때문에 thread에 비해 메모리 사용이 늘어나지만,
- 싱글 머신 아키텍처로부터 여러 머신을 사용하는 분산 애플리케이션으로 쉽게 전환 가능

## Thread vs Process

- Python에서 병렬처리는 Thread와 multiprocess 사용!
- thread는 cpu 작업이 적고 I/O 작업이 많은 경우
- process는 더 많은 메모리를 필요로 하지만, 각각 proces에서 병렬로 cpu 작업 가능하고, 분산 처리가 필요한 경우