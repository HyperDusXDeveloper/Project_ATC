import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import ta  # Pandas TA Library

# ดึงข้อมูลราคาหุ้น
def fetch_data(ticker, period="1y", interval="1d"):
    df = yf.download(ticker, period=period, interval=interval)
    df['Date'] = df.index
    df.reset_index(drop=True, inplace=True)
    return df

# คำนวณตัวชี้วัด
def calculate_indicators(df):
    # MACD (12, 26, 9)
    macd = ta.trend.MACD(df['Close'], window_slow=26, window_fast=12, window_sign=9)
    df['MACD'] = macd.macd().iloc[:, 0]  # ใช้ iloc เพื่อดึงคอลัมน์แรก
    df['Signal'] = macd.macd_signal().iloc[:, 0]

    # EMA (50, 100, 200)
    df['EMA_50'] = ta.trend.ema_indicator(df['Close'], window=50)
    df['EMA_100'] = ta.trend.ema_indicator(df['Close'], window=100)
    df['EMA_200'] = ta.trend.ema_indicator(df['Close'], window=200)

    # RSI (6, 14, 24)
    df['RSI_6'] = ta.momentum.rsi(df['Close'], window=6)
    df['RSI_14'] = ta.momentum.rsi(df['Close'], window=14)
    df['RSI_24'] = ta.momentum.rsi(df['Close'], window=24)

    return df

# วิเคราะห์จุดกลับตัว
def find_reversal_points(df):
    df['Reversal'] = np.where(
        (df['MACD'] > df['Signal']) & 
        (df['Close'] > df['EMA_50']) &
        (df['RSI_14'] > 50),  # เงื่อนไขจุดกลับตัว
        'Bullish',
        np.where(
            (df['MACD'] < df['Signal']) &
            (df['Close'] < df['EMA_50']) &
            (df['RSI_14'] < 50),
            'Bearish',
            'None'
        )
    )
    return df

# แสดงกราฟ
def plot_reversal(df):
    plt.figure(figsize=(14, 7))

    # ราคาปิด
    plt.plot(df['Date'], df['Close'], label='Close Price', color='blue', alpha=0.6)

    # EMA
    plt.plot(df['Date'], df['EMA_50'], label='EMA 50', color='green', linestyle='--', alpha=0.7)
    plt.plot(df['Date'], df['EMA_100'], label='EMA 100', color='orange', linestyle='--', alpha=0.7)
    plt.plot(df['Date'], df['EMA_200'], label='EMA 200', color='red', linestyle='--', alpha=0.7)

    # จุดกลับตัว
    bullish = df[df['Reversal'] == 'Bullish']
    bearish = df[df['Reversal'] == 'Bearish']
    plt.scatter(bullish['Date'], bullish['Close'], label='Bullish Reversal', color='green', marker='^', s=100)
    plt.scatter(bearish['Date'], bearish['Close'], label='Bearish Reversal', color='red', marker='v', s=100)

    # ตั้งค่ากราฟ
    plt.title('Price and Reversal Points')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()

# ดำเนินการทั้งหมด
if __name__ == "__main__":
    ticker = "AAPL"  # ใส่ชื่อหุ้นที่ต้องการ เช่น AAPL (Apple)
    df = fetch_data(ticker)
    df = calculate_indicators(df)
    df = find_reversal_points(df)
    plot_reversal(df)
