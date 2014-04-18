unit Nullpobug.Example.Spring4d.CalculatorGUIForm;

interface

uses
  System.SysUtils
  , System.Types
  , System.UITypes
  , System.Rtti
  , System.Classes
  , System.Variants
  , FMX.Types
  , FMX.Controls
  , FMX.Forms
  , FMX.Dialogs
  , FMX.StdCtrls
  , FMX.Layouts
  , FMX.Memo
  ;

type
  TCalculatorGUIForm = class(TForm)
    DisplayArea: TMemo;
    procedure FormCreate(Sender: TObject);
  public
    procedure WriteLine(S: String);
  end;

var
  CalculatorGUIForm: TCalculatorGUIForm;

implementation

{$R *.fmx}

procedure TCalculatorGUIForm.FormCreate(Sender: TObject);
begin
  DisplayArea.Lines.Clear;
end;

procedure TCalculatorGUIForm.WriteLine(S: String);
begin
  DisplayArea.Lines.Add(S);
end;

end.
