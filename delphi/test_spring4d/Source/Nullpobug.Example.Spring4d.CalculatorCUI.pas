unit Nullpobug.Example.Spring4d.CalculatorCUI;

interface

implementation

uses
  Nullpobug.Example.Spring4d.ServiceLocator
  , Nullpobug.Example.Spring4d.CalculatorUIIntf
  ;

type
  TCalculaterCUIImpl = class(TInterfacedObject, ICalcuratorUI)
    procedure WriteLine(S: String);
    function Name: String;
  end;

procedure TCalculaterCUIImpl.WriteLine(S: String);
begin
  Writeln(S);
end;

function TCalculaterCUIImpl.Name: String;
begin
  Result := ToString;
end;

procedure RegisterCalculatorCUI;
begin
  ServiceLocator.RegisterComponent<TCalculaterCUIImpl>.Implements<ICalcuratorUI>;
  ServiceLocator.Build;
end;

initialization
  RegisterCalculatorCUI;

end.
