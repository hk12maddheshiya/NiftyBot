import streamlit as st
import pickle
import pandas as pd
import yfinance as yf
from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator
import numpy as np

st.set_page_config(page_title="GapUp Predictor", layout="centered")
st.title("📈 Nifty Gap Up/Down Predictor")

FEATURE_COLUMNS = [
    'Open', 'Close', 'High', 'Low', 'Volume',
    'percentage_change', 'RSI_14', 'EMA_12',
    'Reliance', 'HDFC', 'ICICI', 'Infosys', 'TCS',
    'SP500', 'Nasdaq', 'DowJones',
    'Nikkei', 'HangSeng', 'Kospi', 'CrudeOil', 'Gold', 'USDINR'
]

@st.cache_resource
def load_model():
    return pickle.load(open("niftyPred.pkl", "rb"))
   

model = load_model()

st.subheader("1. Enter Global Market Cues")
col1, col2, col3 = st.columns(3)
with col1:
    nikkei_open = st.number_input("Nikkei 225 Open", value=0.0)
    crude_chg = st.number_input("Crude Oil % Change", value=0.0)
with col2:
    hangseng_open = st.number_input("Hang Seng Open", value=0.0)
    gold_chg = st.number_input("Gold % Change", value=0.0)
with col3:
    kospi_open = st.number_input("Kospi / Gift Nifty Open", value=0.0)
    usd_chg = st.number_input("USD/INR % Change", value=0.0)

def asianData(nikkei_open, hangseng_open, kospi_open):
    
   
    nk_df = yf.download("^N225", period="5d", progress=False)
    hs_df = yf.download("^HSI", period="5d", progress=False)
    ks_df = yf.download("^KS11", period="5d", progress=False)

    
    nikkei_base   = nk_df['Close'].tail(2).iloc[0].item()
    hangseng_base = hs_df['Close'].tail(2).iloc[0].item()
    kospi_base    = ks_df['Close'].tail(2).iloc[0].item()

    # 3. Calculation
    nikkei_pct   = (nikkei_open - nikkei_base) / nikkei_base * 100
    hangseng_pct = (hangseng_open - hangseng_base) / hangseng_base * 100
    kospi_pct    = (kospi_open - kospi_base) / kospi_base * 100

    return nikkei_pct, hangseng_pct, kospi_pct
def get_historical_data(ticker, period="60d"):
    try:
        data = yf.Ticker(ticker).history(period=period)
        return data
    except Exception:
        return pd.DataFrame()

def get_nifty_features():
    df = get_historical_data("^NSEI")
    
    if df.empty:
        return None

    df["rsi"] = RSIIndicator(df["Close"], window=14).rsi()
    df["ema12"] = EMAIndicator(df["Close"], window=12).ema_indicator()
    df["pct"] = (df["Close"] - df["Open"]) / df["Close"] * 100
    
    last = df.iloc[-1]
    
    return [
        last["Open"], last["Close"], last["High"], last["Low"], last["Volume"],
        last["pct"], last["rsi"], last["ema12"]
    ]

if st.button("Fetch Data & Predict"):
    with st.spinner("Fetching live market data..."):
        
        nifty_data = get_nifty_features()
        
        if nifty_data is None:
            st.error("Failed to fetch Nifty data.")
            st.stop()

        tickers_map = [
            ("Reliance", "RELIANCE.NS"),
            ("HDFC", "HDFCBANK.NS"),
            ("ICICI", "ICICIBANK.NS"),
            ("Infosys", "INFY.NS"),
            ("TCS", "TCS.NS"),
            ("SP500", "^GSPC"),
            ("Nasdaq", "^IXIC"),
            ("DowJones", "^DJI")
        ]
        
        asianResults = asianData(nikkei_open, hangseng_open, kospi_open)
        other_market_data = []
        
        for name, code in tickers_map:
            df = get_historical_data(code, period="5d")
            if df.empty:
                other_market_data.append(0.0)
                continue
            
            last = df.iloc[-1]
            val = (last["Close"] - last["Open"]) / last["Close"] * 100
            other_market_data.append(val)

        manual_inputs = [asianResults[0], asianResults[1], asianResults[2], crude_chg, gold_chg, usd_chg]
        
        final_input_vector = nifty_data + other_market_data + manual_inputs
        
        st.subheader("Data used for Prediction")
        df_display = pd.DataFrame([final_input_vector], columns=FEATURE_COLUMNS)
        st.dataframe(df_display)

        if model:
            prediction = model.predict([final_input_vector])
            if prediction == 1:
                st.success(f"### 🚀 Prediction: GAP UP")
            else:
                st.error(f"### 📉 Prediction: GAP DOWN")