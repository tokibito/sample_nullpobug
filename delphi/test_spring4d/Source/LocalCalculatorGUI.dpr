program LocalCalculatorGUI;

{$APPTYPE GUI}

uses
  System.SysUtils
  , Nullpobug.Example.Spring4d.Calculator
  , Nullpobug.Example.Spring4d.LocalMathService  // ここで依存性注入
  , Nullpobug.Example.Spring4d.CalculatorGUI  // ここで依存性注入
  ;

begin
  try
    TCalculator.Main;
  except
    on E: Exception do
      Writeln(E.ClassName, ': ', E.Message);
  end;
end.
