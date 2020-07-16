class Solution:
    def twoSum(self, nums, target: int) :
        
        # binary search algorithm

        lo = 0
        hi = len(nums) - 1
        result = [ None for x in range(2) ]
        while(lo <= hi):
            mid = lo + (hi - lo)//2
            

            if mid > hi or mid < lo:
                return None

            Sum = nums[lo] + nums[hi]
            
            print("lo", nums[lo])
            print("mid", nums[mid])
            print("hi", nums[hi])
            print("Sum ", Sum) 
            print("\n")
            if Sum == target:
                result[0] = lo
                result[1] = hi
                return result
            if Sum > target:
                hi = mid - 1
            if Sum < target:
                lo = mid + 1
                
        return None
        



arr = [ 2, 7, 10, 11, 15, 45, 50, 65, 91 ]
target = 26



if __name__ == "__main__":
    obj = Solution()
    print( obj.twoSum( arr, target ) )


   
   

    
