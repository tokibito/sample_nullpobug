unit Nullpobug.Example.Spring4d.MathService;

interface

type
  IMathService = interface
    ['{BFC7867C-6098-4744-9774-35E0A8FE1A1D}']
    function Add(a, b: integer): integer;
    function Multiply(a, b: integer): integer;
  end;

implementation

uses
  Nullpobug.Example.Spring4d.Container
  ;

type
  TNormalMathServiceImplemenation = class(TInterfacedObject, IMathService)
    function Add(a, b: integer): integer;
    function Multiply(a, b: integer): integer;
  end;
 
{ TNormalMathServiceImplemenation }
 
function TNormalMathServiceImplemenation .Add(a, b: integer): integer;
begin
  Result := a + b;
end;
 
function TNormalMathServiceImplemenation .Multiply(a, b: integer): integer;
begin
  Result := a * b;
end;
 
procedure RegisterNormalMathService;
begin
  ServiceLocator.RegisterComponent<TNormalMathServiceImplemenation>.Implements<IMathService>;
  ServiceLocator.Build;
end;
 
initialization
  RegisterNormalMathService;

end.
