program CalculatorTest;

{$APPTYPE CONSOLE}

uses
  System.SysUtils
  , Nullpobug.UnitTest
  , Nullpobug.Example.Spring4d.Calculator
  , Nullpobug.Example.Spring4d.CalculatorTest
  , Nullpobug.Example.Spring4d.LocalMathService  // ここで依存性注入
  ;

begin
  try
    // ReportMemoryLeaksOnShutdown := True;
    Nullpobug.UnitTest.RunTest;  
  except
    on E: Exception do
      Writeln(E.ClassName, ': ', E.Message);
  end;
end.
