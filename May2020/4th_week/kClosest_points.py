import math

class Solution:
  def kClosest(self, points, K ):
    self.mergeSort(points)
    ans = []
    i = 0
    while i < K:
      ans.append(points[i])
      i += 1

    return ans

  def distance_from_origin(self, point):
    return math.sqrt( math.pow(point[0],2) + math.pow(point[1], 2) ) 

  def mergeSort(self, arr): 
    if len(arr) >1: 
      mid = len(arr)//2 #Finding the mid of the array 
      L = arr[:mid] # Dividing the array elements 
      R = arr[mid:] # into 2 halves 

      self.mergeSort(L) # Sorting the first half 
      self.mergeSort(R) # Sorting the second half 
      i = j = k = 0
      
      # Copy data to temp arrays L[] and R[] 
      while i < len(L) and j < len(R): 
        if self.distance_from_origin(L[i]) < self.distance_from_origin(R[j]): 
          arr[k] = L[i] 
          i+=1
        else: 
          arr[k] = R[j] 
          j+=1
        k+=1
      
      # Checking if any element was left 
      while i < len(L): 
        arr[k] = L[i] 
        i += 1
        k += 1
      
      while j < len(R): 
        arr[k] = R[j] 
        j += 1
        k += 1


points = [[3,3],[5,-1],[-2,4]]
K = 2

# points = [[1,3],[-2,2]] 
# K = 1

# points = [[0,1],[1,0]]
# K = 2

# points = [[1,3],[-2,2],[2,-2]]
# K = 2

if __name__ == "__main__":
  
  # obj = Solution()
  # print( obj.kClosest(points, K) )

  arr = [31,26,3,4,5,65,4]
  points.sort(key= lambda x : math.sqrt( math.pow(x[0],2) + math.pow(x[1],2) ) ,reverse=False)
  print(points)
  
