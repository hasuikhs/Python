# TinyDB

- Python에서 간단히 사용 가능한 NO-SQL 패키지

## 1. 설치

```bash
$ pip install tinydb
```

## 2. 기본 사용법

- 테스트를 한다고 파일명을 `tinyDb.py` 로 지정하면 모듈 에러가 나므로 사용해선 안됨
- 패키지 import

```python
from tinydb import TinyDB, Query
```

### 2.1 DB 생성

- db를 조회해서 없으면 생성됨

```python
db = TinyDB('db.json')
```

### 2.2 CRUD

#### 2.2.1 Insert

```python
db.insert({'count': 7, 'type': 'apple'})
db.insert({'count': 4, 'type': 'banana'})
```

#### 2.2.2 Search

```python
# 모든 document 조회
db.all()

# for문으로 돌면서 출력
for item in db:
    print(item)
```

- 일반 search

  ```python
  apple = db.search(Query().type == 'apple')
  over_five = db.search(Query().count > 5)
  
  # 복합 조건 and는 & or는 |
  over_five_apple = db.search(Query().type == 'apple' & Query().count > 5)
  ```

#### 2.2.3 Update

```python
db.update({'count': 6}, Query().type == 'apple')
```

#### 2.2.4 Delete

```python
db.remove(Query().type == 'apple')

# 모든 document delete
db.truncate()
```



