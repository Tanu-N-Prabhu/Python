import java.util.*;

public class Solution {
    static int solveMeFirst(int a, int b) {
        return a + b;
    }
 
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a, b;
        System.out.print("Enter number 1:");
        a = in.nextInt();
        System.out.print("Enter number 2:");
        b = in.nextInt();
        System.out.println("Sum of entered numbers: " + solveMeFirst(a, b));
    }
}
