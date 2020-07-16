class Solution:
  def twoCitySchedCost(self, costs: List[List[int]]) -> int:
  
    # Sort the costs by the non-decreasing values of the savings
    costs.sort(key=lambda x : x[0] - x[1])
    
    minimum_cost = 0
    for i in range(len(costs)):
      if i < len(costs)//2:
        minimum_cost += costs[i][0] # sending first half to city A
      else:
        minimum_cost += costs[i][1] # sending rest of the half to city B

    return minimum_cost
          