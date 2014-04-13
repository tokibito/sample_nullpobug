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
    class procedure Main;
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

class procedure TCalculator.Main;
var
  FCalculator: TCalculator;
begin
  FCalculator := TCalculator.Create;
  try
    Writeln(FCalculator.MathService.Name);
    Writeln('10 + 20 = ', FCalculator.Addition(10, 20));
    Writeln('10 * 20 = ', FCalculator.Multiplication(10, 20));
  finally
    FCalculator.Free;
  end;
end;

end.
