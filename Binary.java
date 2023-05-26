import java.util.Scanner;
import java.util.*;

public class Binary {
    // static Node view(){
    // System.out.println("the values in tree");

    // }

    static Node create() {
        Scanner sc = new Scanner(System.in);
        int data;
        Node root = null;
        System.out.println("enter value");
        data = sc.nextInt();
        if (data == -1) {
            return null;
        }

        root = new Node(data);
        System.out.println("enter the left child of " + root.data);
        root.leftNode = create();

        System.out.println("enter the right child of " + root.data);
        root.rightNode = create();
        return root;

    }

    public static void main(String[] args) {
        // Scanner sc=new Scanner(System.in);
        Node root = create();

    }

}

class Node {
    public int data;
    Node leftNode;
    Node rightNode;

    public Node(int data) {
        this.data = data;
        rightNode = null;
        leftNode = null;
    }
}
