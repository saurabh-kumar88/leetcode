class Solution:
  def reconstructQueue(self, people):

    
    people =  people.sort(key = lambda x : (-x[0], x[1]) )

    ans = []
    for person in people:
      ans.insert(person[1], person)
    return ans
    

Arr = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

if __name__ == "__main__":
    obj = Solution()
    print(obj.reconstructQueue(Arr))
        