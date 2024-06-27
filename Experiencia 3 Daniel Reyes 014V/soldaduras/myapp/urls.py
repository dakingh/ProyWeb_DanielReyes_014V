from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('contacto/', views.contacto, name='contacto'),  
    path('feriados/', views.feriados, name='feriados'),  
    path('galeria/', views.galeria, name='galeria'),  
    path('materiales/', views.materiales, name='materiales'),
    path('base/', views.base, name='base'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('tienda/', views.tienda_productos, name='tienda_productos'),
    path('listar-productos/', views.listar_productos, name="listar_productos"),
    path('modificar-productos/<id>/', views.modificar_productos, name="modificar_productos"),
    path('eliminar_producto/<int:id>/', views.eliminar_producto, name="eliminar_producto"),
    path('registro/', views.registro, name="registro"),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('comprar_carrito/<int:carrito_id>/', views.comprar_carrito, name='comprar_carrito'),
    path('informacion_carrito/<int:carrito_id>/', views.informacion_carrito, name='informacion_carrito'),
    path('listar_ventas/', views.listar_ventas, name='listar_ventas'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
]
