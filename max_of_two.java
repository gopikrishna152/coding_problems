import java.util.Scanner;

public class max_of_two {
    public static void main(String[] args) {

            Scanner s =new Scanner(System.in);
            System.out.println("enter the value of a");
            int a=s.nextInt();
            System.out.println("enter the value of b");
            int b=s.nextInt();
            if (a>b){
                System.out.println("max number is"+a);
            }
            else{
                System.out.println("max number is "+b);
            }
    }
}
