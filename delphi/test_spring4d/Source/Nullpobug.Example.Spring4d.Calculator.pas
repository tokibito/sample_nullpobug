unit Nullpobug.Example.Spring4d.Calculator;
 
interface
 
uses
  Nullpobug.Example.Spring4d.ServiceLocator
  , Nullpobug.Example.Spring4d.MathServiceIntf
  ;
 
type
  TCalculator = class
  private
    FMathService: IMathService;
  public
    constructor Create;
    function Addition(A, B: Integer): Integer;
    function Multiplication(A, B: Integer): Integer;
    property MathService: IMathService read FMathService;
  end;
 
implementation
 
constructor TCalculator.Create;
begin
  FMathService := ServiceLocator.Resolve<IMathService>;
end;
 
function TCalculator.Addition(A, B: Integer): Integer;
begin
  Result := FMathService.Add(A, B);
end;
 
function TCalculator.Multiplication(A, B: Integer): Integer;
begin
  Result := FMathService.Multiply(A, B);
end;
 
end.
