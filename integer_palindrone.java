import java.util.Scanner;
public class integer_palindrone {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the number ");
        int num=sc.nextInt();
        int req=0;
        while(num>0){
            int remainder=num%10;
            num=num/10;

            req=(req*10)+remainder;
            System.out.println(req);
        }
        if(req==num)
        {
            System.out.println("its a palindrome dood!");
        }
        else{
            System.out.println("mg");
        }



    }
}
