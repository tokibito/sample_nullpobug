unit Nullpobug.Example.Spring4d.MathServiceIntf;

interface

type
  IMathService = interface
    ['{0455C256-9FFB-41B3-B00E-43FB3E06E516}']
    function Add(a, b: integer): integer;
    function Multiply(a, b: integer): integer;
    function Name: String;
  end;

implementation

end.
