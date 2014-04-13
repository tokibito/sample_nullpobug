// ************************************************************************ //
// このファイルに宣言されている型は、下記の WSDL ファイルから
// 読み取られたデータから生成されました:
// WSDL     : http://localhost:5000/wsdl/IMathResource
// バージョン  : 1.0
// (2014/04/13 22:13:57 - - $Rev: 56641 $)
// ************************************************************************ //

unit Nullpobug.Example.Spring4d.MathResource;

interface

uses
  Soap.InvokeRegistry
  , Soap.SOAPHTTPClient
  , Soap.XSBuiltIns
  , System.Types
  , System.Win.ComObj
  , Winapi.ActiveX
  , Xml.xmldom
  ;

type

  // ************************************************************************ //
  // WSDL ドキュメントで参照される、次の型は、
  // このファイルで表現されていません。これらは、表現された、または参照された、別の型のエイリアス [@] ですが、
  // ドキュメントで [!] 宣言されていません。後者のカテゴリの型は
  // 一般に事前定義/既知の XML (Embarcadero 型) にマップされます。ただし
  // スキーマ型の宣言またはインポートに失敗した無効な WSDL ドキュメントを示すこともできます。
  // ************************************************************************ //
  // !:int             - "http://www.w3.org/2001/XMLSchema"[]


  // ************************************************************************ //
  // 名前空間 : urn:MathResourceIntf-IMathResource
  // SOAP アクション: urn:MathResourceIntf-IMathResource#%operationName%
  // トランスポート : http://schemas.xmlsoap.org/soap/http
  // スタイル       : rpc
  // 使用       : encoded
  // バインディング   : IMathResourcebinding
  // サービス  : IMathResourceservice
  // ポート   : IMathResourcePort
  // URL            : http://localhost:5000/soap/IMathResource
  // ************************************************************************ //
  IMathResource = interface(IInvokable)
  ['{ED670BD7-8A5C-37AC-0A43-09B7ADD5A0C5}']
    function  Add(const A: Integer; const B: Integer): Integer; stdcall;
    function  Multiply(const A: Integer; const B: Integer): Integer; stdcall;
  end;

function GetIMathResource(UseWSDL: Boolean=System.False; Addr: string=''; HTTPRIO: THTTPRIO = nil): IMathResource;


implementation
  uses System.SysUtils;

function GetIMathResource(UseWSDL: Boolean; Addr: string; HTTPRIO: THTTPRIO): IMathResource;
const
  defWSDL = 'http://localhost:5000/wsdl/IMathResource';
  defURL  = 'http://localhost:5000/soap/IMathResource';
  defSvc  = 'IMathResourceservice';
  defPrt  = 'IMathResourcePort';
var
  RIO: THTTPRIO;
begin
  Result := nil;
  if (Addr = '') then
  begin
    if UseWSDL then
      Addr := defWSDL
    else
      Addr := defURL;
  end;
  if HTTPRIO = nil then
    RIO := THTTPRIO.Create(nil)
  else
    RIO := HTTPRIO;
  try
    Result := (RIO as IMathResource);
    if UseWSDL then
    begin
      RIO.WSDLLocation := Addr;
      RIO.Service := defSvc;
      RIO.Port := defPrt;
    end else
      RIO.URL := Addr;
  finally
    if (Result = nil) and (HTTPRIO = nil) then
      RIO.Free;
  end;
end;


initialization
  {$IFDEF MACOSX}
  DefaultDOMVendor := 'ADOM XML v4';
  {$ELSE}
  CoInitializeEx(nil, COINIT_MULTITHREADED);
  DefaultDOMVendor := 'MSXML';
  {$ENDIF}
  { IMathResource }
  InvRegistry.RegisterInterface(TypeInfo(IMathResource), 'urn:MathResourceIntf-IMathResource', '');
  InvRegistry.RegisterDefaultSOAPAction(TypeInfo(IMathResource), 'urn:MathResourceIntf-IMathResource#%operationName%');

end.
