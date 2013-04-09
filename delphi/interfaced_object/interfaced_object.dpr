program interfaced_object;

{$APPTYPE CONSOLE}

type
  IFoo = interface
    procedure Say;
  end;

  TFoo = class(TInterfacedObject, IFoo)
  public
    procedure Say;
  end;

procedure TFoo.Say;
begin
  Writeln('Hello, world!');
end;

var
  // TFooだと明示的な開放が必要
  // IFooだと参照カウントで自動的に開放
  Foo: IFoo;

begin
  // 終了時にメモリリークをレポートする
  ReportMemoryLeaksOnShutdown := True;
  Foo := TFoo.Create;
  Foo.Say;
  // Freeを呼ばない
end.
