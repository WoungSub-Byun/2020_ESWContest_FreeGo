API 명세
=
초기 테이블 생성
-
``` 
    GET /init
```
- Request
```
```
- Response
```
{
    SUCCESS { "code" : 200, "message": "init success" }
    FAIL { "code" : 400, "message" : "fail" }
}
```

재료 목록 조회
-
```
    POST /show
```
- Request
```
{
    "id": "내 냉장고1"
}
```
- Response
```
    SUCCESS { "code": 200,
            "data": [
                {
                    "id": "내 냉장고1",
                    "p_ex_date": "Mon, 31 Aug 2020 00:00:00 GMT",
                    "p_name": "가지",
                    "p_number": 4
                }, ...
            ],
            "message" : "select success"
    }

    FAIL { "code" : 404, "message" : "fail" }
```
재료 존재여부 확인
-
``` 
    POST /find
```
- Request
```
{
    "id" : "내 냉장고1",
    "p_name" : "동원참치"
}
```
- Response
```
{
    SUCCESS { "code" : 200, "message": "find success" }
    FAIL { "code" : 400, "message" : "fail" }
}
```

유통기한 지난 재료 조회
-
```
    POST /late
```
- Request
```
{
    "id" : "내 냉장고1"
}
```
- Response
```
    SUCCESS {"code": 200,
            "data": [
                {
                    "id" : "내 냉장고1",
                    "p_ex_date" : "Mon, 31 Aug 2020 00:00:00 GMT",
                    "p_name": "가지",
                    "p_number" : 4
                }, ...
            ],
            "message" : "select success"
    }

    FAIL { "code" : 404, "message" : "fail" }
```

재료 추가
-
```
    POST /insert
```
- Request
```
{
    "id" : "내 냉장고1",
    "p_name" : "가지",
    "p_number" : 3, #양수
    "p_ex_date" : 20230807
}
```
- Response
```
    SUCCESS { "code": 200, "message": "insert success" }
    FAIL { "code": 404, "message": "fail" }
    FAIL { "code": 404, "message": "already exist" }
```
재료 수량 수정
-
```
    POST /update
```
- Request
```
{
    "id" : "내 냉장고1",
    "p_name" : "오이",
    "p_number" : 5
}
```
- Response
```
    SUCCESS { "code": 200, "message": "update success" }
    FAIL { "code": 404, "message": "fail" }
```
재료 삭제
-
```
    POST /delete
```
- Request
```
{
    "id" : "내 냉장고1",
    "p_name" : "동원참치"
}
```
- Response
```
    SUCCESS { "code": 200, "message": "delete success" }
    FAIL { "code": 404, "message": "fail" }
```
바코드정보로 상품정보 조회
-
```
    POST /lookupcode
```
- Request
```
{
    "gtin": 0000000000000 #13자리수
}
```
- Response
```
    SUCCESS {"code": 200,
            "data": [
                "0000000000000",       #gtin정보
                "동원참치",             #상품이름, 정보
                "(주)동원",             #만든 회사
                "KOREA, REPUBLIC OF",  #원산지 정보
                "http://이미지링크"     #상품이미지링크
            ],
            "message" : "success"
    }
    FAIL { "code": 404, "message": "fail" }
```