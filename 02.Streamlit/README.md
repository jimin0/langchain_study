# 🔗 LangChain Study: 02.Streamlit

이 폴더는 LangChain과 Streamlit을 활용한 다양한 애플리케이션 개발 실습 파일들을 포함하고 있습니다.

## 📅 학습 기간
- 시작일: 2024.07.05
- 종료일: 2024.07.07

## 📁 폴더 및 파일 구조

### prompts
- `insta.yaml`: Instagram 스타일의 프롬프트 설정 (🔗 99.chatbot.py에 사용)
- `naver.yaml`: 네이버 블로그 스타일의 프롬프트 설정 (🔗 99.chatbot.py에 사용)
- `sns.yaml`: 일반 SNS 스타일의 프롬프트 설정
- `tech_blog.yaml`: 기술 블로그 스타일의 프롬프트 설정 (🔗 99.chatbot.py에 사용)
- `twitter.yaml`: Twitter 스타일의 프롬프트 설정 (🔗 99.chatbot.py에 사용)

###  Python 파일
1. `00-test.py` & `00-text.py`: 초기 테스트 및 텍스트 처리 예제
2. `01-candle.py` & `01-data.py`: 캔들차트 및 데이터 처리 예제
3. `02-basic-ui.py`: Streamlit 기본 UI 구성 예제
4. `03-lotto.py`: 로또 번호 생성기 예제
5. `04-appl.py` & `04-chart.py`:lg 전자 주식 데이터 처리 및 차트 생성 예제
6. `05-csv-xls-file.py`: CSV 및 Excel 파일 처리 예제
7. `06-chatbot.py`, `06-chatbot2.py`, `06-chatbot3.py`, `06-main.py`: 챗봇 구현 예제들
8. `07-chatbot.py` & `07-chatbot2.py`: 고급 챗봇 구현 예제
9. `99-chatbot.py`: 최종 챗봇 프로젝트 (SNS 최적화 : 인스타, 트위터 바이럴계, 네이버, 기술블로그 자동 작성 기능)

## 🎯 목적

이 폴더의 목적은 Streamlit을 활용하여 LangChain 기반의 다양한 애플리케이션을 개발하는 실습을 수행하는 것입니다. 
기본적인 UI 구성부터 복잡한 챗봇 시스템까지, 단계별로 Streamlit과 LangChain의 기능을 학습하고 적용합니다.

1. Streamlit을 이용한 웹 애플리케이션 구축
2. 다양한 데이터 형식(CSV, Excel) 처리 및 시각화
3. 금융 데이터 분석 및 차트 생성
4. LangChain을 활용한 챗봇 시스템 구현
5. YAML 파일을 이용한 프롬프트 관리 및 커스터마이징

## 🚀 시작하기

**설치**
```python
pip install streamlit
```
**실행**
```python
streamlit run [파일이름.py]
```


## 📚 참고 자료

- [Streamlit 공식 문서](https://docs.streamlit.io/)
- [LangChain 공식 문서](https://python.langchain.com/v0.2/docs/introduction/)
- [EP01. Streamlit으로 빠르게 웹앱 생성하기 - 설치, 환경설정, 실습파일](https://www.youtube.com/watch?v=Gr5Vuo7TCaE)
- [EP02. 텍스트 컴포넌트](https://youtu.be/CiOfNvp-KmA)
- [EP03. 데이터프레임(DataFrame), 테이블 출력](https://youtu.be/C73XAQJFa1E)
- [EP04. 자주 사용하는 위젯(Widgets)들](https://youtu.be/3CWpFR-EkQc)
- [EP05. 로또 생성기 웹사이트 만들기](https://youtu.be/2mER-EvDWzo)
- [EP06. 그래프, 차트 그리기](https://youtu.be/2424N7ITZvo)
- [EP07. 파일 업로드 기능 & 업로드된 파일 처리](https://youtu.be/L3ExMrinu20)
- [EP08. 주식 데이터 조회, 주가 차트 그리기](https://youtu.be/0PA3XsPwPDg)
- [EP09. 사이드바, 탭 추가하기](https://youtu.be/frdggOd5eNQ)
- [EP10. MBTI 대백과사전 웹앱 만들기 (NAVER Clova API 활용)](https://youtu.be/2tT8-peVTLw)
- [EP11. Naver Clova Studio API를 활용한 챗봇 서비스 만들기](https://youtu.be/sLTe2jMGdYU)
- [EP12. 기업의 평균 월급여, 연봉 추정하기 (국민연금 데이터 활용)](https://youtu.be/-CMZKaoX5Og)
- [EP13. 기업의 월급여, 연봉 추정 서비스 제작 & 웹으로 배포 (무료 호스팅)](https://youtu.be/OpeECxk5c-Q)