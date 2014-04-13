program RemoteCalculator;

{$APPTYPE CONSOLE}

uses
  System.SysUtils
  , Nullpobug.Example.Spring4d.Calculator
  , Nullpobug.Example.Spring4d.RemoteMathService  // ここで依存性注入
  ;

var
  FCalculator: TCalculator;

begin
  try
    FCalculator := TCalculator.Create;
    try
      Writeln(FCalculator.MathService.Name);
      Writeln('10 + 20 = ', FCalculator.Addition(10, 20));
      Writeln('10 * 20 = ', FCalculator.Multiplication(10, 20));
    finally
      FCalculator.Free;
    end;
  except
    on E: Exception do
      Writeln(E.ClassName, ': ', E.Message);
  end;
end.
