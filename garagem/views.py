from rest_framework.viewsets import ModelViewSet

from garagem.models import Categoria, Acessorio, Marca, Modelo, Veiculo, Cor
from garagem.serializers import (CategoriaSerializer, AcessorioSerializer, CorSerializer, MarcaSerializer, ModeloSerializer, VeiculoSerializer)

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return VeiculoListSerializer 
        elif self.action == "retrieve":
            return VeiculoDetailSerializer
        return VeiculoSerializer

# Create your views here.
