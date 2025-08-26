# CSS Box Model

## display 속성 (박스의 화면 배치 방식)

### 박스 타입

박스 타입에 따라 페이지에서의 배치 흐름 및 다른 박스와 관련하여 박스가 동작하는 방식이 달라짐

1) Block 타입
2) Inline 타입


### block 타입

블록 타입은 하나의 독립된 덩어리처럼 동작하는 요소

> block 타입은 책의 각 문단과 같다.   
> 모든 문단은 항상 새로운 줄에서 시작하며, 그 자체로 하나의 독립된 덩어리를 이룸   
> 다른 문단이 옆에 끼어들 수 없다.   
> 이처럼 block 타입은 웹 페이지의 큰 구조와 단락을 만듬

```css
.index {
  display: block;
}
```

### block 타입의 특성

- 항상 새로운 행으로 나뉨 (한 줄 전체를 차지, 너비 100%)
- width, height, margin, padding 속성을 모두 사용할 수 있음
- padding, margin, border로 인해 다른 요소를 상자로부터 밀어냄
- width 속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간을 모두 차지함
    - 상위 컨테이너 너비 100%로 채우는 것
- 대표적인 block 타입 태그 : `h1~6`, `p`, `div` `ul`, `li`

### block 타입의 대표: `div`

- 다른 HTML 요소들을 그룹화하여 레이아웃을 구성하거나 스타일링을 적용할 수 있음
- 헤더, 푸터, 사이드바 등 웹페이지의 다양한 섹션을 구조화하는 데 가장 많이 쓰이는 요소

```css
<div class="container">
  <h1>제목</h1>
  <p>단락 내용입니다.</p>
</div>

<div>
  <p>콘텐츠</p>
</div>
```

### inline 타입

문장 안의 단어처럼 흐름에 따라 자연스럽게 배치되는 요소
block 타입과 반대되는 개념이라고 생각해도 좋다.

> inline 타입은 문장 속 단어를 형광펜으로 칠하는 것과 같다.   
> 형광펜을 칠해도 문장의 흐름은 끊기지 않고 단어는 제자리에 있다   
> inline 타입은 줄을 바꾸지 않고, 텍스트의 일부에만 다른 스타일을 적용할 때 사용된다.   

```css
.indx {
  display: inline;
}
```

### inline 타입 특성

- 줄바꿈이 일어나지 않음 (콘텐츠의 크기만큼만 영역을 차지)
- width와 height 속성을 사용할 수 없음
- 수직 방향(상하)
    - padding, margin, border가 적용은 되지만, 다른 요소를 밀어낼 수는 없음
- 수평 방향(좌우)
    - padding, margin, border가 적용되어 다른 요소를 밀어낼 수 있음
- 대표적인 inline 타입 태그 : `a`, `img`, `span`, `strong`

### inline 타입의 대표 : `span`

- 자체적으로 시각적 변화 없음
    - 스타일을 적용하기 전까지는 특별한 변화 없음

- 텍스트 일부 조작
    - 문장 내 특정 단어나 구문에만 스타일을 적용할 때 유용

- 블록 요소처럼 줄바꿈을 일으키지 않으므로, 문서의 구조에 큰 변화를 주지 않음

```css
<p>이 문장에서 <span style="color: blue;">파란색</span> 단어만 색상이 다릅니다.</p>
<p>이 단어는 <span class="highlight-text">강조</span>되었습니다.</p>
<p>이것은 <span id="changeText">클릭</span>하면 변경됩니다.</p>
```

## Normal flow

일반적인 흐름 또는 레이아웃을 변경하지 않은 경우 웹 페이지 요소가 배치되는 방식

> 워드 문서를 예로 들면,   
> 엔터를 눌러 문단을 나누는 것이 block 요소의 배치 방식,   
> 엔터를 누르지 않고 계속 타이핑하는 것이 inline 요소의 배치 방식이다

html에서는 블록은 한 줄 전체를, 인라인은 콘텐츠만큼의 공간만을 차지하며 줄을 바꾸지 않는 것

```css
<body>
  <h1>Normal flow</h1>
  <p>Lorem, ipsum dolor sit amet consect explicabo</p>
  <div>
    <p>block 요소는 기본적으로 부모 요소의 너비 100%를 차지하며, 자식 콘텐츠의 최대 높이를 취한다.</p>
    <p>block 요소의 총 너비와 총 높이는 content + padding + border width/height다.</p>
  </div>
  <p>block 요소는 서로 margins로 구분된다.</p>
  <p>inline 요소는 <span>이 것처럼</span> 자체 콘텐츠의 너비와 높이만 차지한다.
    그리고 inline 요소는 <a href="#">width나 height 속성을 지정 할 수 없다.</a>
  </p>
  <p>
    물론 이미지도 <img src="#"> 인라인 요소다.
    단, 이미지는 다른 inline 요소와 달리 width나 height로 크기를 조정할 수 있다.
  </p>
  <p>
    만약 inline 요소의 크기를 제어하려면 block 요소로 변경하거나 inline-block 요소로 설정해주어야 한다.
  </p>
</body>
```

## 기타 display 속성

1. inline-block
2. none
3. flex

### inline 타입

`inline-block 타입`

inline과 block의 특징을 모두 가진 특별한 display 속성 값

- Block과 Inline의 특징을 합친 것 (줄바꿈 없이, 크기 지정 가능)
- width 및 height 속성 사용 가능
- padding, margin 및 border로 인해 다른 요소가 상자에서 밀려남

> TIP   
>   
> 주로 가로로 정렬된 내비게이션 메뉴나 여러 개의 버튼, 이미지 갤러리 처럼 수평으로 나열하면서,   
> 각 항목의 크기를 직접 제어하고 싶을 때 매우 유용하게 사용된다.

활용 예시

```css
<style>
  span {
    margin: 20px;
    padding: 20px;
    width: 80px;
    height: 50px;
    background-color: lightblue;
    border: 2px solid blue;
    display: inline-block;
  }

  ul>li {
    background-color: crimson;
    padding: 10px 20px;
    display: inline-block;
  }

  .container {
    text-align: center;
  }

  .box {
    width: 100px;
    height: 100px;
    background-color: #4CAF50;
    margin: 10px;
    display: inline-block;
  }
</style>
```


### none 타입

요소를 화면에 표시하지 않고, 공간조차 부여되지 않음

> none 타입은 축구팀의 '후보 선수'와 같다.   
> 선수는 팀 명단(HTML)에 포함되어 있지만, 벤치에 앉아있을 땐 경기장(웹 페이지)에 보이지 않는다.   
> 주전 선수는 후보 선수의 공간을 남겨두지 않고, 포메이션을 짠다.   
> 이처럼 요소가 레이아웃에서 아예 바져 있는 상태가 none 타입이다.

활용예시

```css
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .box {
      width: 100px;
      height: 100px;
      background-color: red;
      border: 2px solid black;
    }

    .none {
      display: none;
    }
  </style>
</head>

<body>
  <div class="box"></div>
  <div class="box none"></div>
  <div class="box"></div>
</body>

</html>
```


# CSS Position

### CSS Layout

각 요소의 **위치**와 **크기를 조정**하여 웹 페이지의 디자인을 결정하는 것   
요소들을 상하좌우로 정렬하고, 간격을 맞추고, 전체적인 페이지의 뼈대를 구성
- 핵심 속성: display(block, inline, flex, grid, ···)

### CSS Position

요소를 Normal Flow에서 제거하여 **다른 위치로 배치**하는 것   
다른 요소 위에 올리기, 화면의 특정 위치에 고정시키기 등
- 핵심 속성: position(static, relative, absolute, fixed, sticky, ···)

### Postion 이동 방향

- 네 가지 방향 속성(상, 하, 좌, 우)을 이용해 요소의 위치를 조절할 수 있음
- 겹치는 요소의 쌓이는 순서를 조절할 수 있음
-> 5가지 방식으로 이동 가능

## Position 유형

### 1. Position: static

- 요소를 Normal Flow에 따라 배치
- top, right, botton, left 속성이 적용되지 않음

- 기본 값
  ```css
  .static {
    position: static;
    background-color: lightcoral;
  }
  ```

### 2. Positon: relative

- 요소를 Normal Flow에 따라 배치
- **<u>자신의 원래 위치를 기준</u>** 으로 이동
- top, right, bottom, left 속성으로 위치를 조정
- 다른 요소의 레이아웃에 영향을 주지 않음 (요소가 차지하는 공간은 static일 때와 같음)
    - 본인의 위치를 벗어나서 이동은 하지만, 다른 요소들은 그 자리로 갈 수는 없음
    - 이동전의 위치를 계속 차지하면서 이동함

```css
.relative {
  position: relative;
  background-color: lightblue;
  top: 100px;
  left: 100px;
}
```

### 3. Positon: absolute

- 요소를 Normal Flow에서 제거
- **가장 가까운 relative 부모 요소를 기준**으로 이동
    - 만족하는 부모 요소가 없다면 body 태그를 기준으로 함
- top, right, bottom, left 속성으로 위치를 조정
- 문서에서 요소가 차지하는 공간이 없어짐
    - 다른 요소들도 움직이게 한다.
```css
.absolute {
  position: absolute;
  background-color: lightgreen;
  top: 100px;
  left: 100px;
}
```

### 4. Position: fixed

- 요소를 Normal Flow에서 제거
- 현재 화면영역(viewprt)을 기준으로 이동
    - margin 없는 전체 화면!
- 스크롤해도 항상 같은 위치에 유지됨
- top, right, bottom, left 속성으로 위치를 조정
- 문서에서 요소가 차지하는 공간이 없어짐
    - 다른 요소들에도 영향을 끼친다.

### 5. Position: sticky

- relative와 fixed의 특성을 결합한 속성
- 스크롤 위치가 임계점에 도달하기 전에는 relative처럼 동작
- 스크롤 위치가 임계점에 도달하면 fixed처럼 화면에 고정
- 다음 sticky요소가 나오면 이전 sticky요소의 자리를 대체
    - 이전 sticky 요소와 다음 sticky 요소의 위치가 겹치게 되기 때문


### Position absolute 활용(뱃지)

```css
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .card {
      position: relative;
      width: 300px;
      height: 200px;
      border: 1px solid black;
    }

    .card-content {
      padding: 10px;
    }

    .badge {
      position: absolute;
      top: 0;
      right: 0;
      background-color: red;
      color: white;
      padding: 5px 10px;
    }
  </style>
</head>

<body>
  <div class="card">
    <div class="card-content">
      <h3>Card Title</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
      <span class="badge">New</span>
    </div>
  </div>
</body>

</html>
```

## z-index

요소의 쌓임 순서를 정의하는 속성

> z-index는 연극 무대의 배우와 배경과 같다.   
> 무대 맨 뒤에는 숲 배경(z-index: 1)이 있고, 그 앞에는 배우(10)가 서 있다.   
> 배우의 z-index가 더 높기 때문에 배경보다 앞에 보이게 된다.   
> 이처럼 z-index는 요소들의 앞뒤 순서를 정해 입체감을 만든다.

### z-index의 특성

- 정수 값을 사용해 Z축 순서를 지정
- 값이 클 수록 요소가 위에 쌓이게 됨
- static이 아닌 요소에만 적용됨
- 기본 값은 auto로 부모 요소의 z-index 값에 영향을 받음
- 같은 부모 내에서만 z-index 값을 비교하고, 값이 같으면 HTML 문서 순서대로 쌓임
- 부모의 z-index가 낮으면 자식의 z-index가 아무리 높아도 부모보다 위로 올라갈 수 없음

> TIP   
>    
> - positon 속성이 static(기본값)이 아닌 요소에만 z-index가 적용됨
> - 음수 z-index 값은 요소를 부모 요소의 뒤(배경)로 보낼 때 사용할 수 있음


활용 예시

```css
.red {
  background-color: red;
  top: 50px;
  left: 50px;
  z-index: 3;
}

.green {
  background-color: green;
  top: 100px;
  left: 100px;
  z-index: 2;
}

.blue {
  background-color: blue;
  top: 150px;
  left: 150px;
  z-index: 1;
}
```

# CSS Flexbox

### 박스 표시(Display) 타입

1. Outer display 타입
  - block 타입
  - inline 타입

2. Inner display 타입
  - 박스 내부의 요소들이 어떻게 배치될지를 결정
  - CSS Flexbox(속성: flex)

### CSS Flexbox

요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식

> Flexbox(flex) 타입은 책장의 책들을 정리하는 것과 같다.   
> 책장(flex 컨테이너) 안에 책들(Flex 아이템)을 넣고,    
> "책들을 왼쪽에 붙여줘", "서로 같은 간격으로 띄워줘"와 같은 명령을 통해 손쉽게 배치할 수 있다.

## Flexbox 구성요소

- main axis (메인 축 : ↔)
- cross axis (교차 축 : ↕)
- flex container 
- flex item

### main axis (주 축)

- flex item 들이 배치되는 기본 축
- main start에서 시작하여 main end 방향으로 배치(기본 값) (왼쪽에서 오른쪽)

### cross axis (교차 축)

- main axis에 수직인 축
    - 메인 축이 변경되면 바뀐다.
-  cross start에서 시작하여 cross end 방향으로 배치 (위쪽에서 아래쪽)


## Flexbox 속성

### Flexbox 속성 목록 (간추린 version)

1. Flex Container 관련 속성

- display
- flex-direction
- flex-wrap
- justify-content
- align-items
- align-content

2. Flex Item 관련 속성

- align-self
- flex-grow
- flex-basis
- order


### 1. Flex Container 지정

- display 속성을 flex로 설정하면, Flex Container로 지정됨
- flex item은 기본적으로 행(주 축의 기본값인 가로 방향)으로 나열
- flex item은 주 축의 시작 선에서 시작
- flex item은 교차 축의 크기를 채우기 위해 늘어남

### 2. flex-direction

- flex item이 **나열되는 방향을 지정**
- 속성
    - row(기본값): 아이템을 가로 방향으로, 왼쪽에서 오른쪽으로 배치
    - column: 아이템을 세로 방향으로 위에서 아래로 배치
    - "-reverse"로 지정하면 flex item 배치의 시작 선과 끝 선이 서로 바뀜

### 3. flex-wrap

- flex item 목록이 flex container의 한 행에 들어가지 않을 경우, **다른 행에 배치할지 여부 설정**
- 속성
    - nowrap(기본 값): 줄 바꿈을 하지 않음
    - wrap: 여러 줄에 걸쳐 배치될 수 있게 설정


### 4. justify-content

  - 주 축을 따라 flex item들을 정렬하고 간격을 조정
  - 속성
      - flex-start(기본값): 주 축의 시작점으로 정렬
      - center: 주 축의 중앙으로 정렬
      - flex-end: 주축의 끝점으로 정렬


### 5. align-content

- 컨테이너에 여러 줄의 flex item이 있을 때, 그 줄들 사이의 공간을 어떻게 분배할 지 지정
    - flex-wrap이 wrap 또는 wrap-reverse로 설정된 여러 행에만 적용됨
    - Flex 아이템이 두 줄 이상일 때만 의미가 있음(flex-wrap이 nowrap으로 설정된 이유)

- 속성
    - stretch(기본값) : 여러 줄을 교차 축에 맞게 늘려 빈 공간을 채움
    - center: 여러 줄을 교차 축의 중앙에 맞취 정렬
    - flex-start: 여러 줄을 교차 축의 시작점(보통 위쪽)에 맞춰 정렬
    - flex-end: 여러 줄을 교차 축의 끝점(보통 아래쪽)에 맞춰 정렬
    ```css
    .container {
      height: 500px;
      border: 1px solid black;
      display: flex;
      /* flex-wrap: nowrap; */
      flex-wrap: wrap;
      /* align-content: flex-start; */
      align-content: center;
      /* align-content: flex-end; */
    }
    ```

### 6. align-items

- 컨테이너 안에 있는 flex item들의 **교차 축 정렬** 방법을 지정
- 속성
    - stretch(기본값): 아이템을 교차 축 높이를 꽉 채우도록 늘어남
    - center: 아이템을 교차 축의 중앙에 맞춰 정렬
    - flex-start: 아이템을 교차 축의 시작점(가로 방향일 경우 위쪽)에 맞춰 정렬
    - flex-end: 아이템을 교차 축의 끝점(가로 방향일 경우 아래쪽)에 맞춰 정렬
    ```css
    .container {
      height: 500px;
      border: 1px solid black;
      display: flex;

      /* align-items: flex-start; */
      align-items: center;
      /* align-items: flex-end; */
    }
    ```

### 7. align-self

- 컨테이너 안에 있는 flex item들을 교차 축을 따라 개별적으로 정렬
- 속성
    - auto(기본값): 부모 컨테이너의 <u>align-items</u> 속성 값을 상속
    - stretch: 해당 아이템만 교차 축 방향으로 늘어나 컨테이너를 꽉 채우도록 정렬
    - center: 해당 아이템만 교차 축의 중앙에 정렬
    - flex-start: 해당 아이템만 교차 축의 시작점(가로 방향일 경우 위쪽)에 정렬
    - flex-end: 해당 아이템만 교차 축의 끝점(가로 방향일 경우 아래쪽)에 정렬

    ```css
    .item1 {
      align-self: center;
    }

    .item2 {
      align-self: flex-end;
    }
    ```

### 목적에 따른 속성 분류

- 배치(flex-direction, flex-wrap)
- 공간 분배(justify-content, align-content)
- 정렬(align-items, align-self)

### 속성 쉽게 이해하는 방법

- justify - 주축
- align - 교차 축

> TIP    
>   
> - justify-items 및 justify-self 속성이 없는 이유는 뭘까?   
> 애초에 필요가 없기 때문    
> 간단하게 margin auto를 통해 정렬 및 배치가 가능하다.


### 8. flex-grow

- 남는 행 여백을 비율에 따라 각 flex item에 분배
- flex item이 컨테이너 내에서 확장하는 비율을 지정
```css
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .container {
      display: flex;
      width: 100%;
    }

    .item {
      height: 100px;
      color: white;
      font-size: 3rem;
    }

    .item-1 {
      background-color: red;
      flex-grow: 1;
    }

    .item-2 {
      background-color: green;
      flex-grow: 2;
    }

    .item-3 {
      background-color: blue;
      flex-grow: 3;
    }
  </style>
</head>

<body>
  <div class="container">
    <div class="item item-1">1</div>
    <div class="item item-2">2</div>
    <div class="item item-3">3</div>
  </div>
</body>

</html>
```

> TIP   
>   
> **Flex-shrink**   
> - flex-grow의 반대 개념
> - 컨테이너의 공간이 부족할 때, flex item이 줄어드는 비율을 지정하는 속성

### flex-basis

- flex item의 초기 크기 값을 지정
- flex-basis와 width 값을 동시에 적용한 경우 flex-basis가 우선
``` css
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .container {
      display: flex;
      width: 100%;
    }

    .item {
      height: 100px;
      color: white;
      font-size: 3rem;
    }

    .item-1 {
      background-color: red;
      flex-basis: 300px;
    }

    .item-2 {
      background-color: green;
      flex-basis: 600px;
    }

    .item-3 {
      background-color: blue;
      flex-basis: 300px;
    }
  </style>
</head>

<body>
  <div class="container">
    <div class="item item-1">1</div>
    <div class="item item-2">2</div>
    <div class="item item-3">3</div>
  </div>
</body>

</html>
```

## flex-wrap 응용

### 반응형 레이아웃 작성

다양한 디바이스와 화면 크기에 자동으로 적응하여 콘텐츠를 최적으로 표시하는 웹 레이아웃 방식  

flex-wrap을 사용해 반응형 레이아웃 작성(flex-grow&flex-basis 활용)

1. .card 요소를 flex 컨테이너로 설정
2. 컨테이너의 공간이 부족할 경우, 여러 줄로 나뉘어 배치되도록 허용
3. 각 flex item의 기본 너비를 설정
4. 컨테이너에 여유 공간이 있을 때 공간을 차지하며 늘어날 수 있도록 함
    - 두 flex item 모두 값이 1 이므로 절반씩 나눠가짐

```css
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .card {
      width: 80%;
      border: 1px solid black;
      /* 1 */
      display: flex;
      /* 2 */
      flex-wrap: wrap;
    }

    img {
      width: 100%;
    }

    .thumbnail {
      /* 3 */
      flex-basis: 700px;
      /* 4 */
      flex-grow: 1;
    }

    .content {
      /* 3 */
      flex-basis: 350px;
      /* 4 */
      flex-grow: 1;
    }
  </style>
</head>

<body>
  <div class="card">
    <img class="thumbnail" src="images/sample.jpg" alt="sample">
    <div class="content">
      <h2>Heading</h2>
      <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis minus sed expedita ut nihil tempora
        neque autem odio eos, repudiandae blanditiis, molestiae consequatur. Adipisci illo dolor repellat alias
        maiores.
        Aut?</p>
    </div>
  </div>
</body>

</html>
```

# 참고

## 박스 타입 별 수평 정렬

### block 요소의 수평 정렬

- margin: auto 사용
- 블록의 너비를 지정하고 좌우 마진을 auto로 설정

```css
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .box {
      width: 100px;
      height: 100px;
      background-color: crimson;
      border: 1px solid black;
    }

    .margin-auto {
      margin: 0 auto;
    }
  </style>
</head>
<body>
  <div class="box margin-auto"></div>
</body>
```

### inline 요소의 수평 정렬
- text-align 사용
- 부모 요소에 적용
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .text-center {
      text-align: center;
    }

  </style>
</head>
<body>
  <div class="text-center">
    <span>inline요소</span>
  </div>

</body>

### inline-block 요소의 수평정렬

- text-align 사용
- 부모 요소에 적용

## Flexbox 속성정리

### flex-direction

1. row(기본값): 아이템을 가로 방향으로, 왼쪽에서 오른쪽으로 배치
2. row-reverse: 아이템을 가로 방향으로, 오른쪽에서 왼쪽으로 배치
3. column: 아이템을 세로 방향으로, 위에서 아래로 배치
4. column-reverse: 아이템을 세로 방향으로, 아래에서 위로 배치

### flex-wrap

1. wrap: 여러 줄에 걸쳐 배치될 수 있게 설정
2. nowrap(기본 값): 줄 바꿈을 하지 않음

### justify-content

1. flex-start(기본값): 주 축의 시작점으로 정렬
2. flex-end: 주 축의 끝점으로 정렬
3. center: 주 축의 중앙으로 정렬
4. space-between: 첫 아이템은 시작점, 마지막 아이템은 끝점에 붙이고 아이템들 사이의 간격을 균등하게 배분
5. space-around: 각 아이템의 둘레에 균등한 간격으로 배분.(양 끝 아이템은 절반의 간격이 설정)
6. space-evenly: 모든 아이템들 사이와 양 끝의 간격을 모두 동일하게 배분

### align-content

1. flex-start: 여러 줄을 교차 축의 시작점에 맞춰 정렬
2. flex-end: 여러 줄을 교차 축의 끝점(보통 아래쪽)에 맞춰 정렬
3. center: 여러 줄을 컨테이너의 중앙으로 정렬
4. space-between: 첫 줄은 시작점에, 마지막 줄은 끝점에 붙이고, 그 사이 줄들의 간격을 균등하게 배분
5. space-around: 각 줄의 위아래에 균등한 간격을 배분(컨테이너의 시작과 끝에는 절반의 간격이 설정)
6. space-evenly: 모든 줄들 사이와 양 끝의 간격을 모두 동일하게 배분

### align-items

1. stretch(기본값): 아이템이 교차 축 방향으로 늘어나 컨테이너를 꽉 채우도록 정렬
2. flex-start: 아이템을 교차 축의 시작점(가로 방향일 경우 위쪽)에 맞춰 정렬
3. flex-end: 아이템을 교차 축의 끝점(가로 방향일 경우 아래쪽)에 맞춰 정렬
4. center: 아이템을 교차 축 높이를 꽉 채우도록 늘어남

### align-self

1. stretch: 해당 아이템만 교차 축 방향으로 늘어나 컨테이너를 꽉 채우도록 정렬
2. flex-start: 해당 아이템만 교차 축의 시작점(가로 방향일 경우 위쪽)에 정렬
3. flex-end: 해당 아이템만 교차 축의 끝점(가로 방향일 경우 아래쪽)에 정렬
4. center: 해당 아이템만 교차축의 중앙에 정렬

