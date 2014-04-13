program Calculator;

{$APPTYPE CONSOLE}

uses
  Nullpobug.Example.Spring4d.Calculator
  ;

var
  FCalculator: TCalculator;

begin
  FCalculator := TCalculator.Create;
  try
    Writeln(FCalculator.Addition(10, 20));
    Writeln(FCalculator.Multiplication(10, 20));
  finally
    FCalculator.Free;
  end;
end.
