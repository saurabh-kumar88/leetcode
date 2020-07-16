from collections import Counter
arr = [3,2,3]
arr2 = [3,2,11,11,11,45,45,45,6544,56,75,64,65,38,745,45,45,45,45,431,1,1,1,1,1,1,11,1,1,1,1,11,1,1,1,1,11,1,1,1,1,1,1]

class Solution(object):
    
    def majorityElement(self, nums) -> int:
        count = Counter(nums)
        key_list = list( count.keys() )
        val_list = list( count.values() )

        majority = max(val_list)

        return int( key_list[val_list.index(majority)] )




if __name__ == "__main__":
    
    obj = Solution()
    # print( obj.majorityElement(arr2) )

    arr2.sort()
    print( arr2[  len(arr2)//2  ] )
    
            



