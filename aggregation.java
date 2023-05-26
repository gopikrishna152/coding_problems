class operation{
    int sq(int n){
        return n*n;
    }
}

class circle{
    operation op;
    double pi=3.14;

    double area(int radius){
        op=new operation();
        int rsquare=op.sq(radius);//code reusability (i.e. delegates the method call).
        return pi*rsquare;


    }
}



public class aggregation {
    public static void main(String[] args) {
        circle c1=new circle();
        double result=c1.area(5);
        System.out.println(result);

    }
}
