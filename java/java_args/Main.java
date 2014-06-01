class Main {
  public static void main(String[] args) {
    display(1, 2, 3);
  }

  static void display(Integer... params) {
    for (Integer value: params) {
      System.out.println(value);
    }
  }
}
