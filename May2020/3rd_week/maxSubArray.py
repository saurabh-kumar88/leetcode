"kadane's algorithm"
def kadane_max(arr):
  local_max = 0
  global_max = -2**31

  n = len(arr)
 
  for index in range(n):
    local_max =  max(arr[index], arr[index] + local_max )
    if local_max > global_max:
      global_max = local_max

  return global_max
	
	
def maxCircularSum(A):

  local_min_sum, global_min_sum = 0, float('inf')
  local_max_sum, global_max_sum = 0, float('-inf')
  
  arrSum = 0
  for number in A:
    local_min_sum = min( (local_min_sum + number), number  )
    global_min_sum = min( local_min_sum, global_min_sum )

    local_max_sum = max( number, (local_max_sum + number), number )
    global_max_sum = max(local_max_sum, global_max_sum )

    arrSum += number
  
  # global_max_sum = maximum subarray sum without crossing boundary
  # arrSum - global_min_sum  = maximum subarray sum with crossing boundary

  if global_max_sum > 0:
    return max( global_max_sum, (arrSum - global_min_sum) )
  else:
    return global_max_sum

arr = [11, 10, -20, 5, -3, -5, 8, -13, 10, 100, -90]
arr2 = [-2,-3,-1]


if __name__ == "__main__":                                                        
  print( maxCircularSum(arr) )
   

  	