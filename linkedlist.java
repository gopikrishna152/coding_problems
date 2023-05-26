public class linkedlist {

    Node head;

    public void insert(int data) {

        Node node = new Node();
        node.data = data;
        node.next = null;
        if (head == null) {
            head = node;
        } else {
            Node n = head;
            while (n.next != null) {
                n = n.next;
            }
            n.next = node;
        }
    }

    public void show() {
        Node n = head;
        while (n.next != null) {
            System.out.println(n.data);
            n = n.next;
        }
        System.out.println(n.data);

    }

    public void delete(int data) {
        Node n = head;
        if (n.data == data) {
            head = n.next;
        } else {

            while (n.data != data) {
                Node previous = n;
                n = n.next;
                previous.next = n.next;
            }

        }

    }

}