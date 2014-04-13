unit MathResourceImpl;

interface

uses Soap.InvokeRegistry, System.Types, Soap.XSBuiltIns, MathResourceIntf;

type

  TMathResource = class(TInvokableClass, IMathResource)
  public
    function Add(A, B: Integer): Integer;
    function Multiply(A, B: Integer): Integer;
  end;

implementation

function TMathResource.Add(A, B: Integer): Integer;
begin
  Result := A + B;
end;

function TMathResource.Multiply(A, B: Integer): Integer;
begin
  Result := A * B;
end;

initialization
   InvRegistry.RegisterInvokableClass(TMathResource);
end.

