from finviz.portfolio import Portfolio
from finviz.screener import Screener

# portfolio = Portfolio('bg.mstoev@gmail.com', 'A93JPd8rLbXW8yj')
# portfolio.create_portfolio('TEST', 'portfolio.csv')

stocks = Screener(rows=20)
print(stocks)