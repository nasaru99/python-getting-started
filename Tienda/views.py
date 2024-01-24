from django.shortcuts import render

from .models import Greeting

# Create your views here.


def index(request):
    return render(request, "index.html")

from django.shortcuts import render
from .models import Categoria, Producto, Carrito, Pedido
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver


def inicio(request):
    return render(request, 'inicio.html')

def lista_productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    context = {
        'productos': productos,
        'categorias': categorias
    }
    return render(request, 'lista_productos.html', context)

def detalle_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})
@login_required
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'lista_categorias.html', {'categorias': categorias})

def productos_por_categoria(request, categoria_id):
    productos = Producto.objects.filter(categoria_id=categoria_id)
    return render(request, 'productos_por_categoria.html', {'productos': productos})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('productos')
    else:
        form = AuthenticationForm()
    return render(request, 'nombre_de_tu_template.html', {'form': form})

def db(request):
    # If you encounter errors visiting the `/db/` page on the example app, check that:
    #
    # When running the app on Heroku:
    #   1. You have added the Postgres database to your app.
    #   2. You have uncommented the `psycopg` dependency in `requirements.txt`, and the `release`
    #      process entry in `Procfile`, git committed your changes and re-deployed the app.
    #
    # When running the app locally:
    #   1. You have run `./manage.py migrate` to create the `hello_greeting` database table.

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
