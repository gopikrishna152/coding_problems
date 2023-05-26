import java.util.Scanner;
public class prime {
    public static void main(String[] args) {

            Scanner s =new Scanner(System.in);
            System.out.println("enter the value of a");
            int a=s.nextInt();
            int count=0;
            for(int i=2;i<a/2;i++){ //it can also can be written as (int i=2;i<a;i++) here the time complxity is more
                if (a%i==0) {

                    count = count + 1;
                }
            }
            if (count==0){
                System.out.println(" prime");
            }
            else{
                System.out.println("not a prime");
            }
    }
}
