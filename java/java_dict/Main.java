import java.util.Map;
import java.util.HashMap;

class Main {
  public static void main(String[] args) {
    Map<String, String> dct = new HashMap<String, String>();
    dct.put("foo", "bar");
    dct.put("hoge", "fuga");
    System.out.println(dct);
  }
}
