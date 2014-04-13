unit Nullpobug.Example.Spring4d.LocalMathService;

interface

implementation

uses
  Nullpobug.Example.Spring4d.ServiceLocator
  , Nullpobug.Example.Spring4d.MathServiceIntf
  ;

type
  TLocalMathServiceImpl = class(TInterfacedObject, IMathService)
    function Add(A, B: integer): Integer;
    function Multiply(A, B: integer): Integer;
    function Name: String;
  end;

{ TLocalMathServiceImpl }

function TLocalMathServiceImpl.Add(A, B: Integer): Integer;
begin
  Result := A + B;
end;

function TLocalMathServiceImpl.Multiply(A, B: Integer): Integer;
begin
  Result := A * B;
end;

function TLocalMathServiceImpl.Name: String;
begin
  Result := ToString;
end;

procedure RegisterLocalMathService;
begin
  ServiceLocator.RegisterComponent<TLocalMathServiceImpl>.Implements<IMathService>;
  ServiceLocator.Build;
end;

initialization
  RegisterLocalMathService;

end.
