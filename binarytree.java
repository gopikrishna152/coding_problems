import java.util.*;

public class binarytree {

    class leftview {

        void leftview(Node root, List<Integer> result) {

        }
    }

    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);

        List<Integer> result = new ArrayList<>();
        leftview instance = new leftview();
        instance.leftview(root, result);

    }

}

class Node {
    int data;
    Node left, right;

    public Node(int data) {
        this.data = data;
        this.right = this.left = null;
    }
}