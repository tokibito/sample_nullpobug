program test_zerobased_str;

{$APPTYPE CONSOLE}
{$ZEROBASEDSTRINGS OFF}

var
  Foo: String;
  I: Integer;

begin
  Foo := 'ABCDE';
  for I := 0 to Length(Foo) - 1 do
    Writeln(Foo[I]);
end.
