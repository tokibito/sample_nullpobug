var myApp = angular.module('myApp', []);

myApp.controller('myController', function ($scope, $http) {
  $scope.items = [];
  $scope.load = function(url) {
    // ajaxの例
    $http.get(url).success(function (data, status, headers, config) {
      $scope.items = data;
    });
  };

  $scope.addItem = function() {
    var item = {};
    $scope.items.push(item);
  };

  $scope.deleteItem = function() {
    var newItems = [];
    // angularのforEach
    angular.forEach($scope.items, function(item) {
      if (!item.selected) {
        newItems.push(item);
      }
    });
    $scope.items = newItems;
  };

  $scope.selectAll = function() {
    angular.forEach($scope.items, function(item) {
      item.selected = true;
    });
  }

  $scope.ok = function() {
    // DOM操作にjQueryを使う
    $("#target").text(angular.toJson($scope.items));
  };
});
