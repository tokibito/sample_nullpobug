unit my_class;

{$M+}
{$IFDEF FPC}
{$MODE Delphi}
{$ENDIF}

interface

type
  TMyClass = class(TObject)
  published
    procedure SayHello;
  end;

implementation

procedure TMyClass.SayHello;
begin
  WriteLn('Hello');
end;

end.
