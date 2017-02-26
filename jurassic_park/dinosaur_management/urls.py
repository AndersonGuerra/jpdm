from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.inicio),

    url(r'^cadastro$', views.cadastro),

    url(r'^gerenciar$', views.gerenciar),

    url(r'^alterar$', views.alterar),

    url(r'^excluir$', views.excluir),

    url(r'^sobre$', views.sobre)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
