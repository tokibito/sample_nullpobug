unit my_class;

{$M+}  // publishedを使うのでM+オプション指定
{$IFDEF FPC}
{$MODE Delphi}
{$ENDIF}

interface

type
  TMyClass = class(TObject)
  published  // RTTI生成のためにpublishedを使う
    procedure SayHello;
  end;

implementation

procedure TMyClass.SayHello;
begin
  WriteLn('Hello');
end;

end.
