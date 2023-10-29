from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.clasificacion, name='clasificacion'),
    path('caracteristicas', views.caracteristicas, name='caracteristicas'),
    path('ajax/clasificacion', views.ajaxClasificacion, name='ajaxClasificacion'),
    path('ajax/caracteristicas', views.ajaxCaracteristicas, name='ajaxCaracteristicas')
]

"""
path('gdp/', views.gdp, name='gdp'),
path('', views.dashboard, name=''),
path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

path('ajax/getSubIndicadores/', views.get_sub_indicadores, name='get_sub_indicadores'),
path('ajax/getIndicadoresDefinitionByUnidad/', views.get_indicadores_definition_by_unidad, name='get_indicadores_definition_by_unidad'),
path('ajax/getSubSectores/', views.get_sub_sectores, name='get_sub_sectores'),
path('ajax/getDataIndicador/', views.get_data_indicador, name='get_data_indicador'),
path('ajax/getPrincipalLayout/', views.get_principal_layout, name='get_principal_layout'),
"""