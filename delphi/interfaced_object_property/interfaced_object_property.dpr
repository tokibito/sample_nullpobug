program interfaced_object_property;

{$APPTYPE CONSOLE}

type
  IFoo = interface
    procedure Say;
  end;

  TFoo = class(TInterfacedObject, IFoo)
  private
    FValue: String;
  public
    procedure Say;
    property Value: String read FValue write FValue;
  end;

procedure TFoo.Say;
begin
  Writeln(FValue);
end;

var
  // TFooだと明示的な開放が必要
  // IFooだと参照カウントで自動的に開放
  Foo: IFoo;
  // TFooとしてアクセスするための変数
  AFoo: TFoo;

begin
  // 終了時にメモリリークをレポートする
  ReportMemoryLeaksOnShutdown := True;
  Foo := TFoo.Create;
  // TFooにキャストする
  AFoo := Foo as TFoo;
  AFoo.Value := 'Hello, world!';
  AFoo.Say;
  // Freeを呼ばない
end.
