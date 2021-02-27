import numpy as np

class CandleStick:
    open = 0
    close = 0
    high = 0
    low = 0

    def __init__(self, price_vec):
        self.open = price_vec[0]
        self.close = price_vec[1]
        self.high = price_vec[2]
        self.low = price_vec[3]

    # GETTERS FOR PRICE ATTRIBUTES
    def getOpen(self):
        return self.open

    def getClose(self):
        return self.close

    def getHigh(self):
        return self.high

    def getLow(self):
        return self.low

    def getRange(self):
        return self.high - self.low

    def __repr__(self):
        return "Open: {} Close: {} High:{} Low:{}".format(self.open, self.close, self.high, self.low)


