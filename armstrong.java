import java.util.Scanner;
import java.lang.Math;

public class armstrong {

    public static void main(String[] args) {
        // int number, originalNumber, remainder, result = 0, n = 0;
        // Scanner scanner = new Scanner(System.in);
        // System.out.println("Enter a number:");
        // number = scanner.nextInt();
        // originalNumber = number;
        // while (originalNumber != 0) {
        // originalNumber /= 10;
        // ++n;
        // }
        // originalNumber = number;
        // while (originalNumber != 0) {
        // remainder = originalNumber % 10;
        // result += Math.pow(remainder, n);
        // originalNumber /= 10;
        // }
        // if (result == number)
        // System.out.println(number + " is an Armstrong number.");
        // else
        // System.out.println(number + " is not an Armstrong number.");

        for (int i = 1; i <= 100; i++) {
            int n = i;
            int j;
            int rev = 0;
            while (n != 0) {
                j = n % 10;
                rev = rev * 10 + j;
                n /= 10;
            }
            if (i == rev) {
                System.out.print(i + " ");
            }
        }
    }
}
