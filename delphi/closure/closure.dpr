program closure;

{$APPTYPE CONSOLE}

type
  TIntCounterFunc = reference to function: Integer;

function MakeCounter(Initial: Integer = 0; Step: Integer = 1): TIntCounterFunc;
var
  Value: Integer;
begin
  Value := Initial;
  Result := function: Integer
  begin
    Result := Value;
    Inc(Value, Step);
  end;
end;

var
  counter1, counter2, counter3: TIntCounterFunc;
begin
  counter1 := MakeCounter();
  counter2 := MakeCounter(100, 2);
  counter3 := MakeCounter(20, 35);
  WriteLn('1: ', counter1);
  WriteLn('2: ', counter2);
  WriteLn('3: ', counter3);
  WriteLn('1: ', counter1);
  WriteLn('1: ', counter1);
  WriteLn('3: ', counter3);
  WriteLn('2: ', counter2);
  WriteLn('2: ', counter2);
end.
