class vehicle{
    String name;
    int milege;
    public vehicle(String n,int milege){
        name=n;
        this.milege=milege;
        System.out.println("the vehicle constructer has started the journey");

    }
    void display(){
        System.out.println("this works on the display method"+"\nthe vehicle is"+" "+name+" and its milage is"+" "+milege);
    }
}


public class constructor__practice {
    public static void main(String[] args) {
        vehicle v1=new vehicle("glamour",500);
        v1.display();

    }
}
