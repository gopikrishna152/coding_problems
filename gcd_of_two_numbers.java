public class gcd_of_two_numbers {
    public static void main(String[] args) {
        int a=24;
        int b=6;
        while(a!=0 && b!=0){
            if (a>b){
                a=a%b;
            }
            else{
                b=b%a;
            }
        }
        System.out.println("the gcd of the two numbers is  "+ a);


    }
}
