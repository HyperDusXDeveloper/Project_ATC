import pandas as pd
import matplotlib.pyplot as plt

# Load historical stock data
df_stock = pd.read_csv('amzn_historical_data.csv')
df_stock['Date'] = pd.to_datetime(df_stock['Date'])
df_stock = df_stock.sort_values(by='Date')

# Plotting stock price
plt.figure(figsize=(14, 7))
plt.plot(df_stock['Date'], df_stock['Close'], label='ราคาปิด (USD)')
plt.title('ราคาปิดหุ้น Amazon (AMZN) ในอดีต')
plt.xlabel('วันที่')
plt.ylabel('ราคาปิด (USD)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('amzn_stock_price.png')
plt.close()

# Plotting trading volume
plt.figure(figsize=(14, 7))
plt.bar(df_stock['Date'], df_stock['Volume'], color='skyblue')
plt.title('ปริมาณการซื้อขายหุ้น Amazon (AMZN) ในอดีต')
plt.xlabel('วันที่')
plt.ylabel('ปริมาณการซื้อขาย')
plt.grid(True)
plt.tight_layout()
plt.savefig('amzn_trading_volume.png')
plt.close()

print('กราฟราคาหุ้นและปริมาณการซื้อขายถูกสร้างขึ้นเรียบร้อยแล้ว')
