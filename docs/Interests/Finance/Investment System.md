# Investment System


Sources of info

Fundamental
- Valuation
	- ROCE
	- 1Y Revenue Growth vs 3Y vs 5Y Revenue Growth
	- 1Y EBITDA change vs 3Y vs 5Y EBITDA Change 
	- PE vs Sector PE
- Solvency
	- Debt vs Long Term Debt
	- Working Capital 
	- Debtor Days
- Accounting
	- Receivable Days
	- Profit Margin  Quarter vs Year vs Previous year

Price Action
- Volume
- Spread  52W high vs low
- Pivot Points
- Markov movement prediction
- Last Breakout since
- Event Sensitivity

Derived Market
- OI
- Change in OI
- Long, vs Long unwinding
- Short vs Short unwinding


Derived Speculative
- Analyst Reports
- News
- Mutual Fund holdings Change
- Court Cases
- Events
- Law changes in sector - domestic
- Law changes in sector - international
- Large Tender or Contract

Website Data
- Trendyline
- Quantsapp
- Screener
- tickertape
- moneycontrol
- Google Dork 
	- HDFC
		- inurl:https://www.hdfcsec.com/hsl.research.pdf/ & after:2023-06-06 & intext:"Techno Funda"

Trigger Events
- Upcoming Result
- Upcoming court case in news
- Merger news
- new contract/deal news

Supplier Ranking
- [Metoree | Search Manufacturers and Suppliers](https://us.metoree.com/)
- 


## Stocks
- Smallcap
	- Fact Sheet: [[Stocks/SBCL_ShivalikBimetal]]
	- Fact Sheet: [[Stocks/ERIS-ErisLifesciencesLtd]]   Current: 879,  Target: 998 to 1011, Stop: 865
	- [Oil India Ltd Share Price Today - Oil India Ltd Share Price LIVE on NSE/BSE](https://www.tickertape.in/stocks/oil-india-OILI) 
	- Linde India
	- Mishtaan
	- Varun Beverages
	
- Unverified
	- [Laurus Labs Ltd Share Price Today - Laurus Labs Ltd Share Price LIVE on NSE/BSE](https://www.tickertape.in/stocks/laurus-labs-LAUL#overview)
	- [Granules India Ltd Share Price Today - Granules India Ltd Share Price LIVE on NSE/BSE](https://www.tickertape.in/stocks/granules-india-GRAN?ref=screener-table_int-asset-widget)
	- [Laurus Labs Ltd Share Price Today - Laurus Labs Ltd Share Price LIVE on NSE/BSE](https://www.tickertape.in/stocks/laurus-labs-LAUL#overview)





Research Prompts

You are a research analyst for a hedge fund and do thorough fundamental analysis of companies based in and traded in India. 
You provide a summary of the company under the following headings. Each summary section presents your understanding, the  strengths and the weaknesses as per your assement. 
The headings for your analysis are 
```
## Management 
## Capacity Building 
## Revenue, Sales, Profit Growth 
## Challenges 
## Debt & Credit Rating 

## Upcoming News: in and after Q4/2023 
### JV 
### MOUs ### Tenders ### Technology Transfer ### Merger & Acquisitions

```
Do you understand?


#### Stock data

Alpha Vantage:  `M72H2PC6CO1ZQS0F`
User: `arvind@devnullmail.com`

Yahoo Finance
> [Remote Data Access — pandas-datareader 0.10.0 documentation](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html)
```python
from pandas_datareader import get_data_yahoo as data  
a = data(’^NSEI’,‘2010-01-01’,‘2020-10-01’) 
```

IEXAPIs.com  [API Url](https://cloud.iexapis.com/stable/ref-data/region/in/symbols?token=API-KEY)
FMPCloud   [API Url](https://fmpcloud.io/api/v3/historical-price-full/HDFC.NS?from=2018-03-12&to=2019-03-12&apikey=API-KEY)
Unibit.ai  [API Url](https://api.unibit.ai/v2/stock/historical?tickers=RELIANCE.NS&selectedFields=all&startDate=2021-06-15&endDate=2021-06-20&dataType=json&accessKey=API-KEY)
