unit invokes;

{$IFDEF FPC}
{$MODE Delphi}
{$ENDIF}

interface

uses
  SysUtils;

type
  TMethodtableEntry = packed record
    Name: PShortString;
    Address: Pointer;
  end;

  TPlainMethod = procedure of object;

  procedure InvokeMethod(Obj: TObject; Name: string; AClass: TClass);

implementation

procedure InvokeMethod(Obj: TObject; Name: string; AClass: TClass);
var
  pp: ^Pointer;
  pMethodTable: Pointer;
  pMethodEntry: ^TMethodTableEntry;
  I, numEntries: Word;
  VMethod: TMethod;
  VPlainMethod: TPlainMethod absolute VMethod;
begin
  if AClass = nil then Exit;
  pp := Pointer(NativeUInt(AClass) + vmtMethodtable);
  pMethodTable := pp^;
  if pMethodtable <> nil then begin
    numEntries := PByte(pMethodTable)^;
    pMethodEntry := Pointer(NativeUInt(pMethodTable) + 4);
    for I := 1 to numEntries do
    begin
      if LowerCase(pMethodEntry^.Name^) = LowerCase(Name) then
      begin
        VMethod.Code := pMethodEntry^.address;
        VMethod.Data := Obj;
        VPlainMethod;
      end;
      pMethodEntry := Pointer(NativeUInt(pMethodEntry) + SizeOf(TMethodtableEntry));
    end;
  end;
  InvokeMethod(Obj, Name, AClass.ClassParent);
end;

end.
