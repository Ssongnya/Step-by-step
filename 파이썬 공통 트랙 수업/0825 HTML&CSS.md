# 웹

## 기본 용어 설명

### Web
Web site, Web application 등을 통해 사용자들이 정보를 검색하고 상호작용 하는 기술

### WWW

#### World Wide Web

인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보 공간
### Web site

인터넷에서 여러 개의 **Web page**가 모인 것으로, 사용자들에게 정보나 서비스를 제공하는 공간


### Web page

HTML, CSS 등의 웹 기술을 이용하여 만들어진, **"Web site"를 구성하는 하나의 요소**

### Web page의 구성요소

만약 집을 만든다면?
1) 철제 프레임(구조)
2) 페인트 (스타일링)
3) 불 켜기 (행위)

#### Web page는?

1) **HTML - 구조 담당**
2) **CSS - 스타일링 담당**
3) Javascript - 행동 담당


# 웹 구조화

## HTML

### HTML

: HyperText Markup Language

웹 페이지의 **<u>의미</u>**와 **<u>구조</u>**를 정의하는 언어 (약어)

### HyperText

: 웹 페이지를 다른 페이지로 연결하는 링크

- 참조를 통해 사용하자 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
- **비선형성** / 상호연결성 / 사용자 주도적 탐색

### Markup Language

: 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

- 인간이 읽고 쓰기 쉬운 형태이면, **데이터의 구조와 의미**를 정의하는 데 집중
- ex) HTML, Markdown

#### Markup Language 예시

- 아무런 구조와 형식 없이 내용만 있는 원본 데이터
```
HTML. HTML 이란 Hyper Text Markup Language의 약자이다.
Hyper Text. Hyper Text란 기존의 선형적인 텍스트가 아닌 비선형적을 이루어진텍스트를 의미하며, 이는 인터넷의 등장과 함께 대두되었다.
```

- 사람이 이해할 수 있도록 논리적 구조를 부여한 상태
```
 1. HTML
      HTML 이란 Hyper Text Markup Language의 약자이다.   
 1.1. Hyper Text   
      Hyper Text. Hyper Text란 기존의 선형적인 텍스트가 아닌 비선형적을 이루어진 텍스트를 의미하며, 이는 인터넷의 등장과 함께 대두되었다.
 ```

- 컴퓨터가 이해하고 화면에 표현할 수 있도록 약속된 언어(HTML)로 구조를 완성한 상태

```
<h1>HTML</h1>
<p>HTML 이란 Hyper Text Markup Language의 약자이다.</p>
<h2>Hyper Text</h2>
<p> Hyper Text. Hyper Text란 기존의 선형적인 텍스트가 아닌 비선형적을 이루어진 텍스트를 의미하며, 이는 인터넷의 등장과 함께 대두되었다.</p>
```

## Structure of HTML

### HTML 구조

1. `<!DOCTYPE html>`
    - 해당 문서가 html로 문서라는 것을 나타냄

2. `<html></html>`
    - 전체 페이지의 콘텐츠를 포함

3. `<title></title>`
    - 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용

4. `<head></head>`
    - HTML 문서에 관련된 설명, 설정 등 컴퓨터가 식별하는 <u>메타데이터</u>를 작성
    - 사용자에게 보이지 않음 (눈에 보이는 설정이 아닌 개발자 도구에서 볼 수 있는 코드)

5. `<body></body>`
    - HTML 문서의 내용을 나타냄
    - 페이지에 표시되는 모든 콘텐츠를 작성
    - 한 문서에 하나의 body 요소만 존재


### HTML element(요소)

- 하나의 요소는 **여는 태그**와 **닫는 태그** 그리고 그 안의 **내용**으로 구성됨
- 닫는 태그는 태그 이름 앞에 슬래시가 포함됨
- 닫는 태그가 없는 태그도 존재 (내용이 없는 요소도 존재)
- `<p>My cat is very grumpy</p>`
  - `<p>` : 여는 테그
  - `My cat is very grumpy` : 내용
  - `</p>` : 닫는 테그

### HTML Attributes(속성)

사용자가 원하는 기준에 맞도록 요소를 설정하거나 다양한 방식으로 요소의 동작을 조절하기 위한 값

- 목적
  - 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
  - CSS에서 스타일 적용을 위해 해당 요소를 선택하기 위한 값으로 활용됨
    - CSS : 웹페이지의 디자인과 레이아웃을 구성하는 언어

- 작성 규칙
  1. 속성은 요소 이름과 속성 사이에 공백이 있어야 함
  2. 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함
  3. 속성 값은 열고 닫는 따옴표로 감싸야 함
  4. ex) `<p class="editor-note">My cat is very grumpy</p>`

-> CSS 파트 가서 더 자세히 배울 것!

### HTML 구조 예시

```CSS
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>My page</title>
</head>
<body>
<p>본문입니다.</p>
</body>
</html>
```

#### 자동완성 기능도 존재 `!` 

```CSS
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  
</body>
</html>
```

자동완성 코드를 활용한 예제

```CSS
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <p>My page</p>
  /*Paragraph(문단)의 약자로, 텍스트 문단을 만드는 태그*/

  <a href="http://www.google.co.kr/">google</a>
  /*Anchor(닻)의 약자로, 다른 페이지로 이동시키는 하이퍼링크 태그*/

  <img src="images/sample.png" alt="sample-img">
  <img src="https://random.imagecdn.app/500/150/" alt="sample-img">
  /*Image(이미지)의 약자로, src에 지정된 그림을 보여주는 태그
  alt는 필수 속성은 아니지만, 웹 접근성기술 측면에서 사용해주어야 함*/

</body>
</html>
```

## Text Sturcture

### HTML Text Structure

- HTML의 주요 목적 중 하나는 **텍스트 구조와 의미**를 제공하는 것
- 예를 들어 h1요소는 단순히 텍스트를 크게만 만드는 것이 아닌 현재 문서의 최사우이 제목이라는 의미를 부여하는 것   
  ex) `<h1>Heading</h1>`

> TIP   
>   
> 의미에 맞는 태그 사용은 스크린 리더, 검색 엔진 최적화(SEO)의 기본이 된다.
>   - 스크린 리더 : 화면 내용을 소리로 읽어주는 프로그램
>   - 검색 엔진 최적화(SEO) : 검색 결과 상단에 내 사이트를 노출시켜 방문자를 늘리는 작업


#### 대표적인 HTML Text structure

- Heading & Paragraphs
    - h1~6, p

- Lists
    - ol, ul, li

- Emphasis & Importance
  - em, strong

---

# 웹 스타일링

## CSS

웹 페이지의 디자인과 레이아웃을 구성하는 언어

### CSS 적용 방법

1. 인라인 스타일
2. 내부 스타일 시트
3. 외부 스타일 시트


### 1. 인라인(Inline) 스타일
```CSS
<body>
<h1 style="color:blue; background-color: yellow;">Inline Style</Style></h1>
</body>
```
- HTML 요소 안에 <u>style 속성 값</u>으로 작성
- 기본적으로 급하지 않는 이상 사용하지 않음
  - 가독성 등 여러 측면 고려

### 2. 내부(Internal) 스타일 시트

```CSS
<head>
  ···
  <title>Document</title>
  <style>
    h2 {
      color: red;
      background: black;
    }
  </style>
</head>
```
- <u>head 태그</u> 안에 <u>style 태그</u>에 작성

### 3. 외부(External) 스타일 시트
```CSS
<head>
  ···
  <link rel="stylesheet" href="style.css">
  ···
</head>
```
- 별도 CSS 파일 생성 후 HTML <u>link 태그</u>를 사용해 불러오기

```CSS
별도 CSS 파일 내용

h3 {
  color: violet;
  background-color: green;
}
```
> TIP   
>   
> - 스타일 적용 우선순위는 인라인 > 내부 > 외부 순으로 적용된다.   
> - 인라인 스타일은 재사용이 어렵고 유지보수를 방해하니, 테스트나 특수한 경우에만 사용하는 것을 추천.

## CSS 구문

### CSS 기본 구조와 문법

- 선택자(Selector)
  - '누구를' 꾸밀지 지정하는 부분

- 선언(Declaration)
  - '어떻게' 꾸밀지에 대한 구체적인 한 줄의 명령
  - 속성과 값이 한 쌍으로 이루어지며, 세미콜론(;)으로 끝남

- 속성(Property)
  - 바꾸고 싶은 스타일의 종류를 나타냄

- 값(Value)
  - 속성에 적용할 구체적인 설정을 나타냄

## CSS 선택자

### CSS Selectors

HTML 요소를 선택하여 스타일을 적용할 수 있도록하는 선택자

```CSS
h1 {
  color: red;
  font-size: 30px;
}
```

### CSS 선택자 종류

- 기본 선택자
  - 전체(*) 선택자
  - 요소(tag) 선택자
  - 클래스(class) 선택자
  - 아이디(id) 선택자
  - 속성(attr) 선택자 등

- 결합자 (Combinators)
  - 자손 결합자(" "(space))
  - 자식 결합자(">")

### CSS 선택자: 기본 선택자

- 전체(*) 선택자 : HTML 모든 요소를 선택

- 요소 선택자 : 지저안 모든 태그를 선택

- 클래스 선택자 ('.'(dot)) : 주어진 클래스 속성을 가진 모든 요소를 선택
  - 수업에서는 클래스 선택자만 쓰도록 할 거임.

- 아이디 선택자 ('#')
  - 주어진 아이디 속성을 가진 요소 선택
  - 문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함

- 속성 선택자('[]'(대괄호))
  - 주어진 속성이나 속성값을 가진 모든 요소 선택
  - 속성의 존재 여부, 값의 일치/포함 등 다양한 조건으로 요소를 정교하게 선택가능


### CSS 결합자

- 자손 결합자 (" "(space))
  - 첫 번째 요소의 자손 요소들 선택
  - 예) `p span`은 `<p>`안에 있는 모든 `<span>`을 선택 (하위 레벨 상관 없이)

- 자식 결합자 (">")
  - 첫 번째 요소의 직계 자식만 선택
  - 예) `ul > li`는 `<ul>`안에 있는 모든 `<li>`를 선택 (한 단계 아래 자식들만)

### CSS 선택자, 결합자 적용 예시
```css
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    /* 전체 선택자 */
    * {
      color: red;
    }
    /* 요소 선택자 */
    h2 {
      color: orange;
    }
    h3,
    h4 {
      color: blue;
    }

    /* class 선택자 */
    .green{
      color: green;
    }
    /* id 선택자 */
    #purple {
      color: purple;
    }
    /* 자식 결합자 */

    .green > sapn {
      font-size: 50px;
    }

    /* 자손 결합자 */

    .green li {
      color: brown;
    }
    /* 속성 선택자 */
    [class^="y"] {
      color: yellow;
    }
  </style>
</head>

<body>
  <h1 class="green">Heading</h1>
  <h2>선택자</h2>
  <h3>연습</h3>
  <h4>반가워요</h4>
  <p id="purple">과목 목록</p>
  <ul class="green">
    <li>파이썬</li>
    <li>알고리즘</li>
    <li>웹
      <ol>
        <li>HTML</li>
        <li>CSS</li>
        <li>PYTHON</li>
      </ol>
    </li>
  </ul>
  <p class="green">Lorem, <span>ipsum</span> dolor.</p>
  <p class="yellow">TEST</p>
</body>

</html>
```

## CSS선언

### CSS Declaration

선택된 요소에 적용할 스타일을 구체적으로 명시하는 부분
- 중괄호 안쪽 부분! 무엇을 할지를 결정

```
CSS 선언의 목적
- 선택자는 '어떤 요소에' 스타일을 적용할지 결정하는 규칙
- 선택자로 요소를 선택했으니, 이제 중괄호 {} 안에 '무엇을' 할지 정의
- 이 '무엇을'에 해당하는 부분이 바로 선언(Declaration)
```

### 속성

- 스타일링하고 싶은 기능이나 특성을 의미
- CSS가 미리 정의해 둔 키워드를 사용해야 함
- `font-size`, `background-color`, `width`, `margin`, `padding` 등

### 값

- 속성에 적용될 구체적인 설정
- 속성이 받을 수 있는 값의 종류는 정해져 있음
- `16px`, `lightgray`, `100%`, `10rem` 등

### 값의 단위(Units)

- `color: red;` 처럼 키워드로 끝나는 값도 있지만, 크기나 간격을 나타낼 때는 단위가 필수적
- 단위는 크게 절대 단위와 상대 단위로 나뉜다.

|구분|단위 종류|특징|
|---|--------|----|
|절대 단위|px, pt, cm 등|다른 요소의 영향을 받지 않는 고정된 크기|
|상대 단위|%, em, rem, vw, vh 등|다른 요소(부모, 화면 표시 영역 등)의 크기에 따라 상대적으로 결정|

> TIP   
>   
> - **웹 디자인에서는 반응형 웹과 접근성 때문에 "상대 단위의 중요성"이 매우 높다**
> - 값이 0일 때는 단위를 생략하는 것이 권장된다.


### 절대 단위의 대표: "px"

- 화면을 구성하는 가장 작은 단위인 '픽셀'을 기준으로 하는 절대 단위
- 모니터 해상도에 따라 크기가 결정되며, 직관적이고 예측이 쉬움
- 장점
  - 디자인 시안과 거의 동일한 결과물을 만들 수 있음
  - 요소의 크기를 명확하게 고정하고 싶을 때 유용
- 단점
  - 사용자가 브라우저의 기본 폰트 크기를 변경해도 요소의 크기가 함께 조절되지 않아 접근성에 불리
  - 다양한 디바이스 크기에 유연하게 대응하는 반응형 디자인에 한계가 있음

### 상대 단위: "em"

- 부모 요소의 font-size를 기준으로 크기가 결정되는 상대 단위
- 만약 부모 요소에 font-size가 없다면, 그 상위 부모의 font-size를 상속 받음
- 장점
  - 부모 요소의 크기에 따라 자식 요소의 크기를 유연하게 조절할 수 있음

- 단점
  - **중첩 문제**
  - em 단위를 사용하는 요소가 충첩되면 기준 크기가 계속 변경되어 계산이 복잡해지고 예측이 어려워짐
    - <u>**rem**</u>으로 해결

### 상대 단위의 해결사: "rem"

- "Root em"
- em의 단점을 극복하기 위해 등장
- 부모 요소가 아닌, 최상위 요소인 `<html>`의 font-size를 기준으로 크기가 결정
- html의 기본 font-size는 대부분의 브라우저에서 **16px**

### em, rem 적용 예시
```css
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    /* rem의 기준이 되는 최상위 요소(root)의 글자 크기를 10px로 설정합니다.
    계산을 쉽게 하기 위함이며, 브라우저 기본값은 보통 16px입니다.
  */
    html {
      font-size: 10px;
    }

    /* em의 기준이 될 부모 요소 */
    .parent-for-em {
      font-size: 20px;
      border: 2px solid blue;
      padding: 10px;
      margin-bottom: 20px;
    }

    /* em 단위 사용 */
    .em-unit {
      /* 부모(.parent-for-em)의 font-size인 20px을 기준으로 1.5배 크기를 가집니다.
      계산: 20px * 1.5 = 30px
    */
      font-size: 1.5em;
    }

    /* rem 단위 사용 */
    .rem-unit {
      /* 최상위 요소(html)의 font-size인 10px을 기준으로 1.5배 크기를 가집니다.
      계산: 10px * 1.5 = 15px
    */
      font-size: 1.5rem;
      border: 2px solid red;
      padding: 10px;
    }
  </style>
</head>

<body>

  <div class="parent-for-em">
    부모 요소 (font-size: 20px)
    <div class="em-unit">
      em 단위 자식 (font-size: 1.5em ==> 30px)
    </div>
  </div>

  <div class="rem-unit">
    rem 단위 요소 (font-size: 1.5rem ==> 15px)
  </div>

</body>

</html>
```

#### rem의 특성

1) 일관성 및 예측 가능성
    - 요소가 아무리 깊게 중첩되어도 기준은 항 상 html이므로, em처럼 계산이 복잡해지지 않음

2) 유지보수 용이성
    - html의 font-size만 변경하면 사이트 전체의 레이아웃과 폰트 크기를 일관되게 조절할 수 있음

3) 접근성 향상
    - 사용자가 브라우저에서 설정한 기본 폰트 크기를 html이 상속받으므로, 사용자의 설정에 맞춰 사이트 전체가 유연하게 확대/축소 됨

### 단위 비교 정리
|단위|기준|장점|단점/주의사항|추천 사용처|
|----|---|----|----------|----------|
|`px`|화면의 픽셀|직관적, 고정된 크기|접근성/반응형에 불리|border-width 등 절대적 크기가 필요할때|
|`em`|부포 요소의 font-size|부모에 따라 유연하게 변경|중첩 시 계산 복잡|특정 컴포넌트 내부에서만 상대적 크기 조절이 필요할 때|
|`rem`|<html>의 font-size|**일관성, 유지보수성, 접근성**|루트 폰트 크기에 의존적|**웹사이트 전반의 font-size, margin, padding 등**|
|`%`|부모 요소의 크기|컨테이너에 맞춰 유동적으로|font-size에 사용 시 em과 유사하게 동작|width, height 등 레이아웃 구성 시|

## 명시도

### 명시도(Specificity)

결과적으로 요소에 적용할 CSS 선언을 결정하기 위한 알고리즘

- CSS Selector에 가중치를 계산하여 어떤 스타일을 적용할지 결정
- 동일한 요소를 가리키는 2개 이상의 CSS 규칙이 있는 경우, 가장 높은 명시도를 가진 Selector가 승리하여 스타일이 적용됨

### CSS
  - **Cascading** Style Sheet
  - 웹페이지의 디자인과 레이아웃을 구성하는 언어

### Cascade
  - 계단식
  - 한 요소에 동일한 가중치를 가진 선택자가 적용될 때
  - CSS에서 마지막에 나오는 선언이 사용됨

  ```css
  h1 {
    color: red;
  }
  h1 {
    color: purple;
  }
  ```
  #### Quiz) 위의 h1 태그 내용에 적용되는 색은?   
  Answer) 소스 코드에서 더 나중에 선언된 규칙이 덮어씀   
  ∴ `purple`이 적용됨

  ```css
  .make-red {
    color: red;
  }
  h1 {
    color: purple;
  }
  ```
  #### Quiz) 동일한 h1태그에 다음과 같이 스타일이 작성된다면, h1 태그 내용에 적용되는 색은?
  Answer) 선택자의 명시도에 따라 클래스 선택자를 따름   
  ∴ `red`가 적용됨

### 명시도가 높은 순

1. Importance
  - `!important`

2. Inline 스타일

3. 선택자
    - id 선택자 > class 선택자 > 요소 선택자
      - id 선택자(#id) : 페이지에서 단 하나의 특별한 요소를 선택할 때 사용 
      - class 선택자(.class) : 여러 요소에 동일한 스타일을 적용할 때 사용
      - 요소 선택자(ex: p, div, ···) : 페이지의 모든 특정 태그(p, div등)를 선택
4. 소스 코드 선언 순서

#### 명시도 예시

```css
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    h2 {
      color: darkviolet !important;
    }

    p {
      color: blue;
    }

    .orange {
      color: orange;
    }

    .green {
      color: green;
    }

    #red {
      color: red;
    }
  </style>
</head>

<body>
  <p>1</p>
  <p class="orange">2</p>
  <p class="green orange">3</p>
  <p class="orange green">4</p>
  <p id="red" class="orange">5</p>
  <h2 id="red" class="orange">6</h2>
  <p id="red" class="orange" style="color: brown;">7</p>
  <h2 id="red" class="orange" style="color: brown;">8</h2>
</body>

</html>
```

### !important

`!important`
다른 우선순위 규칙보다 우선하여 적용하는 키워드

▣ **Cascade의 구조를 무시하고 강제로 스타일을 적용하는 방식이므로 사용을 권장하지 않음**

## 상속

### CSS 상속

- 기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높임

- 상속 되는 속성
  - Text 관련 요소 (font, color, text-align), opacity, visibility 등

- 상속 되지 않는 속성
  - Box model 관련 요소(width, height, border, box-sizing ...)
  - position 관련 요소 (position, top/right/bottom/left, z-index) 등

- 상속 여부 확인
  - <u>MDN</u>의 각 속성별 문서 하단에서 상속 여부를 확인할 수 있음
  - mdn : 웹 개발자를 위한 공식 기술 문서 사이트

#### CSS 상속 예시

```css
<body>
  <ul class="parent">
    <li class="child">Hello</li>
    <li class="child">Bye</li>
  </ul>
</body>
```

```css
<style>
  .parent {
    /* 상속 O */
    color: red;

    /* 상속 X */
    border: 1px solid black;
  }
</style>
```

## CSS Box Model

웹 페이지의 모든 HTML 요소를 감싸는 사각형 상자 모델

- 요소의 크기, 배치, 간격을 결정하는 규칙
- 원은 네모 박스를 깎은 것일 뿐
- 하나의 페이지를 만드는 것은 네모난 사각형 상자 모델을 쌓아서 만드는 것

## 박스 구성 요소

1. 내용(content) : 실제 내용이 위치하는 영역

2. 안쪽 여백(padding) : 테두리와 내용 사이의 내부 여백

3. 테두리(border) : content와 padding을 감싸는 테두리

4. 외부 간격(margin) : 이 박스와 다른 요소와의 외부 간격

으로 구성되어 요소의 크기와 배치를 결정

### box 구성의 방향 별 속성 값

1. top →
2. right ↓
3. bottom ←
4. left ↑

### box 구성 요소 예시

```css
<body>
  <div class="box1">box1</div>
  <div class="box2">box2</div>
</body>
```



## shorthand 속성 (단축 속성)

### 'border'

- border-width, border-style, border-color를 한 번에 설정하기 위한 속성
```CSS
border: 2px solid black;
```

### 'margin' & 'padding'

- 4방향의 속성을 각각 지정하지 않고 한번에 지정할 수 있는 속성

## box-sizing 속성 (박스의 크기 계산법)

### The standard CSS box model

1. 표준 상자 모델에서 width와 height 속성 값을 설정하면, 이 값은 _content box_ 의 크기를 조정하게 됨

2. CSS는 border box가 아닌 content box의 크기를 width 값으로 지정

### The alternative CSS box model

- 대체 상자 모델에서 모든 width와 height는 실제 상자의 너비
- 실제 박스 크기를 정하기 위해테두리와 패딩을 조정할 필요 없음

#### 대체 상자 모델로 변경 : box-sizing 속성

```css
컨텐츠 박스의 크기

* {
  box-sizing: content-box;
}

내용을 포함한 전체(실제) 박스의 크기

* {
  box-sizing: border-box;
}

```

---

# 참고

## HTML 스타일 가이드

1. 대소문자 구분
    - HTML은 대소문자를 구분하지 않지만, 소문자 사용을 강력히 권장
    - 태그명과 속성명 모두 소문자로 작성
  
2. 속성 따옴표
    - 속성 값에는 큰 따옴표("")를 사용하는 것이 일반적

3. 코드 구조와 포맷팅
    - 일관된 들여쓰기를 사용 (보통 2칸 공백)
    - 각 요소는 한 줄에 하나씩 작성
    - 중첩된 요소는 한 단계 더 들여쓰기

4. 공백 처리
    - HTML은 연속된 공백을 하나로 처리
    - Enter키로 줄 바꿈을 해도 브라우저에서 인식하지 않음 (줄 바꿈 태그를 사용해야 함)

5. 에러 출력 없음
    - HTML은 문법 오류가 있어도 별도의 에러 메시지를 출력하지 않음

> TIP   
>   
> 속성 값에 띄어쓰기가 포함된다면, 따옴표는 선택이 아닌 필수이므로 꼭 사용해야 합니다.
> - `<p class=text-style red-color></p>` 경우에는 red-color가 적용되지 않음
> - `<p class="text-style red-color"></p>`와 같이 꼭 따옴표 작성하기

## CSS 스타일 가이드

1. 코드 구조와 포맷팅
  - 1) 일관된 들여쓰기를 사용(보통 2칸 공백)
  - 2) 선택자와 속성은 각각 새 줄에 작성
  - 3) 중괄호 앞에 공백 넣기
  - 4) 속성 뒤에는 콜론(':')과 공백 넣기
  - 5) 마지막 속성 뒤에는 세미콜론(';') 넣기

2. 선택자 사용
  - 1) <u>**class 선택자</u>를 우선적으로 사용**
  - 2) id, 요소 선택자 등은 가능한 피할 것
  - 여러 선택자들과 함께 사용할 경우 우선순위 규칙에 따라 예기치 못한 스타일 규칙이 적용되어 전반적인 유시보수가 어려워지기 때문

3. 속성과 값
  - 1) 속성과 값은 소문자로 작성
  - 2) 0 값에는 단위를 붙이지 않음

4. 명명 규칙
  - 1) 클래스 이름은 의미 있고 목적을 나타내는 이름을 사용
  - 2) 케밥 케이스(kebab-case)를 사용
  - 3) 약어보다는 전체 단어를 사용

5. CSS 적용 스타일
  - 1) <u>인라인(inline) 스타일</u>은 되도록 사용하지 말 것
  - 2) CSS와 HTML 구조 정보가 혼합되어 작서오디기 때문에 코드를 이해하기 어렵게 만듦


## MDN

### MDN Web Docs
Mozilla Developer Network에서 제공하는 온라인 문서로, 웹 개발자와 디자이너를 위한 종합적인 참고 자료

HTML, CSS, JavaScript, 웹 API, 개발 도구 등 웹 기술에 대한 정보를 제공

### MDN 문서를 활용해야 하는 이유

1. 정확성 및 신뢰성
    - Mozilla와 웹 커뮤니티의 전문가들에 의해 작성되고 유지 관리
    - 웹 표준을 정확하게 바녕하고 있으며, 신뢰할 수 있는 정보 소스를 제공

2. 최신 웹 기술
    - 최신 웹 표준과 기술을 다루고 이썽, 웹 개발자들이 최신 정보를 쉽게 접할 수 있음

3. 명확한 설명과 예제
    - 복잡한 개념을 이해하기 쉽게 설명하고, 실습 가능한 예제 코드를 제공

### MDN 문서의 중요성

- MDN 문서는 엡 개발 학습의 모든 단계에서 중요한 참고 자료
- 개발 과정에서 발생하는 다양한 문제에 대한 솔루션을 찾는 데 유용
- 이 문서를 활용함으로써, 웹 기술에 대한 깊은 이해를 얻고, 실무에 필요한 능력을 갖출 수 있음

> TIP   
>   
> - 페이지 하단의 '브라우저 호환성' 표를 꼭 확인해서, 내가 쓸 기술의 지원 범위를 파악하기
> - 기술명 옆 'Deprecated(폐기 예정)' 같은 표시를 꼭 확인하는 습관을 들이기
> - OpenAI가 최신 버전을 반드시 반영하는 게 아니기 때문에 직접 실습하며 공부해보기

