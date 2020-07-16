class Solution {
    /*
     hour hand covers  ---> 30 degrees/hr
     or 30 * (minutes/60) degress/min
     minutes hande covers ---> 6 degrees/min
    
    */
    
    public double angleClock(int hour, int minutes) {
        double hour_angle = (double)hour;
        hour_angle = (hour_angle%12) * 30;  
       
        // chnage in hour hand due to minute hand
        hour_angle = hour_angle + ( ((double)minutes/60) * 30 );
        double minute_angle = 6 * (double)minutes;
        
        double ans = Math.abs(hour_angle - minute_angle);
        // If the angle is obtuse (>180), convert it to acute (0<=x<=180)
            if(ans > 180) ans = 360.0 - ans;
            
        return ans;
    }
}


public class Day14_Angle_Between_Hands_of_a_Clock
{

    public static void main(String[] args) {
        Solution obj = Solution();
        System.out.println( obj.angleClock(12, 30) );
    }


}