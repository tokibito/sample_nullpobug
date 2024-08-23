unit invokes;

{$IFDEF FPC}
{$MODE Delphi}
{$ENDIF}

interface

uses
  SysUtils;

type
  TMethodtableEntry = packed record
    Name: PShortString;  // メソッド名
    Address: Pointer;  // メソッドの関数ポインタ
  end;

  TPlainMethod = procedure of object;  // 今回は引数無しのメソッド

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
  pp := Pointer(NativeUInt(AClass) + vmtMethodtable);  // 仮想メソッドテーブルのオフセット分アドレスずらし
  pMethodTable := pp^;
  if pMethodtable <> nil then begin
    numEntries := PDWord(pMethodTable)^;  // メソッドテーブルのエントリ数をポインタ経由で取得
    pMethodEntry := Pointer(NativeUInt(pMethodTable) + SizeOf(DWord));  // ポインタ分ずらしてエントリにアクセス
    for I := 1 to numEntries do
    begin
      if LowerCase(pMethodEntry^.Name^) = LowerCase(Name) then  // 指定されたメソッド名と同じ場合
      begin
        VMethod.Code := pMethodEntry^.address;  // メソッドの関数ポインタ
        VMethod.Data := Obj;  // SelfをAssign
        VPlainMethod;  // メソッド呼び出し
      end;
      pMethodEntry := Pointer(NativeUInt(pMethodEntry) + SizeOf(TMethodtableEntry));
    end;
  end;
  InvokeMethod(Obj, Name, AClass.ClassParent);
end;

end.
