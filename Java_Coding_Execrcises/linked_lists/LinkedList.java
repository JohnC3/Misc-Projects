import java.io.*;
import java.util.*;


public class LinkedList{

  public static void main(String args[]){
    System.out.println("I am the main method!");

    Node ll = make_trival_ll();
  }

  public static Node make_trival_ll(){

    SinglyLinkedList root = new SinglyLinkedList(0);

    for (int i = 1; i < 10; i++){
      root.appendToTail(i);
    }

    root.printContents();

    return root;

  }
}


class Node{

  Node next = null;
  int data;

  public Node(int d){
    data = d;
  }

  void appendToTail(int d){
    Node end = new Node(d);
    Node n = this;
    while (n.next != null){
      n = n.next;
    }
    n.next = end;
  }

}


class SinglyLinkedList extends Node{

  Node next = null;
  int data;

  public SinglyLinkedList(int d){
    data = d;

  }

  void printContents(){
    Node n = this;
    System.out.printf("%d\n", n.data);
    while (n.next != null){
      n = n.next;
      System.out.printf("%d\n", n.data);
    }
  }
}
