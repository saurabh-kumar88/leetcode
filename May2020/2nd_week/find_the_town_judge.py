# 1. The town judge trusts nobody.
# 2. Everybody (except for the town judge) trusts the town judge.
# 3. There is exactly one person that satisfies properties 1 and 2.

from collections import Counter

class Solution:
    def findJudge(self, N: int, trust ) -> int:
        believers = []
        judge = []
        for x in trust:
            believers.append(x[0])
            judge.append(x[1])

        judge = list(dict.fromkeys(judge))
        
        # Boyer-moore voting algorithm
        temp = {}
        candidate = None
        vote = 0
        
        for x in judge:
            for z in trust:
                if x == z[1]:
                    vote += 1
                elif x == z[0]:
                    vote = 0
                    break
            count = 0
            temp[x] = vote
        
        for x in temp.keys():
            if temp[x] == N-1 or temp[x] == N:
                return x
        return -1
                

        

            
          
            

             
        

         
        
            


        
N = 3 
# trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
trust = [[1,3],[2,3]]
# trust = [[1,3],[2,3],[3,1]]
# trust = [[1,2], [2,3]]
# trust = [[1,2]]

if __name__ == "__main__":
    obj = Solution()
    print( obj.findJudge(N, trust) )
    











    # count = [0] * (N + 1)
    #     for i, j in trust:
    #         count[i] -= 1
    #         count[j] += 1
    #     for i in range(1, N + 1):
    #         if count[i] == N - 1:
    #             return i
    #     return -1