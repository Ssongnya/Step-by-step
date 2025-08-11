# Queue의 종류

## 선형 Queue

### 선형 큐의 특징

1. 1차원 리스트를 이용한 큐
- 큐의 크기 = 리스트 크기
- **front** : 저장된 첫 번째 원소의 인덱스
- **rear** : 저장된 마지막 원소의 인덱스

2. 상태 표현
- 초기 상태 : **front = rear = -1**
- 공백 상태 : **front = rear**
- 포화 상태 : **rear = n-1**(n : 리스트의 크기, n-1 : 리스트의 마지막 인덱스)

--- 

### 선형 큐의 구현

#### 1. 초기 createQueue()

#### 초기 공백큐 생성
- 크기 n인 1차원 리스트 생성
- front, rear = -1 로 초기화

#### 2. enQueue(item)

#### 삽입 : enQueue(item)

마지막 원소 뒤에 새로운 원소를 삽입하기 위해
1) rear 값을 하나 증가시켜 새로운 원소를 삽입할 자리를 마련함
2) 그 인덱스에 해당하는 리스트원소 `Q[rear]`에 item을 저장

```python
def enQueue(item):
  global rear
  if isFull():
    print("Queue_Full")
  else:
    rear += 1
    Q[rear] = item
```

#### 3. deQueue

#### 삭제 : deQueue()

가장 앞에 있는 원소를 삭제하기 위해
1) front 값을 하나 증가시켜 큐에 남아있는 첫 번째 원소로 이동함
2) 새로운 첫 번째 원소를 리턴함으로써 삭제와 동일한 기능을 함

```python
def deQueue():
  global front
  if isEmpty():
    print("Queue_Empty")
  else:
    front += 1
    return Q[front]
```

#### 4. isEmpty(), isFull()

#### 공백상태 및 포화상태 검사 : isEmpty(), isFull()

- 공백 상태 : `front = rear`
- 포화 상태 : `rear = n - 1` (n : 리스트의 크기, n - 1 : 리스트의 마지막 인덱스)

```python
def isEmpty():
  return front == rear

def isFull():
  return rear == len(Q) - 1
```

#### 5. Qpeek()

#### 검색 : Qpeek()
- 가장 앞에 있는 원소를 검색하여 반환하는 연산
- 현재 front의 한자리 뒤(front+1)에 있는 원소,   
  즉, 큐의 첫 번째에 있는 원소를 반환

```python
def Qpeek():
  if isEmpty():
    print("Queue_Empty")
  else :
    return Q[front+1]
```
---

### 선형 큐의 문제점 : 잘못된 포화 상태 인식!

리스트의 크기를 고정 → 사용할 큐의 크기만큼을 미리 확보 → 메모리의 낭비 발생

1) 삽입, 삭제를 계속할 경우 리스트의 앞부분에 활용할 수 있는 공간이 있음에도, `rear = n-1`인 상태, 즉, **포화 상태로 인식**

2) 더 이상의 삽입을 수행할 수 없음

|장점|단점|
|---|----|
|삽입, 삭제의 처리 속도가 빠름|메모리 낭비가 심함|

#### 선형 큐의 단점 해결 방법

- 원형 큐 사용으로 메모리 절약
- 파이썬의 리스트 특성을 사용한 큐 사용으로 메모리 절약
  - 단점 : 삽입, 삭제 시 복사, 데이터 이동시키는 연산 수행에 많은 시간 소모
- 단순연결 리스트로 구현한 큐 사용으로 메모리 동적 확보
- 큐 라이브 사용
---

## 원형 Queue

### 원형 큐

1차원 리스트를 사용하되, 논리적으로 리스트의 처음과 끝이 연결되어 원형형태의 큐를 이룬다고 가정하고 사용한다.

### 원형 큐의 특징

1. 초기 공백 상태
  - front = rear = 0

2. Index의 순환
  - front와 rear의 위치가 리스트의 마지막 인덱스인 `n-1`을 가리킨 후, 논리적 순환을 이루어 리스트의 처음 인덱스인 0으로 이동해야 함
  - 이를 위해 나머지 연산자 %를 사용

3. front 변수
  - 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠

4. 삽입 위치 및 삭제 위치

|테이블 인덱스|삽입 위치|삭제 위치|
|-----------|--------|--------|
|선형 큐|`rear = rear + 1`|`front = front + 1`|
|원형 큐|`rear = (rear + 1) % n`|`front = (front + 1) % n`|

### 원형 큐의 기본 연산 과정

1) 큐 생성 : createQueue() 
    - `Q[0]`이 front 이자 rear
2) 원소 A 삽입 : enQueue(A) 
    - `Q[0]`: fornt, `Q[1]` : A, rear
3) 원소 B 삽입 : enQueue(B)
    - `Q[0]`: front, `Q[1]` : A, `Q[2]` : B, rear
4) 원소 반환/삭제 : deQueue() - front 였던 A가 반환/삭제 되고, rear 였던 B만 남는다
5) 큐 생성(createQueue) - A삭제 후 새로운 큐 정의
    - `Q[1]` : front, `Q[2]` : B, rear
6) 원소 C 삽입 : enQueue(C)
    - `Q[1]` : front, `Q[2]` : B, `Q[3]` : C, rear
7) 원소 D 삽입 : enQueue(D)
    - `Q[1]` : front, `Q[2]` : B, `Q[3]` : C, `Q[4]` : D, rear
    - Queue는 full

### 원형 큐의 구현

#### 1. 초기 createQueue()

#### 초기 공백큐 생성

- 크기 n인 1차원 리스트 생성
- `front, rear = 0` 으로 초기화

#### 2. isEmpty(), isFull()

#### 공백상태 및 포화상태 검사 : isEmpty(), isFull()

- 공백상태 : front = rear
- 포화상태 : 삽입할 rear의 다음 위치 = 현재 front
- `(rear + 1) % n = front`

```python
def isEmpty():
  return front == rear

def isFull():
  return (rear+1) % len(cQ) == front
```

#### 3. enQueue(item)

#### 삽입 : enQueue(item)

마지막 원소 뒤에 새로운 원소를 삽입하기 위해
1) rear 값을 조정하여 새로운 원소를 삽입할 자리를 마련함 :   
`rear <- (rear + 1) % n`
2) 인덱스에 해당하는 리스트 원소 `cQ[rear]`에 item을 저장

```python
def enQueue(item):
  global rear
  if isFull():
    print("Queue_Full")
  else :
    rear = (rear + 1) % len(cQ)
    cQ[rear] = item
```

#### 4. deQueue

#### 삭제 : deQueue(), delete()

가장 앞에 있는 원소를 삭제하기 위해
1) front 값을 조정하여 삭제할 자리를 준비함
2) 새로운 front 원소를 리턴함으로써 삭제와 동일한 기능을 함

```python
def deQueue():
  global front
  if isEmpty():
    print("Queue_Empty")
  else :
    front = (front + 1) % len(cQ)
    return cQ[front]

def delete():
  global front
  if isEmpty():
    print("Queue_Empty")
  else:
    front = (front + 1) % len(cQ)
```

    