from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from garagem.views import CategoriaViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"acessorios", acessoriosViewSet)
router.register(r"cor", corViewSet)
router.register(r"marca", marcaViewSet)
router.register(r"modelo", modeloViewSet)
router.register(r"veiculo", veiculoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]