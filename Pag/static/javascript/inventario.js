var app = angular.module('inventarioApp', []);

app.controller('inventarioController', ['$scope', '$http', function($scope, $http) {
    $scope.productos = [];
    $scope.nuevoProducto = {};

    $scope.obtenerProductos = function() {
        $http.get('/api/productos/')
            .then(function(response) {
                $scope.productos = response.data;
            }, function(error) {
                console.error('Error al obtener los productos:', error);
            });
    };

    $scope.obtenerProductos();

    $scope.agregarProducto = function() {
        $http.post('/api/productos/', $scope.nuevoProducto)
            .then(function(response) {
                $scope.productos.push(response.data);
                $scope.nuevoProducto = {};
            }, function(error) {
                console.error('Error al agregar el producto:', error);
            });
    };

    $scope.editarProducto = function(producto) {
        $scope.productoSeleccionado = angular.copy(producto);
        document.getElementById('editModal').style.display = "block";
    };

    $scope.closeModal = function() {
        document.getElementById('editModal').style.display = "none";
    };

    $scope.guardarCambios = function() {
        $http.put('/api/productos/' + $scope.productoSeleccionado.id + '/', $scope.productoSeleccionado)
            .then(function(response) {
                var index = $scope.productos.findIndex(producto => producto.id === $scope.productoSeleccionado.id);
                $scope.productos[index] = response.data;
                $scope.closeModal();
            }, function(error) {
                console.error('Error al guardar los cambios:', error);
            });
    };

    $scope.eliminarProducto = function(producto){
        var index = $scope.productos.indexOf(producto);
        if (index !== -1) {
            $http.delete('/api/productos/' + producto.id + '/')
                .then(function(response) {
                    $scope.productos.splice(index, 1);
                }, function(error) {
                    console.error('Error al eliminar el producto:', error);
                });
        }
    };
}]);
