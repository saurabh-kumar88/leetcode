class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        hour_angle = ( hour % 12 ) * 30 
        # change in hour angle caused by movements of minute hand
        hour_angle = hour_angle + ( minutes/60 * 30 )
        minutes_angle = minutes * 6
        
        ans = abs(hour_angle - minutes_angle)
        # If the angle is obtuse (>180), convert it to acute (0<=x<=180)
        if(ans > 180):
            ans = 360 - ans
        return ans

if __name__ == '__main__':
    obj = Solution()
    print( obj.angleClock(12, 30) )
        
        