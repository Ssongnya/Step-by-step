# Bootstrap Grid system

### Bootstrap Grid system

웹 페이지의 <u>레이아웃</u>을 조정하는 데 사용되는 **12개의 컬럼**으로 구성된 시스템

> 반응형 디자인을 지원해 웹 페이지를 모바일, 태블릿, 데스크탑 등 다양한 기기에서 적절하게 표시할 수 있도록 도와준다.

> 레이아웃   
>   
> 각 요소의 위치와 크기를 조정하여 웹 페이지의 디자인을 결정하는 것

### 반응형 웹 디자인

디바이스 종류나 화면 크기에 상관없이, 어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술

> 32인치 모니터, 태블릿, 스마트폰 등, 화면 크기에 따라 요소의 배치를 변경하여 일관된 사용자 경험을 제공할 수 있다.

### 12개의 컬럼 사용 예시

#### 구글 뉴스

12칸 중 크기에 따라 필요한 만큼의 컬럼을 차지하게 요소를 배치

-> 내부의 요소도 12칸으로 나눠서 활용

## Grid system 구조

### Grid system 기본 요소

#### Container

Column들을 담고 있는 공간

#### Column

실제 컨텐츠를 포함하는 부분

#### Gutter

컬럼과 컬럼 사이의 여백 영역(상하좌우)

#### 1개의 row안에 12개의 column영역이 구성

각 요소는 12개 중 몇 개를 차지할 것인지 지정됨

## Grid system 실습

```css
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
  <style>
    .box {
      border: 1px solid black;
      background-color: lightblue;
      text-align: center;
    }
  </style>
</head>

<body>
  <h2 class="text-center">Basic</h2>
  <div class="container">
    <div class="row">
      <div class="col">
        <div class="box">col</div>
      </div>
      <div class="col">
        <div class="box">col</div>
      </div>
      <div class="col">
        <div class="box">col</div>
      </div>
    </div>
    <div class="row">
      <div class="col-4">
        <div class="box">col-4</div>
      </div>
      <div class="col-4">
        <div class="box">col-4</div>
      </div>
      <div class="col-4">
        <div class="box">col-4</div>
      </div>
    </div>
    <div class="row">
      <div class="col-2">
        <div class="box">col-2</div>
      </div>
      <div class="col-8">
        <div class="box">col-8</div>
      </div>
      <div class="col-2">
        <div class="box">col-2</div>
      </div>
    </div>
  </div>
<body>
```

### Grid system 실습 - 중첩(Nestig)

- 하나의 column에 또다른 row를 넣기
- nesting은 바깥 col 안에 새로운 row를 만들고, 다시 12칸 체계로 col을 배치하는 것
    - 내부 col의 비율은 “바깥 col의 크기”와는 무관하고, “자신이 속한 row의 12칸”만 따름

```css
  <h2 class="text-center">Nesting</h2>
  <div class="container">
    <div class="row">
      <div class="col-4 box">
        <div>col-4</div>
      </div>
      <div class="col-8 box">
        <div class="row">
          <div class="col-6">
            <div class="box">col-6</div>
          </div>
          <div class="col-6">
            <div class="box">col-6</div>
          </div>
          <div class="col-6">
            <div class="box">col-6</div>
          </div>
          <div class="col-6">
            <div class="box">col-6</div>
          </div>
        </div>
      </div>
    </div>
  </div>
  ```

#### `col-6`가 두 줄씩 쌓이는 원리
- 원리 ①: Bootstrap의 12칸 규칙
    - Bootstrap의 .row 안에서는 항상 **12칸(grid)**을 기준으로 나눠짐
    - col-6은 그 중 6칸 차지 → 즉, 화면 가로폭의 50%를 차지
    - 따라서 col-6 + col-6 = 12 → 한 줄이 꽉 찼다고 판단
    - 그 다음 col-6이 또 나오면 자동으로 줄바꿈되어 새로운 행에서 다시 배치
  
### Grid system 실습 - 상쇄(Offset)

- Offset으로 Column을 생략하기
- offset은 간단히 말하면, 열(col) 앞에 빈 공간을 강제로 만들어서 위치를 조정

#### 동작 원리

col-4 → 첫 칸에서 4칸 차지
col-3 offset-3 → 앞에 3칸 비워두고(col-3 offset-3), 그다음에 3칸 차지
offset = 왼쪽에 투명한 col-N을 미리 넣는 것이라고 생각

즉, 12칸 중 배치 결과는 이렇게 돼요:

```css
[■■■■][□□□][■■■][□□□]
```
■ = 실제 column
□ = offset(빈칸)

### Gutter

Grid system에서 column 사이에 여백 영역

x축은 padding, y축은 margin으로 여백 생성

### Grid system실습 - gutters

- 컬럼(col) 사이에 생기는 간격
    - 즉, col과 col 사이에 "숨겨진 여백"이라고 생각하면 됩니다.
    - 실제로는, gutter는 padding으로 구현돼 있다.
    - margin으로 가로로는 밀 수 없는 이유!

- Gutter를 이용해 가로 간격 조정
    - gx-0
    - col 사이 여백 제거
```css
  <h2 class="text-center">Gutters(gx-0)</h2>
  <div class="container">
    <div class="row gx-0">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>
```

- Gutter를 이용해 세로 간격 조정
    - gy-5
    - row 사이 여백 증가
```css
  <h2 class="text-center">Gutters(gy-5)</h2>
  <div class="container">
    <div class="row gy-5">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>
```

- Gutter를 이용해 가로/세로 간격 조정
    - g-5

```css
  <h2 class="text-center">Gutters(g-5)</h2>
  <div class="container">
    <div class="row g-5">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>
```


## Grid system for responsive web

### 반응형 웹 디자인

**Responsive Web Design**

디바이스 종류나 화면 크기에 상관없이, 어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술

- Bootstrap grid system에서는 12개의 column과 **6개의 breakpoints**를 사용하여 반응형 웹 디자인을 구현

## Grid system Breakpoints

웹 페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점
  - 화면 너비에 따라 6개의 분기점 제공(xs, sm, md, lg, xl, xxl)

각 breakpoints마다 설정된 최대 너비 값 **"이상으로"** 화면이 커지면 grid system 동작이 변경됨

| 구분              | xs        | sm         | md         | lg         | xl         | xxl         |
| --------------- | --------- | ---------- | ---------- | ---------- | ---------- | ----------- |
| 최소 화면 크기        | `<576px`  | `≥576px`   | `≥768px`   | `≥992px`   | `≥1200px`  | `≥1400px`   |
| Container 최대 너비 | auto (없음) | 540px      | 720px      | 960px      | 1140px     | 1320px      |
| Class prefix    | `.col-`   | `.col-sm-` | `.col-md-` | `.col-lg-` | `.col-xl-` | `.col-xxl-` |


## Break points 실습

### breakpoints 실습

- 화면 사이즈가 변함에 따라 column의 배치 바꾸기
```css
  <h2 class="text-center">Breakpoints</h2>
  <div class="container">
    <div class="row">
      <div class="col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-6 col-md-8 col-lg-3 col-xl-4">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-6 col-md-2 col-lg-3 col-xl-12">
        <div class="box">col</div>
      </div>
    </div>
  </div>
```

### breakpoints 실습 (offset 활용)

```css
  <h2 class="text-center">Breakpoints + offset</h2>
  <div class="container">
    <div class="row g-4">
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-4 offset-sm-4 col-md-6 offset-md-0">
        <div class="box">col</div>
      </div>
    </div>
  </div>
```

## CSS Layout 종합 정리

| 구분      | Grid system       | Flexbox        | Position  |
| ------- | ----------------- | -------------- | --------- |
| 레이아웃 단위 | 2차원 (행+열)         | 1차원 (행 또는 열)   | 개별 좌표 기반  |
| 장점      | 복잡한 레이아웃, 반응형에 강함 | 유연한 정렬, 간단한 구조 | 정밀한 위치 제어 |
| 활용 예시   | 전체 페이지, 대시보드      | 메뉴, 버튼 그룹      | 모달, 고정 배너 |


### 1. Grid System
📌 **언제 쓰나? → “페이지 전체 뼈대” 만들 때**

- 웹사이트 전체 레이아웃 : 헤더 / 메인 / 사이드바 / 푸터 같은 큰 구조  
- 대시보드 화면 : 카드나 차트를 행과 열로 정확하게 나눠야 할 때  
- 갤러리/포트폴리오 : 사진을 일정한 격자에 맞춰 배치할 때  
- 반응형 레이아웃 : 화면 크기에 따라 칸 수를 달리해서 보여줄 때  

👉 **큰 판짜기에 적합합니다.**

### 2. Flexbox
📌 **언제 쓰나? → “작은 단위 정렬”할 때**

- 네비게이션 바 : 메뉴 항목을 가로로 나열하고, 가운데 정렬/양쪽 정렬  
- 버튼 그룹 : 버튼 크기를 자동으로 맞춰서 균등 분배  
- 폼 레이아웃 : 입력창과 버튼을 한 줄에 나란히 배치  
- 카드 컴포넌트 내부 : 제목, 설명, 버튼을 세로/가로로 깔끔히 정렬  

👉 **컴포넌트 안의 요소 정렬에 최적화.**


### 3. Position
📌 **언제 쓰나? → “특정 요소를 고정/띄워야 할 때”**

- 고정 헤더/푸터 : 스크롤해도 항상 보이는 상단/하단 바  
- 모달/팝업 : 화면 가운데에 겹쳐서 뜨는 창  
- 툴팁/드롭다운 메뉴 : 버튼을 기준으로 특정 위치에 떠야 할 때  
- 스크롤 따라오는 요소 : 광고 배너, 챗봇 버튼 같은 UI  

👉 **정확한 좌표 제어가 필요할 때 사용.**


#### 🔹 비유하자면
- **Grid** = 건물의 뼈대(층과 방 구조)  
- **Flexbox** = 방 안의 가구 배치  
- **Position** = 벽에 못 박고 시계나 그림 고정하기  


#### ✅ 정리
- **Grid** → 큰 구조, 2차원 레이아웃  
- **Flexbox** → 내부 정렬, 1차원 배치  
- **Position** → 특정 요소 고정/부유  


- CSS 레이아웃 기술들은 각각 고유한 특성과 장단점을 가지고 있음
- 이들은 상호 보완적이며, 특정 상황에 따라 적합한 도구가 달라짐
- 최적의 기술을 선택하고 효과적으로 활용하기 위해서는 다향한 실제 개발 경험이 필수적임

---


# UX & UI

## UX

### UX (User Experience)

제품이나 서비스를 사용하는 사람들이 느끼는 전체적인 경험과 만족도를 개선하고 최적화하기 위한 디자인과 개발 분야

### UX 예시
- 백화점 1층에서 느껴지는 좋은 향수 향기
- 러쉬 매장 근처만 가도 맡을 수 있는 러쉬 향기
- 원하는 음악을 검색할 때, 검색 기능이 적절하게 작동하고 검색 결과가 정확하게 나오는 것

### UX 설계

- 사람들의 마음과 생각을 이해하고 정리해서 제품에 녹여내는 과정
- 유저 리서치, 데이터 설계 및 정제, 유저 시나리오, 프로토타입 설계

## UI

### UI (User Interface)

서비스와 사용자 간의 상호작용을 가능하게 하는 디자인 요소들을 개발하고 구현하는 분야

### UI 에시

- 리모콘
    - 사용자가 버튼을 누르면 TV가 켜지고, 채널을 변경하거나 볼륨을 조절할 수 있음
- ATM 
    - 사용자가 터치스크린을 통해 사용자 정보를 입력하고, 원하는 금액을 선택할 수 있음
- 웹 사이트
    - 사용자가 로그인 버튼을 누르면, 이동하는 화면의 디자인 및 레이아웃

### UI 설계

- 예쁜 디자인보다는 사용자가 더 쉽고 편리하게 사용할 수 있도록 고려
- 이를 위해서는 디자인 시스템, 중간 산출물, 프로토타입 등이 필요

### 디자이너와 기획자 그리고 개발자

- 많은 회사에서 UX/UI 디자인을 함께하는 디자이너를 채용하거나 UX는 기획자, UI는 디자이너의 역할로 채용하기도 함
- UX (직무 : UX Researcher, User Researcher)
    - (구글) 사용자의 경험을 이해하기 위한 통계 모델을 설계
    - (MS) 리서치를 기획하고 사용자에 대한 지표를 정의
    - (Meta) 정성적인 방법과 정량적인 방법을 사용해서 사용자 조사를 실시

- UI (직무 : Product Designer, Interaction Designer)
    - (구글) 다양한 디자인 프로토타이핑 툴을 사용해서 개발 가이드를 제공
    - (MS) 시각 디자인을 고려해서 체계적인 디자인 컨셉을 보여줌
    - (Meta) 제품을 이해하고 더 나은 UI Flow와 사용자 경험을 디자인

# 참고

## The Grid system

- CSS가 아닌 편집 디자인에서 나온 개념으로 구성 요소를 잘 배치해서 시각적으로 좋은 결과물을 만들기 위함
- 기본적으로 안쪽에 있는 요소들의 오와 열을 맞추는 것에서 기인
- 정보 구조와 배열을 체계적으로 작성하여 정보의 질서를 부여하는 시스템

## Grid cards

- row-cols 클래스를 사용하여 행당 표시할 열(카드) 수를 손쉽게 제어할 수 있음

