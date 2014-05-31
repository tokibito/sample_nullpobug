import java.util.Dictionary;
import java.util.Hashtable;

class Main {
  public static void main(String[] args) {
    Dictionary<String, String> dct = new Hashtable<String, String>();
    dct.put("foo", "bar");
    dct.put("hoge", "fuga");
    System.out.println(dct);
  }
}
