program MyCallback;

{$APPTYPE CONSOLE}

uses
  SysUtils,
  MethodCallBack;

type
  TSayCallback = procedure of object; stdcall;
  TMyClass = class
  private
    FName: string;
    FCallbackProc: Pointer;
    procedure Say; stdcall;
  public
    constructor Create(Name: string);
    property CallbackProc: Pointer read FCallbackProc;
    property Name: string read FName write FName;
  end;

function SetCallback(f: TSayCallback): Pointer;
begin
  Result := GetOfObjectCallBack(TCallBack(f), 0, ctSTDCALL);
end;

constructor TMyClass.Create(Name: string);
begin
  FName := Name;
  FCallbackProc := SetCallback(Say);
end;

procedure TMyClass.Say;
begin
  WriteLn(FName);
end;

procedure DLLProc(Callback: Pointer); stdcall; external 'MyLibrary';

var
  obj1, obj2: TMyClass;
begin
  obj1 := TMyClass.Create('foo');
  obj2 := TMyClass.Create('bar');
  try
    DLLProc(obj1.CallbackProc);
    DLLProc(obj2.CallbackProc);
    obj1.Name := 'hoge';
    DLLProc(obj1.CallbackProc);
  finally
    obj1.Free;
    obj2.Free;
  end;
end.
