unit Nullpobug.Example.Spring4d.CalculatorGUI;

interface

implementation

uses
  Vcl.Forms
  , Nullpobug.Example.Spring4d.ServiceLocator
  , Nullpobug.Example.Spring4d.CalculatorUIIntf
  , Nullpobug.Example.Spring4d.CalculatorGUIForm
  ;

type
  TCalculatorGUIImpl = class(TInterfacedObject, ICalcuratorUI)
    constructor Create;
    procedure WriteLine(S: String);
    function Name: String;
  end;

constructor TCalculatorGUIImpl.Create;
begin
  Application.CreateForm(TCalculatorGUIForm, CalculatorGUIForm);
  CalculatorGUIForm.Show;
end;

procedure TCalculatorGUIImpl.WriteLine(S: String);
begin
  CalculatorGUIForm.WriteLine(S);
end;

function TCalculatorGUIImpl.Name: String;
begin
  Result := ToString;
end;

procedure RegisterCalculatorGUI;
begin
  ServiceLocator.RegisterComponent<TCalculatorGUIImpl>.Implements<ICalcuratorUI>;
  ServiceLocator.Build;
end;

initialization
  RegisterCalculatorGUI;
  Application.Initialize;

finalization
  Application.Run;

end.
