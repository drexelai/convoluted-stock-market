# convoluted-stock-market


- [x] Pick stock
- [x] Determine benchmark to beat  (SPY, sectors, buy and hold)
- [x] Determine the sample data  - (maybe 4 hours)
- [x] Download data (2010 to today) - Chaim
- [x] Plot stock raw data - Adam
- [x] Convert to percentages and plot (OOP) - Ethan, Yigit, 
- [x] Implement the metric - Ethan
- [x] Convolution operation - Ethan
- [x] Determine and report buy and hold value for the carnival - Yigit
- [ ] Fit a beta curve to determine the patterns (implement h(t)) 
- [ ] Report consolidation breakout profits - Yigit
- [x] Implement pipeline code - Yigit
 
## Development
- `conda create --name convoluted_stock_market_env python=3.6` (Do it once)
- `conda activate convoluted_stock_market_env`
- `pip install -r requirements.txt`


## Stocks
https://finviz.com/screener.ashx?v=121&f=cap_mega,sec_financial,sh_avgvol_o1000,sh_curvol_o1000&ft=4&o=-marketcap
Mega Cap Stocks from sectors whose average volume is greater than 1M.

### Index
- SPY

### Technology Dataset
- AAPL
- MSFT
- TSM
- NVDA
- XLK

### Health Care Dataset
- JNJ
- UNH
- NVS
- ABT
- XLV

### Finance Dataset
- BRK-B
- V
- JPM
- MA
- XLF

## Current Results
### Buy and Hold
```
[INFO] Pipeline for all stocks started. Start date: 2002-02-13 End date: 2021-02-12
[INFO] SPY buy and hold percent increase is 199.01568103357366%
[INFO] XLK buy and hold percent increase is 257.9072973953583%
[INFO] XLV buy and hold percent increase is 205.246846652216%
[INFO] XLF buy and hold percent increase is 169.4375809774955%
[INFO] AAPL buy and hold percent increase is 702.8559614372138%
[INFO] MSFT buy and hold percent increase is 329.2663695674954%
[INFO] TSM buy and hold percent increase is 433.2157151856909%
[INFO] NVDA buy and hold percent increase is 616.0704686694858%
[INFO] JNJ buy and hold percent increase is 189.87428557255117%
[INFO] UNH buy and hold percent increase is 398.6397051555083%
[INFO] NVS buy and hold percent increase is 196.80808895444898%
[INFO] ABT buy and hold percent increase is 266.7951924005368%
[INFO] BRK-B buy and hold percent increase is 202.89777759708417%
[INFO] V buy and hold percent increase is nan%
[INFO] JPM buy and hold percent increase is 345.2042508493086%
[INFO] MA buy and hold percent increase is nan%
[INFO] Pipeline for all stocks finished.
```