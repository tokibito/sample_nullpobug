library MyLibrary;

type
  TCallback = procedure; stdcall;

procedure DLLProc(Callback: TCallback);
begin
  Callback;
end;

exports DLLProc;

end.
