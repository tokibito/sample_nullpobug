unit MathResourceIntf;

interface

uses Soap.InvokeRegistry, System.Types, Soap.XSBuiltIns;

type

  IMathResource = interface(IInvokable)
  ['{D7C2E1AF-E5F0-4272-BF2D-CFF6D10DE12E}']
  function Add(A, B: Integer): Integer;
  function Multiply(A, B: Integer): Integer;
  end;

implementation

initialization
  InvRegistry.RegisterInterface(TypeInfo(IMathResource));

end.
