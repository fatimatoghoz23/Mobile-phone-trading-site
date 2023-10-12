from django.urls import path

from . import views

urlpatterns = [
    path('product/<str:id>/',views.product,name='product'),#لعرض تفاصيل المنتج
    path('products/',views.products,name='products'),

]