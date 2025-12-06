
# 📈 NiftyBot: Nifty Gap Up/Down Predictor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![Status](https://img.shields.io/badge/Status-Active-success)

**NiftyBot** is a Machine Learning-powered dashboard built with Streamlit that predicts the opening direction (Gap Up or Gap Down) of the **Nifty 50 Index**. It analyzes real-time global market cues, technical indicators, and historical data to provide an early morning forecast for traders.

## 🚀 Key Features

* **Live Data Integration:** Automatically fetches real-time data for Nifty, US Indices (S&P 500, Nasdaq), and major Indian stocks (Reliance, HDFC, etc.) using `yfinance`.
* **Global Cues Analysis:** Considers the impact of Asian Markets (Nikkei, Hang Seng, Kospi) and commodities (Crude Oil, Gold).
* **Technical Indicators:** Calculates RSI (14) and EMA (12) on the fly for better prediction accuracy.
* **Interactive Interface:** Simple, user-friendly dashboard to input pre-market Asian cues manually if needed.
* **ML Prediction:** Uses a pre-trained classification model (`niftyPred.pkl`) to generate Buy/Sell signals.

## 🛠️ Tech Stack

* **Python** (Logic & Data Processing)
* **Streamlit** (Frontend Dashboard)
* **Scikit-Learn** (Machine Learning Model)
* **yfinance** (Market Data API)
* **TA-Lib** (Technical Analysis Library)
* **Pandas & NumPy** (Data Manipulation)

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/hk12maddheshiya/NiftyBot.git](https://github.com/hk12maddheshiya/NiftyBot.git)
    cd NiftyBot
    ```

2.  **Install dependencies**
    Make sure you have Python installed, then run:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If you don't have a `requirements.txt`, install manually: `pip install streamlit pandas numpy yfinance ta scikit-learn`)*

3.  **Place the Model File**
    Ensure the trained model file `niftyPred.pkl` is present in the root directory.

4.  **Run the App**
    ```bash
    streamlit run app.py
    ```

## 📊 How It Works

The model takes a vector of inputs to make a prediction. The workflow is as follows:

1.  **Nifty Data:** Fetches OHLC data, calculates `RSI_14`, `EMA_12`, and `Percentage Change`.
2.  **Stock Watch:** Fetches daily changes for top heavyweights (Reliance, HDFC, ICICI, Infosys, TCS).
3.  **Global Sentiment:** Fetches US Market close data (S&P 500, Nasdaq, Dow Jones).
4.  **Asian & Commodities:** Takes user input or live fetches for Nikkei, Hang Seng, Kospi, Crude Oil, and Gold.
5.  **Prediction:** The aggregated data is passed to the ML model, which outputs:
    * 🟢 **Gap Up**
    * 🔴 **Gap Down**

## 📂 Project Structure
This is a professional, ready-to-use README.md file based on the code and context you provided.

I have structured it to explain what the project does, how to run it, and the logic behind the prediction.

📋 Instructions
Go to your GitHub repository (NiftyBot).

Click Add file > Create new file.

Name the file: README.md

Copy and paste the code block below into that file.

Click Commit changes.

Markdown

# 📈 NiftyBot: Nifty Gap Up/Down Predictor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![Status](https://img.shields.io/badge/Status-Active-success)

**NiftyBot** is a Machine Learning-powered dashboard built with Streamlit that predicts the opening direction (Gap Up or Gap Down) of the **Nifty 50 Index**. It analyzes real-time global market cues, technical indicators, and historical data to provide an early morning forecast for traders.

## 🚀 Key Features

* **Live Data Integration:** Automatically fetches real-time data for Nifty, US Indices (S&P 500, Nasdaq), and major Indian stocks (Reliance, HDFC, etc.) using `yfinance`.
* **Global Cues Analysis:** Considers the impact of Asian Markets (Nikkei, Hang Seng, Kospi) and commodities (Crude Oil, Gold).
* **Technical Indicators:** Calculates RSI (14) and EMA (12) on the fly for better prediction accuracy.
* **Interactive Interface:** Simple, user-friendly dashboard to input pre-market Asian cues manually if needed.
* **ML Prediction:** Uses a pre-trained classification model (`niftyPred.pkl`) to generate Buy/Sell signals.

## 🛠️ Tech Stack

* **Python** (Logic & Data Processing)
* **Streamlit** (Frontend Dashboard)
* **Scikit-Learn** (Machine Learning Model)
* **yfinance** (Market Data API)
* **TA-Lib** (Technical Analysis Library)
* **Pandas & NumPy** (Data Manipulation)

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/hk12maddheshiya/NiftyBot.git](https://github.com/hk12maddheshiya/NiftyBot.git)
    cd NiftyBot
    ```

2.  **Install dependencies**
    Make sure you have Python installed, then run:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If you don't have a `requirements.txt`, install manually: `pip install streamlit pandas numpy yfinance ta scikit-learn`)*

3.  **Place the Model File**
    Ensure the trained model file `niftyPred.pkl` is present in the root directory.

4.  **Run the App**
    ```bash
    streamlit run app.py
    ```

## 📊 How It Works

The model takes a vector of inputs to make a prediction. The workflow is as follows:

1.  **Nifty Data:** Fetches OHLC data, calculates `RSI_14`, `EMA_12`, and `Percentage Change`.
2.  **Stock Watch:** Fetches daily changes for top heavyweights (Reliance, HDFC, ICICI, Infosys, TCS).
3.  **Global Sentiment:** Fetches US Market close data (S&P 500, Nasdaq, Dow Jones).
4.  **Asian & Commodities:** Takes user input or live fetches for Nikkei, Hang Seng, Kospi, Crude Oil, and Gold.
5.  **Prediction:** The aggregated data is passed to the ML model, which outputs:
    * 🟢 **Gap Up**
    * 🔴 **Gap Down**

## 📂 Project Structure

NiftyBot/ ├── app.py # Main Streamlit application code ├── niftyPred.pkl # Trained Machine Learning Model ├── requirements.txt # List of python dependencies └── README.md # Project Documentation


## 🔮 Future Improvements

* [ ] Add chart visualizations for the past 5 days trend.
* [ ] Automate the fetching of live Asian market data (removing manual input).
* [ ] Add "Neutral/Flat" opening prediction class.
* [ ] deploy on Streamlit Cloud.

<img width="1919" height="877" alt="image" src="https://github.com/user-attachments/assets/4b7616a2-6ea7-48e6-8496-1fa1de90209d" />
<img width="1917" height="865" alt="image" src="https://github.com/user-attachments/assets/186956ee-76ca-44c5-9353-c625338d7ccf" />

