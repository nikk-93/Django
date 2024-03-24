from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('ordered_product/<int:client_id>/<int:show_step>',
         views.ProductView.as_view(),
         name='ordered_product'),
]
