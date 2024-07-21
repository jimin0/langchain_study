import streamlit as st
import pandas as pd
import numpy as np


st.title("다양한 데이터 보여주기")

# DataFrame 생성 -> 많이쓰기
st.subheader("DataFrame 보여주기 - download, searching, full screen, sorting 가능")
dataframe = pd.DataFrame(
    {
        "first column": [1, 2, 3, 4],
        "second column": [10, 20, 30, 40],
    }
)

# DataFrame
# use_container_width 기능은 데이터프레임을 컨테이너 크기에 확장할 때 사용합니다. (True/False)

st.dataframe(dataframe, use_container_width=True)


# 테이블(static)
# DataFrame과는 다르게 interactive 한 UI 를 제공하지 않습니다.
st.subheader("Table 보여주기 - on screen 기능없음")
st.table(dataframe)


# # 메트릭
st.subheader("Metric 보여주기")
st.metric(label="온도", value="10°C", delta="1.2°C")

# ----------------------------------------------
st.subheader("현재 LG전자 주가")
# LG전자 주가 가져오기
import yfinance as yf

# LG전자 티커 심볼
ticker_symbol = "066570.KS"
# LG전자 주식 정보 가져오기
samsung_stock = yf.Ticker(ticker_symbol)

# 최근 5일간의 주가 정보 가져오기
stock_history = samsung_stock.history(period="5d")
# 원단위로 반올림
stock_history = stock_history.round(0)
st.table(stock_history)

# 현재 주가 및 전날 주가 가져오기
current_price = stock_history["Close"][-1]
previous_price = stock_history["Close"][-2]

# 전날 대비 가격 변화 계산
price_change = current_price - previous_price
percentage_change = (price_change / previous_price) * 100

# Streamlit 앱 시작

st.metric(
    label="LG전자", value=current_price, delta=price_change, delta_color="normal"
)

# ----------------------------------------------

# 환율 티커 심볼 설정
tickers = {"USD/KRW": "KRW=X", "JPY/KRW": "KRWJPY=X", "EUR/KRW": "EURKRW=X"}

# 환율 정보 가져오기
rates = {}
previous_rates = {}

for ticker_name, ticker_symbol in tickers.items():
    ticker = yf.Ticker(ticker_symbol)
    history = ticker.history(period="5d")

    current_rate = history["Close"][-1]
    previous_rate = history["Close"][-2]

    # JPY/KRW의 경우 100엔당 원화로 변환
    if ticker_name == "JPY/KRW":
        current_rate *= 100
        previous_rate *= 100

    rates[ticker_name] = current_rate
    previous_rates[ticker_name] = previous_rate

# Streamlit 앱 시작
st.subheader("현재 환율 정보")

# 3개의 컬럼 생성
col1, col2, col3 = st.columns(3)

# 각 컬럼에 환율 정보 지정
with col1:
    ticker_name = "USD/KRW"
    current_rate = rates[ticker_name]
    previous_rate = previous_rates[ticker_name]
    rate_change = current_rate - previous_rate
    percentage_change = (rate_change / previous_rate) * 100

    st.metric(
        label=ticker_name,
        value=f"{current_rate:.2f} KRW",
        delta=f"{rate_change:.2f} KRW ({percentage_change:.2f}%)",
        delta_color="normal",
    )

with col2:
    ticker_name = "JPY/KRW"
    current_rate = rates[ticker_name]
    previous_rate = previous_rates[ticker_name]
    rate_change = current_rate - previous_rate
    percentage_change = (rate_change / previous_rate) * 100

    st.metric(
        label=f"{ticker_name} (100엔당)",
        value=f"{current_rate:.2f} KRW",
        delta=f"{rate_change:.2f} KRW ({percentage_change:.2f}%)",
        delta_color="normal",
    )

with col3:
    ticker_name = "EUR/KRW"
    current_rate = rates[ticker_name]
    previous_rate = previous_rates[ticker_name]
    rate_change = current_rate - previous_rate
    percentage_change = (rate_change / previous_rate) * 100

    st.metric(
        label=ticker_name,
        value=f"{current_rate:.2f} KRW",
        delta=f"{rate_change:.2f} KRW ({percentage_change:.2f}%)",
        delta_color="normal",
    )

# ----------------------------------------------
import plotly.graph_objects as go


# 주식 그래프 추가
st.subheader("LG전자 주가 그래프")

# LG전자 주식 정보 가져오기 (1년 데이터)
lg_stock = yf.Ticker("066570.KS")
stock_data = lg_stock.history(period="1y")

# Plotly를 사용하여 캔들스틱 차트 생성
fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                open=stock_data['Open'],
                high=stock_data['High'],
                low=stock_data['Low'],
                close=stock_data['Close'])])

# 레이아웃 설정
fig.update_layout(
    title='LG전자 주가 (1년)',
    yaxis_title='주가 (원)',
    xaxis_rangeslider_visible=False
)

# Streamlit에 그래프 표시
st.plotly_chart(fig, use_container_width=True)