class ConsolidationBreakout:
    """
    Attributes:
        breakout_duration: breakout duration is the duration of the consolidation in days
        tolerance : How much noise to accept in percentage
    """
    def __init__(self, breakout_duration = 5, tolerance = 3, support=float("-inf"), resistance=float("inf")):
        self.breakout_duration = breakout_duration
        self.tolerance = tolerance
        self.support = support 
        self.resistance = resistance


    def trade_consolidation_breakout_detection(self, prices, predictions):   
        """Slide the consolidation breakout detection signal over prices"""
        max_profit = 0
        profitable_trade_count = unprofitable_trade_count = 0
        assert len(prices) > len(self.breakout_duration)
        bullish = []
        bearish = []
        for i in range(len(prices)- self.breakout_duration):
            if prices['Close'].iloc[i+self.breakout_duration] > prices['Close'].iloc[i] and self.detect_consolidation_breakout(predictions[i:i+self.breakout_duration]) == "bullish":
                # Bullish prediction was correct
                max_profit += prices['Close'].iloc[i+self.breakout_duration] - prices['Close'].iloc[i]
                profitable_trade_count +=1
                bullish.append((i,i+self.breakout_duration)) 
                
            elif prices['Close'].iloc[i+self.breakout_duration] < prices['Close'].iloc[i] and self.detect_consolidation_breakout(predictions[i:i+self.breakout_duration]) == "bullish":
                # Bullish prediction was NOT correct
                max_profit += prices['Close'].iloc[i+self.breakout_duration] - prices['Close'].iloc[i]
                unprofitable_trade_count +=1

            elif prices['Close'].iloc[i+self.breakout_duration] < prices['Close'].iloc[i] and self.detect_consolidation_breakout(predictions[i:i+self.breakout_duration]) == "bearish":
                # Bearish prediction was correct
                max_profit += prices['Close'].iloc[i+self.breakout_duration] - prices['Close'].iloc[i]
                profitable_trade_count +=1
                bearish.append((i,i+self.breakout_duration)) 

            elif prices['Close'].iloc[i+self.breakout_duration] > prices['Close'].iloc[i] and self.detect_consolidation_breakout(predictions[i:i+self.breakout_duration]) == "bearish":
                # Bearish prediction was NOT correct
                max_profit += prices['Close'].iloc[i+self.breakout_duration] - prices['Close'].iloc[i]
                unprofitable_trade_count +=1

            else:
                pass # no detection

        return max_profit, profitable_trade_count, unprofitable_trade_count

    def detect_consolidation_breakout(self, prices):   
        """For the bullish breakout pattern:
            - The close price must be higher than the highest close value of the last 20 bars, 5 bars ago.

            For the bearish breakout pattern:
            - The close price must be lower than the lowest close value of the last 20 bars, 5 bars ago.

            Source: https://www.quantshare.com/item-902-consolidation-breakout-and-congestion-index
        """
        assert len(price) + self.breakout_duration == len(self.width)
        if max(prices) + self.tolerance < self.resistance and min(prices) - self.tolerance > self.support:
            return 'bullish' # up
        elif max(prices) + self.tolerance < self.resistance and  min(prices) - self.tolerance > self.support:
            # TODO: Implement the bullish and bearish distinction
            return 'bearish' # down
        else:
            return 'neutral' # sideways




