
from math import pow, sqrt

def distance(x, h):
	'''
	input: 
	--- x: input data candlestick object
	--- h: pattern data candlestick object
	output: 
	--- metric: the metric distance between these two objects
	'''
	metric = sqrt(pow(x.getOpen() + h.getOpen(), 2) + pow(x.getClose() + h.getClose(), 2) + pow(x.getLow() + h.getLow(), 2) + pow(x.getHigh() + h.getHigh(), 2))
	return metric

def convolve(stockHistory, stockPattern):
	'''
	input:
	--- stockHistory: effectively x(t) for the preprocessed stock data stored as a list of candlestick objects
	--- stockPattern: effectively h(t) for the preprocessed stock pattern stored as a list of candlestick objects
	output:
	--- metricList: a list containing the metric for each window of the stock pattern against the the stock history
	'''
	metricList = []
	for i in range(len(stockHistory) - len(stockPattern)):
		stockWindow = stockHistory[i:(i + len(stockPattern))]
		metric_i = 0
		for j, stock_j in enumerate(stockWindow):
			pattern_j = stockPattern[j]
			metric_i += distance(stock_j, pattern_j)
		metricList.append(metric_i)
	return metricList

