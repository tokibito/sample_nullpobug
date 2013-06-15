unit MyLibrary;

interface

uses
  FMX.Dialogs;

function Add(X, Y: Integer): Integer; cdecl;
procedure Say(Text: PAnsiChar); cdecl;

exports
  {$IFDEF MACOS}
  Add name '_Add',
  Say name '_Say'
  {$ELSE}
  Add,
  Say
  {$ENDIF}
  ;

implementation

function Add(X, Y: Integer): Integer; cdecl;
begin
  Result := X + Y;
end;

procedure Say(Text: PAnsiChar); cdecl;
begin
  ShowMessage(UTF8ToString(Text));
end;

end.
