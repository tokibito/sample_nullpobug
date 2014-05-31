import java.util.List;
import java.util.LinkedList;

class Main {
  public static void main(String[] args) {
    List<Integer> lst = new LinkedList<Integer>();
    for (int i = 0; i < 5; i++) {
      lst.add(i);
    }
    System.out.println(lst);
  }
}
