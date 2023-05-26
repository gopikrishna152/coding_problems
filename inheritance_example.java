class Employee{
    int salary=40000;

}
class Programmer extends Employee{
    int bonus=100000;

}

public class inheritance_example {
    public static void main(String[] args) {
        Programmer p1=new Programmer();
        System.out.println(p1.salary);
        System.out.println(p1.bonus);

    }

}
