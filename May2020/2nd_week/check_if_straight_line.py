import numpy as np

class Solution:
    def checkStraightLine(self, coordinates ) -> bool:
        
        if len(coordinates) == 2:
            return True
        
        common_slope = self.cal_slope(coordinates[0], coordinates[1])    
        
        for point in range(len(coordinates)):    
            even = point
            odd = point + 1 
            if odd > len(coordinates) - 1:
                break
            if( self.cal_slope(coordinates[even] ,coordinates[odd] ) != common_slope ):
                return False
        return True
    
    def cal_slope(self, a, b):
        
        try:
            slope = ( b[1] - a[1] )/( b[0] - a[0] )
        except ZeroDivisionError as err:
            return 0
        
        return slope 

            
        
arr = [[-1,1],[-6,-4],[-6,2],[2,0],[-1,-2],[0,-4]]
# arr =  [ [1,2],[2,3],[3,4],[4,5],[5,6],[6,7] ] 
# arr = [ [1,1],[2,2],[3,4],[4,5],[5,6],[7,7] ]
if __name__ == "__main__":
    obj = Solution()
    print( obj.checkStraightLine(arr) )
    # obj.cal_slope( arr[0], arr[1] )
    # a = np.array( arr[0] )
    # b = np.array( arr[1] )
    # print( np.cross(a,b) )

    

    