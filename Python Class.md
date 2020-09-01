# Python Class

## 1. Class

- 클래스는 객체의 구조와 행동 저의
- 객체의 클래스는 초기화를 통해 제어
- 클래스는 복잡한 문제를 다루기 쉽도록 만듦

## 2. Class 정의

- 클래스를 작성하기 위해서는 class 키워드를 사용하여 새로운 클래스 작성

- Python은 대부분 naming convention이 snake_case를 사용하지만, 클래스의 naming convention은 PasalCase를 사용

  ```python
  class CustomClass:
      def __init__(self, param):
          ...
  ```

### 2.1 Class 생성

- class 생성

  ```python
  class Flight:
      ...
  ```

- class 객체 생성 및 변수에 할당

  ```python
  f = Flight()
  ```

- class method 작성

  ```python
  class Flight:
      def number(self):
          return 'fly'
  ```

- 인스턴스 메소드 접근

  ```python
  f= Flight()
  f.number()
  # 'fly'
  ```

  - Python method의 첫번째 parameter는 관례적으로 self를 사용

  - 호출 시 호출한 객체 자신이 전달되기 때문에 self라는이름을 사용

  - 이를 사용하여 class에서 바로 method로 접근하면서 위에서 할당한 Flight의 인스턴스 f를 parameter로 전달함으로써 똑같은 결과값을 얻음

    ```python
    Flight.number(f)
    # fly
    ```

### 2.2 생성자와 초기화자

- 위처럼 python에서 인스턴스를 생성할때 아래와 같이 생성자를 사용

  ```python
  f = Flight() # constructor
  ```

- 생성자로 인스턴스 생성을 호출받으면 먼저 `__new__`를 호출하여 인스턴스를 생성 할당하고, `__new__` method가 `__init__` method를 호출하여 인스턴스에서 사용할 초기값들을 초기화

  ```python
  Class Flight:
      
      def __init__(self):
          print('init')
          super().__init__()
          
      def __new__(cls):
          print('new')
          return super().__new__(cls)
      
      def number(self):
          return 'fly'
  ```

- 다시 인스턴스를 생성해보면

  ```python
  f = Flight()
  
  # new
  # init
  ```

- class를 수정

  ```python
  Class Flight:
      
      def __init__(self, number):
          self._number = number
          
      def number(self):
          return self._number
  ```

  ```python
  f = Flight(5)
  f.number()
  # 5
  
  f._number()
  # 5
  ```

- python은 기본적으로 다른 언어에 존재하는 접근제어자(public, private, protected)가 없음

- 기본적으로 모두 Public



