# Para DRF siempre va aqui la logica del negocio + la relacion de los serializers
from rest_framework import generics

from .models import Categoria, Producto, Cliente,Pedido

from .serializers import (
    CategoriaSerializer,
    ProductoSerializer,
    ClienteSerializer,
    CatergoriaProductosSerializer,
    PedidoSerializer,
    )

# Metodos GET de Categorias
class CategoriaListView(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
# Metodos GET de Productos
class ProductoListView(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
# Cliente get, put
class ClienteView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# Cliente get one, put, delete
class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    lookup_url_kwarg = 'cliente_id'
    serializer_class = ClienteSerializer
    
class CategoriaProductosView(generics.RetrieveAPIView):
    queryset = Categoria.objects.all()
    lookup_url_kwarg = 'categoria_id'
    serializer_class = CatergoriaProductosSerializer
    
class PedidoCreateView(generics.CreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer