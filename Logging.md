# Logging

- 로깅은 프로그램이 실행될 때 발생하는 이벤트를 추적하는 수단
- 이벤트는 선택적으로 가변 데이터를 포함할 수 있는 설명 메시지로 기술
- 이벤트는 각각의 중요도를 가짐

- 로깅은 일일이 코드 상에 `print()`를 사용하는 것보다 자세하게 인지 가능

## 1. Logging 인스턴스 생성

```python
import logging

def get_logger():
    logger = logging.getLogger('logger_name')
```

- `logger_name`을 적지 않으면 `root`로 생성됨

## 2. Logging 레벨

- 특정 레벨을 설정하면, 그 레벨 이상의 로깅만 출력함

- 따로 설정하지 않으면 기본 레벨은 WARNING으로 지정되어 있음

  | Level    | 설명                                                         |
  | -------- | ------------------------------------------------------------ |
  | DEBUG    | 상세한 정보, 보통 개발 단계에서 사용                         |
  | INFO     | 예상대로 작동하는지 확인                                     |
  | WARNING  | 예상치 못한 일이 발생했거나 가까운 미래에 발생할 문제에 대한 표시<br>프로그램은 여전히 예상대로 작동 중 |
  | ERROR    | 더욱 심각한 문제로 인해, 프로그램이 일부 기능을 수행하지 못 함 |
  | CRITICAL | 심각한 에러, 프로그램 자체가 계속 실행되지 않을 수 있음      |

  ```python
  logger.setLevel(logging.INFO) # INFO 이상의 레벨을 출력
  ```

## 3. Logging 포멧

- 로깅 메시지 커스터마이징

```python
formatter = logging.Formatter(
	'%(asctime)s [%(levelname)-8s] %(module)s.%(funcName)s:%(lineno)-3s # %(message)s'
)
```

| 이름            | 포멧                  | 설명                                                         |
| --------------- | --------------------- | ------------------------------------------------------------ |
| args            | 직접 포멧할 필요 없음 | `message`를 생성하기 위해 `msg`에 병합되는 인자              |
| asctime         | `%(asctime)s`         | log가 생성된 시간, 기본적으로 <2021-01-01 00:00:00,000> 형식 |
| created         | `%(created)f`         | log가 생성된 시간, `time.time()`                             |
| exc_info        | 직접 포멧할 필요 없음 | 예외 튜플 또는, 예외가 발생하지 않았다면, `None`             |
| filename        | `%(filename)s`        | `pathname`의 파일명 부분                                     |
| funcName        | `%(funcName)s`        | log 호출을 포함하는 함수의 이름                              |
| levelname       | `%(levelname)s`       | log의 수준                                                   |
| levelno         | `%(levelno)s`         | log의 숫자 수준                                              |
| lineno          | `%(lineno)d`          | log 호출이 일어난 소스 행 번호                               |
| message         | `%(message)s`         | log 된 메시지                                                |
| module          | `%(module)s`          | 모듈(filename의 이름 부분)                                   |
| msecs           | `%(msec)d`            | log가 생성된 시간의 밀리 초 부분                             |
| msg             | 직접 포멧할 필요 없음 | 원래 log 호출에서 전달된 포멧 문자열                         |
| name            | `%(name)s`            | log 호출에 사용된 로거의 이름                                |
| pathname        | `%(pathname)s`        | log 호출이 일어난 소스 파일의 전체 경로명                    |
| process         | `%(process)d`         | 프로세스 ID                                                  |
| processName     | `%(processName)s`     | 프로세스 명                                                  |
| relativeCreated | `%(relativeCreated)d` | log 모듈이 로드된 시간을 기준으로 log가 생성된 시간          |
| stack_info      | 직접 포멧할 필요 없음 | 현재 스레드의 스택 바닥에서<bR> 이 레코드를 생성한 로깅 호출의 스택 프레임까지의 스택 프레임 정보 |
| thread          | `%(thread)d`          | 스레드 ID                                                    |
| threadName      | `%(threadName)s`      | 스레드 명                                                    |

## 4. 핸들러 설정

- 핸들러는 log 메시지를 지정된 대상으로 전달하는 역할을 함

- 로거 객체는 `addHandler` 메서드를 사용해 0개 이상의 핸들러를 자신에게 추가할 수 있음

  - `StreamHandler` : 스트림(터미널과 같은 콘솔창 등)에 log 메시지를 보냄
  - `FileHandler` : 특정 파일에 log 메시지를 보내 저장시킴

  ```python
  stream_handler = logging.StreamHandler()
  stream_handler.setFormatter(formatter)
  logger.addHandler(stream_handler)
  ```

## 5. 예

```python
import logging

def get_logger():
    logger = logging.getLogger()
    
    formatter = logging.Formatter(
		'%(asctime)s [%(levelname)-8s] %(module)s.%(funcName)s:%(lineno)-3s # %(message)s'
	)
    
    stream_handler = logging.StreamHandler()
	stream_handler.setFormatter(formatter)
	logger.addHandler(stream_handler)
    
    logger.setLevel(logging.INFO)\
    
    return logger

logger = get_logger()

logger.info('test')
```

