from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Marca(models.Model):
    nombre= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, null=True, blank=True, default=None)
    imagen = models.ImageField(upload_to='productos', null=True)
    precio = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='pendiente')
    fecha_compra = models.DateTimeField(null=True, blank=True)  # Nuevo campo para la fecha de compra

    def marcar_como_recibido(self):
        self.estado = 'recibido'
        self.fecha_compra = timezone.now()
        self.save()

    def mostrar_informacion_compra(self):
        detalles = self.detalles.all()
        info = {
            'usuario': self.usuario.username,
            'fecha_compra': self.fecha_compra,
            'estado': self.estado,
            'productos': [{'nombre': detalle.producto.nombre, 'cantidad': detalle.cantidad, 'precio': detalle.precio} for detalle in detalles],
            'total': sum(detalle.subtotal() for detalle in detalles)
        }
        return info


class DetalleCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio = models.IntegerField()

    def subtotal(self):
        return self.cantidad * self.precio
