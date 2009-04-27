program nullpo;

{$APPTYPE CONSOLE}

uses
  SysUtils,
  Classes;

var
  Foo: TObject;

begin
  try
    Foo := nil;
    WriteLn(Format('nil: %s', [IntToHex(Integer(Foo), 8)]));
    WriteLn(Foo.ClassName);
  except
    on E: Exception do
        WriteLn(E.message);
  end;
end.
