public class progresam3{
     int a=100;
    int b=700;
    int c=800;
    void addition(){
        System.out.println("the addition is:");
        System.out.println(a+b+c);
    }
    void division(){
        System.out.println("the division:");
       System.out.println( a/ b/ c);
    }
    void subtraction(){
        System.out.println("the subtraction is :");
        System.out.println(a-b-c);
    }
    void multiplication(){

        System.out.println(" the multiplication is: ");
    System.out.println(a*b*c);
    }
    public static void main(String[] args) {

        progresam3 abc=new progresam3();
        abc.addition();
        abc.multiplication();
        abc.division();
        abc.subtraction();

    }
}
