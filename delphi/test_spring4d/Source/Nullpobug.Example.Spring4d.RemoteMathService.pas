unit Nullpobug.Example.Spring4d.RemoteMathService;

interface

implementation

uses
  Nullpobug.Example.Spring4d.ServiceLocator
  , Nullpobug.Example.Spring4d.MathServiceIntf
  , Nullpobug.Example.Spring4d.MathResource
  ;

type
  TRemoteMathServiceImpl = class(TInterfacedObject, IMathService)
  private
    FMathResource: IMathResource;
  public
    constructor Create;
    function Add(A, B: integer): Integer;
    function Multiply(A, B: integer): Integer;
    function Name: String;
  end;

{ TRemoteMathServiceImpl }

constructor TRemoteMathServiceImpl.Create;
begin
  FMathResource := GetIMathResource;
end;

function TRemoteMathServiceImpl.Add(A, B: Integer): Integer;
begin
  Result := FMathResource.Add(A, B);
end;

function TRemoteMathServiceImpl.Multiply(A, B: Integer): Integer;
begin
  Result := FMathResource.Multiply(A, B);
end;

function TRemoteMathServiceImpl.Name: String;
begin
  Result := ToString;
end;

procedure RegisterRemoteMathService;
begin
  ServiceLocator.RegisterComponent<TRemoteMathServiceImpl>.Implements<IMathService>;
  ServiceLocator.Build;
end;

initialization
  RegisterRemoteMathService;

end.
