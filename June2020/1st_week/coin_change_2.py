class Solution:
  def change(self, amount, coins ) -> int:
    
    # single coins which can make sum
    single_coins = []
    for x in sorted(coins):
      if x <= amount:
        single_coins.append(x)
    # print(single_coins)
    single_combo = self.singleCombinations(coins, amount)

    # combinations <= Sum
    global_max, local_max = amount, coins[0]
    coins_combo = [[]]
    # kadane's Algorithm
    temp = []
    for i in coins:
      local_max += i
      if local_max <= global_max:
        temp.append(i)
    
    coins_combo.append(temp)

    print(coins_combo)
    # return single_combo
  
  # helper method --- single coin combination

  def singleCombinations(self,coins_arr,Sum):
    count = 0
    for i in coins_arr:
      flag = True
      temp, x = 1, None
      while flag:
        x = i * temp
        if x == Sum:
          count += 1
          break
        elif x > Sum:
          break
        temp += 1
    return count

  def printSubArrays(self, arr, start, end): 
    if end == len(arr): 
      return temp

    elif start > end: 
      return printSubArrays(arr, 0, end + 1) 
    
    else: 
      # print(arr[start:end + 1])
      temp.append(arr[start:end + 1]) 
    return printSubArrays(arr, start + 1, end) 
		

# amount = 5 
# coins = [1, 2, 5]

amount = 5
coins = [1,2,3,5]



if __name__ == "__main__":
    obj = Solution()
    # print( obj.change(amount, coins) )
    print( obj.printSubArrays(coins, 0, 0) )
        