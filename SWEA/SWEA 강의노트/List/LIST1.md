# List1

## 알고리즘 기초 & 성능 분석

### 알고리즘이란?

문제를 해결하기 위한 유한한 절차나 방법.컴퓨터가 일을 수행하기 위한 단계적인 방법을 뜻한다.

예) 1부터 100까지의 합 구하기

- 방법 1: `1 + 2 + 3 + … + 100` → 반복문으로 계산
- 방법 2: `(1 + 100) * 50 = 5050` → 공식 이용

같은 문제여도 접근 방법에 따라 효율이 확 달라진다.

### 알고리즘 표현 방법

1. **슈도코드**   
실제 프로그래밍 언어는 아니지만, 로직을 코드처럼 흉내 내서 표현. 실행은 안 되지만 설계할 때 유용함.
    
    ```
    sum ← 0
    for i from 1 to 100:
        sum ← sum + i
    print sum
    ```
    
2. **순서도**   
프로그램 흐름을 도식화한 그림. 복잡한 알고리즘을 한눈에 보기 좋음.

### 알고리즘 성능 분석

좋은 알고리즘의 기준

- 정확성: 제대로 동작하는가?
- 작업량: 연산 횟수가 적은가?
- 메모리 사용량: 메모리를 덜 쓰는가?
- 단순성: 이해하기 쉽고 단순한가?
- 최적성: 더 개선할 여지가 없는가?

결국 성능 비교는 **연산 횟수**를 많이 본다.

### 시간 복잡도 (Big-O 표기법)

알고리즘이 입력 크기 `n`에 따라 걸리는 시간을 수학적으로 표현.

| 표기 | 설명 | 예시 |
| --- | --- | --- |
| O(1) | 상수 시간 | 배열 첫 원소 |
| O(log n) | 로그 시간 | 이진 탐색 |
| O(n) | 선형 시간 | 리스트 순회 |
| O(n²) | 이차 시간 | 버블 정렬 |

### 코드 비교

```python
# 방법 1: 반복문으로 합 구하기 (O(n))
def sum_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# 방법 2: 공식으로 합 구하기 (O(1))
def sum_formula(n):
    return n * (n + 1) // 2

print(sum_loop(100))     # 출력: 5050
print(sum_formula(100))  # 출력: 5050
```

실행 결과는 같지만, 반복문은 100번 돌고 공식은 딱 한 번 계산한다. → 공식이 훨씬 효율적임.

## Exhaustive Search & Baby-gin & Permutation

### Exhaustive Search (완전 검색)

문제를 풀 때 가능한 모든 경우의 수를 전부 시도해보는 방법.

- Brute-force(무식한 방법)라고도 불림.
- 경우의 수가 적을 때 유용함.
- 느리지만 답을 못 찾을 가능성이 거의 없음.
- 보통 처음엔 완전 검색으로 풀어서 답을 확인한 후, 더 좋은 알고리즘으로 개선하기도 함.

### Baby-gin 게임

**문제 조건**

- 0~9 사이 숫자 카드 6장.
- **run**: 연속된 숫자 3개 (예: 456)
- **triplet**: 같은 숫자 3개 (예: 777)
- 6장이 run과 triplet으로만 구성되면 baby-gin.

예시

1. 667767 → 666, 777 → baby-gin
2. 054060 → 456, 000 → baby-gin
3. 101123 → 111, 023 → 023은 run 아님 → baby-gin 아님

### 완전 검색으로 Baby-gin 판단

모든 경우를 시도해서 baby-gin인지 확인하기.

```python
from itertools import permutations

# run이나 triplet인지 체크하는 함수
def check_run_or_triplet(seq):
    if seq[0] == seq[1] == seq[2]:  # triplet
        return True
    if seq[0] + 1 == seq[1] and seq[1] + 1 == seq[2]:  # run
        return True
    return False

def is_baby_gin(numbers):
    for perm in permutations(numbers):  # 모든 순열 생성
        first, second = perm[:3], perm[3:]  # 앞 3자리, 뒤 3자리 나누기

        if check_run_or_triplet(first) and check_run_or_triplet(second):
            return True
    return False

print(is_baby_gin([6, 6, 7, 7, 6, 7]))  # 출력: True
print(is_baby_gin([0, 5, 4, 0, 6, 0]))  # 출력: True
print(is_baby_gin([1, 0, 1, 1, 2, 3]))  # 출력: False
```

✅ 완전 검색은 확실히 답을 찾지만 경우의 수가 많아질수록 느려짐.

### 순열(Permutation)

서로 다른 n개의 원소 중에서 r개를 골라 순서를 고려하여 나열하는 것.

예: {1, 2, 3}의 모든 순열→ 123, 132, 213, 231, 312, 321

파이썬 코드로 구현해봄:

```python
from itertools import permutations

nums = [1, 2, 3]
for p in permutations(nums):
    print(p)

# 출력:
# (1, 2, 3)
# (1, 3, 2)
# (2, 1, 3)
# (2, 3, 1)
# (3, 1, 2)
# (3, 2, 1)
```

### 1️⃣ 순열 함수 (백트래킹)

`itertools` 없이 직접 구현.

```python
def my_permutations(arr, r):
    result = []

    def backtrack(path, used):
        if len(path) == r:
            result.append(path[:])
            return

        for i in range(len(arr)):
            if not used[i]:
                used[i] = True
                path.append(arr[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

    backtrack([], [False] * len(arr))
    return result

# 테스트
print(my_permutations([1, 2, 3], 3))
# 출력: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

### 2️⃣ run/triplet 체크 함수

중첩 함수 없이 따로 정의.

```python
def check_run_or_triplet(seq):
    if seq[0] == seq[1] == seq[2]:  # triplet
        return True
    if seq[0] + 1 == seq[1] and seq[1] + 1 == seq[2]:  # run
        return True
    return False
```

### 3️⃣ Baby-gin 판별 함수

순열 함수를 이용해서 모든 경우의 수 탐색.

```python
def is_baby_gin(numbers):
    # numbers에서 만들 수 있는 모든 6자리 순열 생성
    for perm in my_permutations(numbers, 6):
        first, second = perm[:3], perm[3:]  # 앞 3자리, 뒤 3자리 분리
        if check_run_or_triplet(first) and check_run_or_triplet(second):
            return True
    return False

# 테스트
print(is_baby_gin([6, 6, 7, 7, 6, 7]))  # 출력: True (666, 777)
print(is_baby_gin([0, 5, 4, 0, 6, 0]))  # 출력: True (000, 456)
print(is_baby_gin([1, 0, 1, 1, 2, 3]))  # 출력: False
```

### 출력

```
True
True
False
```

## 탐욕 알고리즘(Greedy) + Baby-gin

### 탐욕 알고리즘(Greedy) 개념

- 매 순간 **가장 좋아 보이는 선택**을 하는 알고리즘.
- 부분적으로는 최적일 수 있지만, 전체적으로 항상 최적이라는 보장은 없음.
- 구현이 간단하고 빠름.

### Baby-gin 탐욕 알고리즘 접근

아이디어:

1. 숫자들을 정렬.
2. 앞에서부터 `triplet` 먼저 체크 → 있으면 제거.
3. 없으면 `run` 체크 → 있으면 제거.
4. 두 번 반복해서 다 제거되면 baby-gin.

### 코드 구현

```python
def is_baby_gin_greedy(numbers):
    # 0~9 숫자의 개수를 세는 카운팅 배열
    c = [0] * 10
    for num in numbers:
        c[num] += 1

    tri = 0  # triplet 개수
    run = 0  # run 개수
    i = 0

    while i < 10:
        # 1. triplet 검사
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue  # 같은 위치 다시 검사 (중복 triplet 방지)

        # 2. run 검사
        if i <= 7 and c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:
            c[i] -= 1
            c[i + 1] -= 1
            c[i + 2] -= 1
            run += 1
            continue  # 같은 위치 다시 검사 (중복 run 방지)

        i += 1  # 다음 숫자로 이동

    return run + tri == 2  # run 2개 or triplet 2개 or run+triplet 조합
```

### 테스트

```python
print(is_baby_gin_greedy([6, 6, 7, 7, 6, 7]))  # 출력: True
print(is_baby_gin_greedy([0, 5, 4, 0, 6, 0]))  # 출력: True
print(is_baby_gin_greedy([1, 0, 1, 1, 2, 3]))  # 출력: False
```

### 출력

```
True
True
False
```

### 완전 탐색 vs 탐욕 알고리즘

| 구분 | 완전 탐색 | 탐욕 알고리즘 |
| --- | --- | --- |
| 정확도 | 100% 확실 | 일부 케이스 실패 가능성 있음 |
| 속도 | 느림 (모든 경우 탐색) | 빠름 (정렬 후 단순 탐색) |
| 구현 난이도 | 다소 복잡 | 간단함 |

## 정렬(Sort) 알고리즘

### 정렬(Sort)이란?

- 데이터들을 **특정 기준**에 따라 재배열하는 과정.
- 주로 오름차순(작은 → 큰) 또는 내림차순(큰 → 작은)으로 정렬.
- 검색, 탐색, 데이터 분석 전처리 과정에서 자주 활용됨.

## 1️⃣ 버블 정렬 (Bubble Sort)

인접한 두 데이터를 비교하고, 잘못된 순서라면 서로 위치를 교환하면서 정렬하는 방법.큰 값이 거품처럼 맨 뒤로 "올라간다"는 느낌이라 **버블 정렬**이라고 부른다.

### 버블 정렬 예시 (직접 손으로 정렬하기)

초기 데이터:`[55, 7, 78, 12, 42]`

1️⃣ 1회전

- 55와 7 비교 → 교환 → `[7, 55, 78, 12, 42]`
- 55와 78 비교 → 그대로
- 78과 12 비교 → 교환 → `[7, 55, 12, 78, 42]`
- 78과 42 비교 → 교환 → `[7, 55, 12, 42, 78]`

→ 가장 큰 값 78이 맨 뒤로 이동!

2️⃣ 2회전

- `[7, 55, 12, 42]`만 비교
- 55와 12 비교 → 교환 → `[7, 12, 55, 42, 78]`
- 55와 42 비교 → 교환 → `[7, 12, 42, 55, 78]`

3️⃣ 3회전

- `[7, 12, 42, 55, 78]` → 이미 정렬 완료

### 버블 정렬 코드

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # 전체 회전
        for j in range(n - 1 - i):  # 인접 비교
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

nums = [55, 7, 78, 12, 42]
print(bubble_sort(nums))  # 출력: [7, 12, 42, 55, 78]
```

### 버블 정렬 특징

- 장점: 구현이 단순하다.
- 단점: 비교와 교환이 많아서 **O(n²)** 시간 복잡도를 가진다.
- 데이터가 적을 때만 실용적.

## 2️⃣ 카운팅 정렬 (Counting Sort)

**정수형 데이터**를 빠르게 정렬하는 알고리즘.비교 없이 "숫자의 개수"를 세서 정렬한다.

### 카운팅 정렬 예시

데이터: `[0, 4, 1, 3, 1, 2, 4, 1]`

1️⃣ 각 숫자 개수 세기

```
숫자:    0  1  2  3  4
개수:    1  3  1  1  2
```

2️⃣ 개수만큼 순서대로 나열

- 0 → 1번
- 1 → 3번
- 2 → 1번
- 3 → 1번
- 4 → 2번

결과: `[0, 1, 1, 1, 2, 3, 4, 4]`

### 카운팅 정렬 코드

```python
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    # 1. 각 숫자의 등장 횟수 세기
    for num in arr:
        count[num] += 1

    # 2. 정렬된 결과 생성
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr

nums = [0, 4, 1, 3, 1, 2, 4, 1]
print(counting_sort(nums))  # 출력: [0, 1, 1, 1, 2, 3, 4, 4]
```

### 카운팅 정렬 특징

- 장점: 매우 빠르다 → **O(n + k)**
- 단점: 숫자의 범위(k)가 너무 크면 비효율적 (메모리 낭비)
- 문자열, 실수 정렬 불가 (정수만 가능)

### 오늘 배운 점

- **버블 정렬**은 간단하지만 느림 (O(n²)).
- **카운팅 정렬**은 숫자 범위가 제한적일 때 강력함.
- 데이터의 특성을 고려해서 정렬 알고리즘을 선택해야 함.
- 정렬 과정은 직접 손으로 시뮬레이션해보면 더 잘 이해됨.