import java.util.Scanner;
public class odd_or_even {
    public static void main(String[] args) {

            Scanner s =new Scanner(System.in);
            System.out.println("enter the value of a");
            int a=s.nextInt();
            if(a%2==0 ){
                System.out.println("the number is even");
            }
            else{
                System.out.println("the number is odd");
            }

    }
}
