program test_integer_helper;

{$APPTYPE CONSOLE}

(* Sysytem.SysUtilsをusesに追加することでヘルパークラスが有効になる *)
uses
  System.SysUtils;

var
  IntValue, IntValue2: Integer;
  StrValue: String;

begin
  IntValue := 12345;
  (* IntegerからStringへ変換 *)
  StrValue := IntValue.ToString;
  Writeln(StrValue);
  (* StringからIntegerへ変換 *)
  IntValue2 := Integer.Parse('54321');
  Writeln(IntValue2);
end.
