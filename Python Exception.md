# Python Exception

## 1. 예외의 종류를 아는 경우

- 예외 처리 대신 if else를 사용할 수 있음

```python
try:
    # 에러가 발생할 가능성이 있는 코드
    
except Exception: # 에러 종류
    # 에러가 발생 했을 경우 처리할 코드
```

## 2. 예외의 종류를 모르는 경우

- 아래 코드에서 ex는 발생한 에러의 이름을 받아옴

```python
try:
    # 에러가 발생할 가능서이 있는 코드

except Exception as ex:
    print('다음과 같은 에러가 발생: {}'.format(ex))
```

