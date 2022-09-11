# MySQL With Flask (+ REST API)

Flask 마이크로 웹 프레임워크와 MySQL을 연동하고, Web에서 데이터를 요청할 수 있도록 간단하게 만들어본 예제.  

1. `test_queries`의 파일 실행
   1. 테이블 Create 후 데이터 Insert
2. `.env` 파일 생성

```js
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER= 여기에유저명입력
MYSQL_PASSWORD= 여기에패스워드입력
MYSQL_DATABASE= 여기에DB명입력
MYSQL_CHARSET='utf8'
```

3. `pip` 패키지 설치
   1. `pip install -r requirement.txt
4. `python run.py`

# 실행확인
```python
python3 run.py

 * Serving Flask app "run" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 257-217-951
 ...
```

## 웹 페이지 접속

웹 브라우저에서 `http://localhost:5000/animal/in` 접속  

## API 요청

터미널에서 `CURL`을 사용하여 요청 및 응답 확인.  

```bash
curl -X GET http://localhost:5000/api/animal/in
```
