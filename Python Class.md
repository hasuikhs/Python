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
          return 'FL902'
  ```

- 인스턴스 메소드 접근

  ```python
  f= Flight()
  f.number()
  # 'FL902'
  ```

  - Python method의 첫번째 parameter는 관례적으로 self를 사용

  - 호출 시 호출한 객체 자신이 전달되기 때문에 self라는이름을 사용

  - 이를 사용하여 class에서 바로 method로 접근하면서 위에서 할당한 Flight의 인스턴스 f를 parameter로 전달함으로써 똑같은 결과값을 얻음

    ```python
    Flight.number(f)
    # FL902
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
          return 'FL902'
  ```

- 다시 인스턴스를 생성해보면

  ```python
  f = Flight()
  
  # new
  # init
  ```

- class를 수정하여 `__new__` 제거

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

### 2.3 초기화자(`__init__`)에 객체의 불변성을 확립(유효성 검증)

- 일반적으로 초기화자(`__init__`)에서 인스턴스의 불변성을 확립하는 것이 좋음

- 인스턴스 생성시 들어올 값에 대하여 `__init__`에서 validation 수행

- 비행기 번호는 앞에 두글자는 영문자와 대문자, 뒤의 숫자는 양의 정수

- 위의 조건으로 class를 변경하면 인스턴스 생성시 규칙에 맞지 않는 값이 들어오면 ValueError 발생

  ```python
  class Flight:
      
      def __init__(self, number):
          if not number[:2].isalpha():
              raise ValueError('첫 두글자가 알파벳이 아님')
          if not number[:2].isupper():
              raise ValueError('첫 두글자가 대문자가 아님')
          if not number[2:].isdigit():
              raise ValueError('세번째 글자 이상이 양의 숫자가 아님')
          self._number = number
  ```

### 2.4 비공개 속성

- 위의 예처럼 `_` 언더바 한개는 내부적으로만 사용되는 변수라고 알리지만, 사실 값도 얻어올 수 있고 할당도 가능

  ```python
  f = Flight("FL902")
  f._number
  # 'FL902'
  
  f.number = 'abc'
  f.number()
  # abc
  ```

- 원칙적으로 접근을 막으려면 `__` 언더바 두개를 사용

  ```python
  class Flight:
      
      def __init__(self, number):
          if not number[:2].isalpha():
              raise ValueError('첫 두글자가 알파벳이 아님')
          if not number[:2].isupper():
              raise ValueError('첫 두글자가 대문자가 아님')
          if not number[2:].isdigit():
              raise ValueError('세번째 글자 이상이 양의 숫자가 아님')
          self.__number = number
          
      def number(self):
          return self.__number
  ```

- `number()` 인스턴스 method를 통해 내부에서는 접근 가능하나 인스턴스 `f`의 속성으로 접근시 에러 발생

  ```python
  f = Flight('FL902')
  f.number()
  # FL902
  
  f.__number
  # error
  ```

### 2.5 오버로딩

- python은 method 오버로딩이 없음
- 만약 같은 이름의 method가 있다면 나중에 선언된 method 실행

