unit Nullpobug.Example.Spring4d.Container;
 
interface
 
uses
  Spring.Container
  ;
 
function ServiceLocator: TContainer;
 
implementation
 
var
  FContainer: TContainer;
 
function ServiceLocator: TContainer;
begin
  if FContainer = nil then
  begin
    FContainer := TContainer.Create;
  end;
  Result := FContainer;
end;
 
end.
