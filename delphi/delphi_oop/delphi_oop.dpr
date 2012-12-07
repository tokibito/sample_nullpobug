program testoop;

{$APPTYPE CONSOLE}

uses
  System.SysUtils
  ;

type
  ISay = interface(IInterface)
    procedure Say;
  end;

  TParent = class(TInterfacedObject, ISay)
  private
    FValue: Integer;
  public
    procedure Say; virtual;
    property Value: Integer read FValue write FValue;
  end;

  TChild = class(TParent)
  public
    procedure Say; override;
  end;

procedure TParent.Say;
begin
  Writeln('Parent.Say: ' + IntToStr(FValue));
end;

procedure TChild.Say;
begin
  Writeln('Child.Say: ' + IntToStr(FValue));
end;

var
  Obj1, Obj2: TParent;

begin
  Obj1 := TParent.Create;
  Obj1.Value := 10;
  Obj1.Say;
  Obj2 := TChild.Create;
  Obj2.Value := 20;
  Obj2.Say;
end.
