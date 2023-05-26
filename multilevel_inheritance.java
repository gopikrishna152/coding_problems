class aaa{
    void sleep(){
        System.out.println("sleeping.....");
    }
}
class blaa extends aaa{
    void bark(){
        System.out.println("barking...");

    }
}
class babydog extends blaa{
    void weeping(){
        System.out.println("weping...");
    }
}



public class multilevel_inheritance {
    public static void main(String[] args) {
       babydog d2=new babydog();
       d2.sleep();
       d2.bark();
       d2.weeping();
    }
}
