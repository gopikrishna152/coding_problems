
// import java.sql.SQLOutput;
import java.util.Scanner;

//program for printing the fibinocci series
public class fibinocci_series {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int nos;
        System.out.println("enter the no of series");
        nos = sc.nextInt();
        int a = 0, b = 1, c;
        System.out.println(a);
        System.out.println(b);
        for (int i = 0; i < nos; i++) {
            c = a + b;
            a = b;
            b = c;
            System.out.println(c);

        }
    }
}
