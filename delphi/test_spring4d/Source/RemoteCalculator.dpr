program LocalCalculator;

{$APPTYPE CONSOLE}

uses
  System.SysUtils
  , Nullpobug.Example.Spring4d.Calculator
  , Nullpobug.Example.Spring4d.RemoteMathService
  ;

var
  FCalculator: TCalculator;

begin
  try
    FCalculator := TCalculator.Create;
    try
      Writeln(FCalculator.MathService.Name);
      Writeln(FCalculator.Addition(10, 20));
      Writeln(FCalculator.Multiplication(10, 20));
    finally
      FCalculator.Free;
    end;
  except
    on E: Exception do
      Writeln(E.ClassName, ': ', E.Message);
  end;
end.
