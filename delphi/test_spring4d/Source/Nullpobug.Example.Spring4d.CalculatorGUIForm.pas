unit Nullpobug.Example.Spring4d.CalculatorGUIForm;

interface

uses
  Winapi.Windows
  , Winapi.Messages
  , System.SysUtils
  , System.Variants
  , System.Classes
  , Vcl.Graphics
  , Vcl.Controls
  , Vcl.Forms
  , Vcl.Dialogs
  , Vcl.StdCtrls;

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

{$R *.dfm}

procedure TCalculatorGUIForm.FormCreate(Sender: TObject);
begin
  DisplayArea.Lines.Clear;
end;

procedure TCalculatorGUIForm.WriteLine(S: String);
begin
  DisplayArea.Lines.Add(S);
end;

end.
