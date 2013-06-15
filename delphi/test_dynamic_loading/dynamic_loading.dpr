program dynamic_loadng;

{$APPTYPE CONSOLE}

uses
  System.SysUtils
{$IFDEF MSWINDOWS}
  , WinApi.Windows
{$ENDIF}
  ;

const
{$IFDEF MacOS}
LIB_NAME = 'mylib.dylib';
{$ELSE}
LIB_NAME = 'mylib.dll';
{$ENDIF}

type
  TAdd = function(X, Y: Integer): Integer; cdecl;
  TSay = procedure(Text: PAnsiChar); cdecl;

var
  Handle: THandle;
  Add: TAdd;
  Say: TSay;

begin
  Handle := SafeLoadLibrary(LIB_NAME);
  try
    if Handle <> 0 then
    begin
      @Add := GetProcAddress(Handle, 'Add');
      if @Add <> nil then
        Writeln(Add(10, 20));
      @Say := GetProcAddress(Handle, 'Say');
      if @Say <> nil then
        Say('こんにちは');
    end;
  finally
    FreeLibrary(Handle);
  end;
end.
