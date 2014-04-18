unit Nullpobug.Example.Spring4d.Calculator;
 
interface
 
uses
  System.SysUtils
  , Nullpobug.Example.Spring4d.ServiceLocator
  , Nullpobug.Example.Spring4d.MathServiceIntf
  , Nullpobug.Example.Spring4d.CalculatorUIIntf
  ;
 
type
  TCalculator = class
  private
    FMathService: IMathService;
    FCalculatorUI: ICalcuratorUI;
  public
    constructor Create;
    function Addition(A, B: Integer): Integer;
    function Multiplication(A, B: Integer): Integer;
    procedure WriteLine(S: String);
    property MathService: IMathService read FMathService;
    property CalculatorUI: ICalcuratorUI read FCalculatorUI;
    class procedure Main;
  end;
 
implementation
 
constructor TCalculator.Create;
begin
  FMathService := ServiceLocator.Resolve<IMathService>;
  FCalculatorUI := ServiceLocator.Resolve<ICalcuratorUI>;
end;
 
function TCalculator.Addition(A, B: Integer): Integer;
begin
  Result := FMathService.Add(A, B);
end;
 
function TCalculator.Multiplication(A, B: Integer): Integer;
begin
  Result := FMathService.Multiply(A, B);
end;

procedure TCalculator.WriteLine(S: String);
begin
  FCalculatorUI.WriteLine(S);
end;

class procedure TCalculator.Main;
var
  FCalculator: TCalculator;
begin
  FCalculator := TCalculator.Create;
  try
    FCalculator.WriteLine('MathService: ' + FCalculator.MathService.Name);
    FCalculator.WriteLine('CalculatorUI: ' + FCalculator.CalculatorUI.Name);
    FCalculator.WriteLine(Format('10 + 20 = %d', [FCalculator.Addition(10, 20)]));
    FCalculator.WriteLine(Format('10 * 20 = %d', [FCalculator.Multiplication(10, 20)]));
  finally
    FCalculator.Free;
  end;
end;

end.
