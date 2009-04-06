program main;

{$APPTYPE CONSOLE}

type
  TWriter = procedure(A, B: Integer); stdcall;
  TCallable = procedure(Writer: TWriter); stdcall;

procedure Call(Callback: TCallable); stdcall; external 'callable';

procedure Callable(Writer: TWriter); stdcall;
begin
  Writer(100, 200);
end;

begin
  Call(Callable);
end.