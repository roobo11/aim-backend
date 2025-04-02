# AIM 백엔드 코딩 테스트 API

자문 및 증권 기반 포트폴리오 API 서버입니다.

---

## 🧰 개발 환경
- Python 3.9 이상
- Django 4.x
- MySQL 8.x
- 가상환경: `venv`

## 🧪 설치 및 실행

```bash
git clone <레포주소>
cd aim-backend

# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 라이브러리 설치
pip install -r requirements.txt

# 환경 설정 파일 (.env)
cp env/.env.example env/.env  # 또는 직접 작성

# 마이그레이션 및 실행
python manage.py migrate
python manage.py runserver
```

## 📌 주요 기능

| 기능 | 설명 |
|------|------|
| 회원가입/로그인 | JWT 인증 기반 |
| 입출금 | 금액 증감 및 트랜잭션 기록 |
| 잔고조회 | 현재 원화 잔액 확인 |
| 자문 요청 | 위험도 기반 증권 배분 포트폴리오 생성 |
| 포트폴리오 조회 | 본인 포트폴리오 및 구성 증권 조회 |
| 증권 관리 | 증권 등록/수정/삭제 |


## 🧾 API 문서 (Swagger)
- Swagger UI: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- Redoc UI: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

> 모든 API는 Bearer Token (JWT) 인증 필요 (회원가입/로그인 제외)

---

## 📂 프로젝트 구조

```plaintext
├── aim/              # .env 설정 보관 디렉토리
├── coding_test/      # Django 프로젝트 루트
├── accounts/         # 회원가입, 로그인, 입출금 기능
├── advice/           # 자문 로직, 포트폴리오 구성/조회
├── securities/       # 증권 CRUD 관리
└── manage.py
```
