class animal{
    void eat(){
        System.out.println("eating.....");
    }
}
class dog extends animal{
    void bark(){
        System.out.println("barking.......");
    }
}



public class single_level_inheritance {
    public static void main(String[] args) {
        dog d1=new dog();
        d1.bark();
        d1.eat();

    }
}
