from django.contrib import admin
from django.urls import path
from tax_app import views

urlpatterns = [
    path('', views.default_view, name='default'),
    path('<int:price>/', views.calculate_tax_view, name='calculate_tax'),
    path('taxrate/', views.tax_rate_view, name='tax_rate'),
    path('admin/', admin.site.urls),
]