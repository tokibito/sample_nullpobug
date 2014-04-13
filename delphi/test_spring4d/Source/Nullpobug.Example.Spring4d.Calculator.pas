unit Nullpobug.Example.Spring4d.Calculator;
 
interface
 
uses
  Nullpobug.Example.Spring4d.Container
  , Nullpobug.Example.Spring4d.MathService
  ;
 
type
  TCalculator = class
  private
    FMathService: IMathService;
  public
    constructor Create;
    function Addition(a, b: integer): integer;
    function Multiplication(a, b: integer): integer;
  end;
 
implementation
 
constructor TCalculator.Create;
begin
  FMathService := ServiceLocator.Resolve<IMathService>;
end;
 
function TCalculator.Addition(a, b: integer): integer;
begin
  Result := FMathService.Add(a, b);
end;
 
function TCalculator.Multiplication(a, b: integer): integer;
begin
  Result := FMathService.Multiply(a, b);
end;
 
end.
