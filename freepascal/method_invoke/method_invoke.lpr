program method_invoke;

{$IFDEF FPC}
{$MODE Delphi}
{$ELSE}
{$APPTYPE CONSOLE}
{$ENDIF}

uses
  MyClass in './my_class.pp',
  Invokes in './invokes.pp';

var
  obj: TMyClass;

begin
  obj := TMyClass.Create;
  // TMyClassのSayHelloを呼び出し、Selfにはobjを指定
  InvokeMethod(obj, 'SayHello', TMyClass);
end.
