'use strict';

angular.module('noviga')
  .factory('User', ['$resource', function ($resource) {
    return $resource('noviga/users/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
