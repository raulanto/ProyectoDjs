from django.urls import  path, include
from rest_framework import routers
from panel import views
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'municipio',views.MunicipioView,'municipio')
router.register(r'estado',views.EstadoView,'estado')
urlpatterns =[
    path("api/v1/", include(router.urls)),
    path("docs", include_docs_urls("Panel API")),
    path('api/v1/municipio/por_estado/<int:estado_id>/', views.MunicipiosPorEstadoList.as_view(),
         name='municipios-por-estado'),

]