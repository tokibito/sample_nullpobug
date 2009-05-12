library callable;

type
  TWriter = procedure(A, B: Integer); stdcall;
  TCallable = procedure(Writer: TWriter); stdcall;

procedure Writer(A, B: Integer); stdcall;
begin
  WriteLn(A, B);
end;

procedure Call(Callback: TCallable); stdcall;
begin
  Callback(Writer);
end;

exports Call;

begin
end.
