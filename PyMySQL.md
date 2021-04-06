# PyMySQL

- [Document](https://pymysql.readthedocs.io/en/latest/modules/connections.html)

- Python에서 MySQL 연동하기

  ```bash
  $ pip install pymysql
  ```

- import

  ```python
  import pymysql
  ```

## 1. 연결

```python
conn = pymysql.connect(
	# 연결될 db 옵션
)
cursor = conn.cursor(pymysql.cursors.DictCursor)
```

- 연결 옵션
  - `host` : 호스트 네임 or ip 주소
  - `user` : mysql id
  - `password` 
  - `database` : database 명
  - `port` : 포트(숫자)
  - `charset` : 'utf8'
  - `read_timeout` : 읽기 타임아웃 시킬 시간 (초 단위)
  - `write_timeout` : 쓰기 타임아웃 시킬 시간 (초 단위)

- 커서

  - 커서의 옵션을 DictCurosr로 주면 컬럼: 값으로 매핑시킨 결과를 얻을 수 있음

- 커넥션이 끊길 경우

  ```python
  conn.open # 커넥션이 열려있는지 확인 아니면 False
  
  conn.ping(reconnect=True) 
  ```

- 커넥션을 사용한 후 반환

  ```python
  conn.close()
  ```

## 2. 실행

```python
sql = 'select * from table'
cursor.execute(sql)

result = cursor.fetchone()
```

- `execute` : sql을 실행
- 데이터 읽기 관련

  - `fetchone()`
  - `fetchall()`

- 데이터 쓰기 관련
  - `commit()` : insert나 update `execute()` 사용시 `commit()`을 사용해야 데이터가 들어감