unit Nullpobug.Example.Spring4d.CalculatorTest;

interface

uses
  System.SysUtils
  , Nullpobug.UnitTest
  , Nullpobug.Example.Spring4d.Calculator
  ;

type
  TCalculatorTest = class(TTestCase)
  private
    FCalculator: TCalculator;
  published
    procedure SetUp; override;
    procedure TearDown; override;
    procedure TestAddition;
    procedure TestMultiply;
  end;

implementation

procedure TCalculatorTest.SetUp;
begin
  FCalculator := TCalculator.Create;
end;

procedure TCalculatorTest.TearDown;
begin
  FCalculator.Free;
end;

procedure TCalculatorTest.TestAddition;
begin
  AssertEquals(FCalculator.Addition(2, 3), 5);
end;

procedure TCalculatorTest.TestMultiply;
begin
  AssertEquals(FCalculator.Multiplication(2, 3), 6);
end;

initialization
  RegisterTest(TCalculatorTest);

end.
