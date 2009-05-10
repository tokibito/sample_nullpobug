program asmhello;

{$APPTYPE CONSOLE}

(*
  register(fastcall)呼び出し規約の場合、
  引数は EAX, EDX, ECX レジスタに格納される
  関数の戻り値は EAX レジスタに格納する。
*)
function Add(X, Y: Integer): Integer; register;
asm
  add EAX, EDX
end;

begin
  WriteLn(Add(3, 7));
end.
