# Python Module

- Python은 모듈을 만드는 방법이 다른 언어와 조금은 다름

#### 프로젝트 구조

- 간단한 프로젝트 구조

```
project ┬ module ┬ __init__.py
        │       └ cat.py
        └ main.py
```

##### `project/module/cat.py`

```python
class Cat:
    def __init__(self, name):
        self.name = name
```

##### `project/class/__init__.py`

- Python은 모듈화 시킬 폴더에서 `__init__.py` 파일을 생성해야 함

```python
from .cat import Cat	// .은 현재 위치의 cat 파일의 Cat을 불러와라
```

##### `project/main.py`

```python
from module import Cat
```

