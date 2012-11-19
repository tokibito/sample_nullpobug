program hexdump;

{$APPTYPE CONSOLE}

uses
  System.SysUtils
  , System.Classes
  ;

var
  FileStream: TFileStream;
  Column, I: Integer;
  ReadLength: Longint;
  Buffer: array [0..255] of Byte;

begin
  (* コマンドライン引数が無ければ終了 *)
  if ParamCount = 0 then
  begin
    Writeln(Format('%s <filepath>', [ExtractFileName(ParamStr(0))]));
    Exit;
  end;
  (* ファイルを読み込み専用で開く *)
  FileStream := TFileStream.Create(ParamStr(1), fmOpenRead);
  try
    Column := 0;
    while True do
    begin
      ReadLength := FileStream.Read(Buffer, SizeOf(Buffer));
      if ReadLength = 0 then
        Break;
      for I := 0 to ReadLength - 1 do
      begin
        (* 改行 *)
        if Column = 16 then
        begin
          Column := 0;
          Writeln('');
        end;
        (* 16進数で画面に出力 *)
        Write(Format('%.2x ', [Buffer[I]]));
        Inc(Column);
      end;
    end;
  finally
    (* ファイルを閉じる *)
    FreeAndNil(FileStream);
  end;
end.
