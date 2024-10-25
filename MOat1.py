import yfinance as yf

# Fetching stock info for a ticker

ticker = 'AAPL'  # Example: Apple Inc.
stock = yf.Ticker(ticker)

# Get company info
company_info = stock.info
print(company_info['longBusinessSummary'])  # Company description (for moat analysis)
print(company_info['sector'])  # Sector the company belongs to
print(company_info['marketCap'])  # Market Cap (can indicate moat)

# Get financials (income statement, balance sheet, cash flow)
financials = stock.financials
balance_sheet = stock.balance_sheet
cash_flow = stock.cashflow

print(financials)
print(balance_sheet)
print(cash_flow)


