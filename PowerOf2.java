package misslanous;
import java.util.Math;

public class PowerOf2{
  public static void main(String[] args) {
    int n = 536870912;
    // int n = 15;
    // System.out.println( (int)(Math.log(n)/Math.log(2)) );
    if (Math.pow(2, (int)(Math.log(n)/Math.log(2))) == n) {
      System.out.println(true);
    }
    else{
      System.out.println(false);
    }
  }
}