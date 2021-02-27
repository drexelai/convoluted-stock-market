import yfinance as yf
import matplotlib.pyplot as plt
import os
from datetime import date, datetime
import pandas as pd
from CandleStick import CandleStick
from ConsolidationBreakout import ConsolidationBreakout
 

def to_datetime(date_str):
    temp = datetime.strptime(date_str, '%Y-%M-%d')
    return date(temp.year, temp.month, temp.day)

def fetch_data(ticker, start_date, end_date):
    """
    Downloads and writes the stock price data to csv.
    If the csv data already exists, read from it.
    """
    file_path = os.path.join("data", ticker+".csv")
    if os.path.exists(file_path):
        return pd.read_csv(file_path, index_col=0)
    start_date_object = to_datetime(start_date)
    end_date_object = to_datetime(end_date)
    stock_price = yf.download(
        ticker, start_date=start_date_object, end_date=end_date_object)
    stock_price.to_csv(file_path)
    return pd.read_csv(file_path, index_col=0)


def buy_and_hold(stock_price):
    """Calculate profit from buy and hold"""
    return sum([s.close for s in stock_price])


def run_pipeline_for_single_stock(ticker, percentages_for_single_stock, start_date="2002-02-13", end_date = "2021-02-12"):
    """For a given stock ticker, 
    i)  calculate and report profit from buy and hold (see buy_and_hold), 
    ii) calculate and report profit from (see trade_convolution)
    No more than 1 share is bought/sold at a time.
    No shorting allowed. i.e we can only sell if we have a share.
    """
    buy_and_hold_profit = buy_and_hold(percentages_for_single_stock)
    print("[INFO] {} buy and hold percent increase is {}%".format(ticker, buy_and_hold_profit))
    # TODO: Implement ConsolidationBreakout trading
    # max_profit = ConsolidationBreakout.trade_consolidation_breakout_detection()
    # return buy_and_hold_profit


def run_pipeline_for_all_stocks(start_date="2002-02-13", end_date = "2021-02-12"):
    print("[INFO] Pipeline for all stocks started. Start date: {} End date: {}".format(start_date, end_date))

    percentages = create_dataset_in_percentages(start_date, end_date)
    for ticker in percentages.keys():
        # if ticker == "SPY": # TODO remove this after testing.
        run_pipeline_for_single_stock(ticker, percentages[ticker], start_date, end_date)

    print("[INFO] Pipeline for all stocks finished.")


def encode_stock_price(stock_price, start_date, end_date):
    """Returns a list of CandleSticks Objects"""

    stock_price['Adj Close'] = stock_price['Adj Close'].pct_change() * 100
    stock_price['Open'] = stock_price['Open'].pct_change() * 100
    stock_price['High'] = stock_price['High'].pct_change() * 100
    stock_price['Low'] = stock_price['Low'].pct_change() * 100

    # Filter data between two dates 
    filtered_stock_price = stock_price.loc[(stock_price.index >= start_date) 
                     & (stock_price.index < end_date)] 

    candle_sticks = []

    for i in range(len(filtered_stock_price)):
        c = CandleStick([filtered_stock_price['Open'].iloc[i], filtered_stock_price['Adj Close'].iloc[i], \
                            filtered_stock_price['High'].iloc[i],filtered_stock_price['Low'].iloc[i]])
        candle_sticks.append(c)

    return candle_sticks


def fetch_sector_db():
    return {'index': ["SPY","XLK","XLV","XLF"],
    'technology': ["AAPL","MSFT","TSM", "NVDA"],
    'healtcare': ["JNJ","UNH", "NVS", "ABT"],
    'finance':["BRK-B","V", "JPM","MA"]}


def create_dataset_in_percentages(start_date, end_date):

    db = fetch_sector_db()
    percentages = {}

    for sector, stocks in db.items():
        for stock in db[sector]:
            stock_price = fetch_data(stock, start_date, end_date)
            encoded_stock_price = encode_stock_price(stock_price, start_date, end_date)
            percentages[stock] = encoded_stock_price

    return percentages


if __name__ == "__main__":

    run_pipeline_for_all_stocks(start_date="2002-02-13", end_date = "2021-02-12")