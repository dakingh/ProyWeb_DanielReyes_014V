from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Carrito, DetalleCarrito
from .forms import ProductoForm, CustomUserCreationForm, UserUpdateForm
from urllib.parse import unquote
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')


def contacto(request):
    return render(request, 'myapp/contacto.html')


def feriados(request):
    return render(request, 'myapp/feriados.html')


def galeria(request):
    return render(request, 'myapp/galeria.html')


def materiales(request):
    return render(request, 'myapp/materiales.html')


def base(request):
    return render(request, 'myapp/base.html')


def tienda_productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'myapp/tienda.html', data)


@permission_required('myapp.add_producto')
def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }
    if request.method == "POST":
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Creado Correctamente!!!")
        else:
            data["form"] = formulario
    return render(request, 'myapp/agregar.html', data)


@permission_required('myapp.view_producto')
def listar_productos(request):
    productos = Producto.objects.all().order_by('codigo')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'myapp/listar.html', data)


@permission_required('myapp.change_producto')
def modificar_productos(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == "POST":
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente!!")
            return redirect(to="listar_productos")
        data["form"] = formulario
    return render(request, 'myapp/modificar.html', data)


@permission_required('myapp.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente!!")
    return redirect(to="listar_productos")


def registro(request):
    data = {
        'form': CustomUserCreationForm
    }

    if request.method == "POST":
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registrado Correctamente")
            return redirect(to="index")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)


@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if producto.stock > 0:
        carrito, created = Carrito.objects.get_or_create(usuario=request.user, estado='pendiente')
        
        precio = producto.precio  # El precio ahora es un entero
        
        detalle, created = DetalleCarrito.objects.get_or_create(
            carrito=carrito, 
            producto=producto, 
            defaults={'precio': precio}
        )
        if not created:
            detalle.cantidad += 1
            detalle.save()
        
        # Descontar el stock del producto
        producto.stock -= 1
        producto.save()
        
        messages.success(request, "Producto agregado al carrito!")
    else:
        messages.error(request, "Stock insuficiente para este producto.")
    
    return redirect('tienda_productos')


@login_required
def ver_carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user, estado='pendiente').first()
    if not carrito:
        carrito = Carrito.objects.create(usuario=request.user, estado='pendiente')
    
    total = sum(detalle.subtotal() for detalle in carrito.detalles.all())
    
    data = {
        'carrito': carrito,
        'total': total
    }
    return render(request, 'myapp/carrito.html', data)


@login_required
def comprar_carrito(request, carrito_id):
    carrito = get_object_or_404(Carrito, id=carrito_id, usuario=request.user)
    carrito.marcar_como_recibido()
    messages.success(request, 'Compra realizada con éxito')
    return redirect('informacion_carrito', carrito_id=carrito.id)


@login_required
def informacion_carrito(request, carrito_id):
    carrito = get_object_or_404(Carrito, id=carrito_id)
    informacion = carrito.mostrar_informacion_compra()
    return render(request, 'myapp/informacion_carrito.html', {'informacion': informacion})


@staff_member_required
def listar_ventas(request):
    carritos = Carrito.objects.filter(estado='recibido').order_by('-fecha_compra')
    return render(request, 'myapp/listar_ventas.html', {'carritos': carritos})


@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu perfil ha sido actualizado!')
            return redirect('editar_perfil')
    else:
        form = UserUpdateForm(instance=request.user)
    
    context = {
        'form': form
    }
    return render(request, 'myapp/editar_perfil.html', context)