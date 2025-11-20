import pandas as pd
import matplotlib.pyplot as plt

# Load financial data
df_income = pd.read_csv("amzn_income_statement_annual.csv")
df_balance = pd.read_csv("amzn_balance_sheet_annual.csv")
df_cashflow = pd.read_csv("amzn_cash_flow_annual.csv")

# Prepare data for plotting (annual income statement)
revenue = df_income[df_income["Metric"] == "Total Revenue"].iloc[0, 1:].astype(float)
gross_profit = df_income[df_income["Metric"] == "Gross Profit"].iloc[0, 1:].astype(float)
operating_income = df_income[df_income["Metric"] == "Operating Income"].iloc[0, 1:].astype(float)
net_income = df_income[df_income["Metric"] == "Net Income Common Stockholders"].iloc[0, 1:].astype(float)

years_income = df_income.columns[1:].tolist()

# Plotting Income Statement
plt.figure(figsize=(14, 7))
plt.plot(years_income, revenue, label='รายได้รวม', marker='o')
plt.plot(years_income, gross_profit, label='กำไรขั้นต้น', marker='o')
plt.plot(years_income, operating_income, label='กำไรจากการดำเนินงาน', marker='o')
plt.plot(years_income, net_income, label='กำไรสุทธิ', marker='o')
plt.title('งบกำไรขาดทุนประจำปีของ Amazon (หน่วย: พันล้าน USD)')
plt.xlabel('ปี')
plt.ylabel('จำนวนเงิน (พันล้าน USD)')
plt.ticklabel_format(style='plain', axis='y')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('amzn_income_statement.png')
plt.close()

# Prepare data for plotting (annual balance sheet)
total_assets = df_balance[df_balance["Metric"] == "Total Assets"].iloc[0, 1:].astype(float)
total_liabilities = df_balance[df_balance["Metric"] == "Total Liabilities Net Minority Interest"].iloc[0, 1:].astype(float)
total_equity = df_balance[df_balance["Metric"] == "Total Equity Gross Minority Interest"].iloc[0, 1:].astype(float)

years_balance = df_balance.columns[1:].tolist()

# Plotting Balance Sheet
plt.figure(figsize=(14, 7))
plt.plot(years_balance, total_assets, label='สินทรัพย์รวม', marker='o')
plt.plot(years_balance, total_liabilities, label='หนี้สินรวม', marker='o')
plt.plot(years_balance, total_equity, label='ส่วนของผู้ถือหุ้นรวม', marker='o')
plt.title('งบดุลประจำปีของ Amazon (หน่วย: พันล้าน USD)')
plt.xlabel('ปี')
plt.ylabel('จำนวนเงิน (พันล้าน USD)')
plt.ticklabel_format(style='plain', axis='y')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('amzn_balance_sheet.png')
plt.close()

# Prepare data for plotting (annual cash flow)
operating_cash_flow = df_cashflow[df_cashflow["Metric"] == "Operating Cash Flow"].iloc[0, 1:].astype(float)
investing_cash_flow = df_cashflow[df_cashflow["Metric"] == "Investing Cash Flow"].iloc[0, 1:].astype(float)
financing_cash_flow = df_cashflow[df_cashflow["Metric"] == "Financing Cash Flow"].iloc[0, 1:].astype(float)
free_cash_flow = df_cashflow[df_cashflow["Metric"] == "Free Cash Flow"].iloc[0, 1:].astype(float)

years_cashflow = df_cashflow.columns[1:].tolist()
print("Hello World")
# Plotting Cash Flow Statement
plt.figure(figsize=(14, 7))
plt.plot(years_cashflow, operating_cash_flow, label='กระแสเงินสดจากการดำเนินงาน', marker='o')
plt.plot(years_cashflow, investing_cash_flow, label='กระแสเงินสดจากการลงทุน', marker='o')
plt.plot(years_cashflow, financing_cash_flow, label='กระแสเงินสดจากกิจกรรมจัดหาเงิน', marker='o')
plt.plot(years_cashflow, free_cash_flow, label='กระแสเงินสดอิสระ', marker='o')
plt.title('งบกระแสเงินสดประจำปีของ Amazon (หน่วย: พันล้าน USD)')
plt.xlabel('ปี')
plt.ylabel('จำนวนเงิน (พันล้าน USD)')
plt.ticklabel_format(style='plain', axis='y')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('amzn_cash_flow.png')
plt.close()

print('กราฟข้อมูลทางการเงินถูกสร้างขึ้นเรียบร้อยแล้ว')