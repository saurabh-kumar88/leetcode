from collections import deque

# class StockSpanner:
#     _INDEX = 0
#     _STOCK_PRICE = deque()
    
#     def __init__(self):
#       pass
#       # self._STOCK_PRICE = deque()
         
#     def isEmpty(self):
#       return (True if StockSpanner._STOCK_PRICE.__len__()==0 else False)

#     def next(self, price: int) -> int:
        
#         StockSpanner._STOCK_PRICE.appendleft(price)
        
#         STOCK_SPAN = 1    
#         while True:
#           if self.isEmpty():
#             break
#           prev_day_price = StockSpanner._STOCK_PRICE.pop() 

#           if prev_day_price == price:
#             break
#           elif prev_day_price < price :
#             STOCK_SPAN += 1

#         return STOCK_SPAN

# -------------- list based -------------

class StockSpanner:
    _INDEX = 0
    def __init__(self):
      self._STOCK_PRICE = []
      
    def next(self, price: int)-> int:
      _SPAN = 1

      if price is None:
        return None
      
      self._STOCK_PRICE.append(price)
      
      if len(self._STOCK_PRICE):
        _INDEX = self._STOCK_PRICE.index( self._STOCK_PRICE[-1] )
      
      if self._STOCK_PRICE[_INDEX] < price:
        _SPAN += 
     


      n = len(self._STOCK_PRICE)
      i = 1
      while i < n:
        # while( len(self._STOCK_PRICE) and ( self._STOCK_PRICE[-1] <= self._STOCK_PRICE[i] )):
        #   self._STOCK_PRICE.pop()
        if self._STOCK_PRICE[n - i] <= price:
          _SPAN = self._STOCK_PRICE.index(self._STOCK_PRICE[-1]) - (n - i)
          return _SPAN
        i += 1
        
        
        # _SPAN = i + 1 if len( self._STOCK_PRICE ) <= 0 else (1 + (i - self._STOCK_PRICE.index(self._STOCK_PRICE[-1]) ) )
        

      return _SPAN

      

priceList = [100, 80, 60, 70, 60, 75, 85]

if __name__ == "__main__":
  
  obj = StockSpanner()

  print( obj.next(None), end=" " )
  print( obj.next(100), end=" " )
  print( obj.next(80), end=" " )
  print( obj.next(60), end=" " )
  print( obj.next(70), end=" " )
  print( obj.next(60), end=" " )
  print( obj.next(75), end=" " )
  print( obj.next(85), end=" " )
  
  # print( obj.next(None), end=" " )
  # print( obj.next(28), end=" " )
  # print( obj.next(14), end=" " )
  # print( obj.next(28), end=" " )
  # print( obj.next(35), end=" " )
  # print( obj.next(46), end=" " )
  # print( obj.next(53), end=" " )
  # print( obj.next(66), end=" " )
  # print( obj.next(80), end=" " )
  # print( obj.next(87), end=" " )
  # print( obj.next(88), end=" " )

     

  

  # ---- test code ---
  # q = deque()
  # for x in priceList:
  #   q.appendleft(x)
    
  # print( q.maxlen )
  

  