from sections.urls import catch_all, section_routes

from . import views

urlpatterns = section_routes('products', views.ProductsView, 'products')
urlpatterns += catch_all('products', views.ProductsView, 'products')
