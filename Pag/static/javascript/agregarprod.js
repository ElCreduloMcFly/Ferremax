function Producto(nombre, precio, imagen, descripcion, cantidad, categoria){
    this.nombre = nombre;
    this.precio = precio;
    this.imagen = imagen;
    this.descripcion = descripcion;
    this.cantidad = cantidad;
    this.categoria = categoria;
}
function previewImage(event) {
    var reader = new FileReader();
    reader.onload = function() {
      var output = document.getElementById('preview');
      output.src = reader.result;
    };
    reader.readAsDataURL(event.target.files[0]);
  }
  
var app = angular.module('lista_de_productos', []);
app.controller('control_principal', ['$scope', function($scope){  
    $scope.productos = [];
    
    $scope.agregar_producto = function(producto){
        // Convertimos la imagen a una URL de objeto para poder mostrarla
        if (producto.imagen) {
            var reader = new FileReader();
            reader.onload = function(e) {
                $scope.$apply(function() {
                    producto.imagen = e.target.result;

                    $scope.productos.push(
                        new Producto(
                            producto.nombre, 
                            producto.precio,
                            producto.imagen,
                            producto.descripcion,
                            producto.cantidad,
                            producto.categoria
                        )
                    );
                    $scope.producto = {};
                });
            };
            reader.readAsDataURL(producto.imagen);
        } else {
            $scope.productos.push(
                new Producto(
                    producto.nombre, 
                    producto.precio,
                    producto.imagen,
                    producto.descripcion,
                    producto.cantidad,
                    producto.categoria
                )
            );
            $scope.producto = {};
        }
    };
}]);

$(document).ready(function() {
    $('#tabla-productos').DataTable();
});
