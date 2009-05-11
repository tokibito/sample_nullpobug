var HTTPObj = {};

HTTPObj.get = function(args) {
  var args = args;
  $.ajax({
    type : 'GET',
    data : args.data,
    url : args.url,
    success : function(data) {
      args.success(eval('('+data+')'));
    },
    error : function (XMLHttpRequest, textStatus, errorThrown) {
      args.error(eval('('+XMLHttpRequest.responseText+')'));
    }
  });
}
