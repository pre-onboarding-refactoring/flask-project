# 🎊 flask refactoring project

<br>
<br>

# 🔖 목차

- Team 소개
- 과제 내용
- 서버 주소
- 기술 환경 및 Tools
- 프로젝트 구조
- API 명세서 및 기능 설명
- 설치 및 실행 방법
<br>  
<br>  

# 🧑‍🤝‍🧑 Team 소개
- (팀장)오지윤, 유동헌

| 이름 | 담당 기능 | 블로그 |
| :----------: | :-------------------------------: | :----: |
| 공통 | 초기환경 설정, DB 모델링, UnitTest, 배포, README.md 작성 | X |
| [유동헌](https://github.com/dhhyy)       | 회사명 자동 완성 기능, 회사 추가 기능 |  |            
| [오지윤](https://github.com/Odreystella) | 회사명 디테일 검색 기능, 회사 추가 기능 |  |

- 기능 별로 나누지 않고 모든 API를 함께 Pair Programming으로 구현하였습니다.
<br>
<br>

# 📖 과제 내용

### **[필수 포함 사항]**

- README 작성
  - 프로젝트 빌드, 자세한 실행 방법 명시
  - 구현 방법과 이유에 대한 간략한 설명
  - 완료된 시스템이 배포된 서버의 주소
  - `Swagger`나 `Postman`을 통한 API 테스트할때 필요한 상세 방법
  - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- `Swagger`나 `Postman`을 이용하여 API 테스트 가능하도록 구현

### **[기능 개발]**

✔️ **REST API 기능**

- 회사명 자동완성
  - 회사명의 일부만 들어가도 검색이 되어야 합니다.
- 회사 이름으로 회사 검색
- 새로운 회사 추가
<br>
<br>

# ➡️ Build(AWS EC2)

API URL: http://3.35.218.65:6000/

<br>

# ⚒️ 기술 환경 및 Tools

- Back-End: `Python 3.9.7`, `flask-restx`
- Database: `MySQL` 
- Deploy: `AWS EC2`,
- ETC: `Git`, `Github`, `Swagger`

<br>

# 🌲 프로젝트 구조
```
├── README.md
├── app.py
├── company
│   ├── __init__.py
│   ├── config.py
│   ├── controller.py
│   ├── models.py
│   └── test_app.py
├── db_uploader.py
├── my_settings.py
├── requirements.txt
└── wanted_temp_data.csv
```
<br>

# 🔖 API 명세서

### 회사 상세 정보

1. 회사 이름을 path parameter로 넣은 뒤 header에 원하는 language를 담아줍니다.
2. 만약 header에 language가 없을 경우 기본값으로 ko에 대한 회사를 보여줍니다.
3. 만약 회사가 존재하지 않는 경우 "Company or Language Not Found"라는 에러 메시지를 반환합니다.

- Method: GET
```
http://3.35.218.65:6000/companies/라인 프레쉬
```

- parameter : path parameter

- response 

```
{
  "company_name": "라인 프레쉬",
  "tags": [
    "태그_1",
    "태그_8",
    "태그_15"
  ]
}
```

### 회사 목록 정보

1. query string으로 들어온 데이터가 포함되는 모든 회사의 정보를 조회합니다.
2. 만약 header에 들어온 language를 지원하지 않는 경우 "COUNTRY_NOT_SUPPORTED"라는 에러 메시지를 반환합니다.
3. 만약 query string으로 들어온 데이터를 포함하고 있는 회사가 없을 경우 "COMPANY NOT FOUND"라는 에러 메시지를 반환합니다.

- Method: GET
```
http://3.35.218.65:6000/companies/search?query=원
```

- parameter : query string

- response
```
[
  {
    "company_name": "원티드"
  },
  {
    "company_name": "원할머니"
  }
]
```

### 회사 생성

1. 회사의 이름과 회사가 지원하는 language, 각 회사가 지원하는 언어의 tag를 body에 입력합니다.
2. header에 들어있는 language로 회사가 생성 되지 않았을 경우 "not found country code"라는 에러 메시지를 반환합니다. 


- Method: POST
```
http://3.35.218.65:6000/companies
```

- parameter : request_body, header parameter(fr입력)

```
{
"company_name": {
    "ko": "직방",
    "fr": "straight",
    "ja": "straight"
},
"tags": [
    {
        "tag_name": {
            "ko": "태그10",
            "fr": "tag10",
            "ja": "tag10"
        }
    },
    {
        "tag_name": {
            "ko": "태그20",
            "fr": "tag20",
            "ja": "tag20"
        }
    },
    {
        "tag_name": {
            "ko": "태그30",
            "fr": "tag30",
            "ja": "tag30"
        }
    }
]
}
```

- response   

```
{
    "company_name": "straight",
    "tags": [
        "tag10",
        "tag20",
        "tag30"
    ]
}
```

### refactoring 사항
1. url 관리 위해 namespace atribute를 사용해 refactoring 하였습니다. 
2. flask-restx 사용하여 Swagger 문서화하는 방법 숙지하였습니다. 
3. 전역에 선언되어 있던 app = Flask(__name__) 객체를 팩토리 패턴으로 변경하여 refactoring 하였습니다. 
4. 로컬 DB를 이용하지 않고 TEST DB를 생성해 pytest를 refactoring 하였습니다. 
