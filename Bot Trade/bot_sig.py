import pandas as pd
import numpy as np
import yfinance
import matplotlib.pyplot as plt
import alpha_vantage
import ccxt

def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    data['EMA_short'] = data['Close'].ewm(span=short_window, adjust=False).mean()
    data['EMA_long'] = data['Close'].ewm(span=long_window, adjust=False).mean()
    data['MACD'] = data['EMA_short'] - data['EMA_long']
    data['Signal_Line'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()
    return data

def find_reversal_points(data):
    data['Reversal'] = np.where(
        (data['MACD'] > data['Signal_Line']) & (data['MACD'].shift(1) <= data['Signal_Line'].shift(1)), 'Bullish', 
        np.where(
            (data['MACD'] < data['Signal_Line']) & (data['MACD'].shift(1) >= data['Signal_Line'].shift(1)), 'Bearish', 
            None
        )
    )
    return data

data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Close': np.cumsum(np.random.randn(100) + 0.5)  # ตัวอย่างข้อมูลสุ่ม
})

data.set_index('Date', inplace=True)

data = calculate_macd(data)
data = find_reversal_points(data)
print(data[['Close', 'MACD', 'Signal_Line', 'Reversal']])
plt.figure(figsize=(14, 7))
plt.plot(data.index, data['Close'], label='Close Price', color='blue')
plt.plot(data.index, data['MACD'], label='MACD', color='green')
plt.plot(data.index, data['Signal_Line'], label='Signal Line', color='red')

bullish = data[data['Reversal'] == 'Bullish']
bearish = data[data['Reversal'] == 'Bearish']
plt.scatter(bullish.index, bullish['Close'], label='Bullish Reversal', color='green', marker='^', alpha=1)
plt.scatter(bearish.index, bearish['Close'], label='Bearish Reversal', color='red', marker='v', alpha=1)

plt.title('MACD and Signal Line with Reversal Points')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()