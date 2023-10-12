from django.urls import path

from pages import chat

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<str:id>/',views.product,name='product'),
    path('products/',views.products,name='products'),
    path('laptops/',views.laptops,name='laptops'),
    path('update_item/',views.updateItem,name='update_item'),
    path('chatbotlisten/',chat.chatbotlisten,name='chatbotlisten'),
    path('process_order/',views.processOrder,name='process_order'),
    path('chatbot/',views.chatbot,name='chatbot'),
    path('search/',views.search,name='search'),
    path('login/',views.pagelogin,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logoutUser,name='logout'),
    path('update/<int:id>',views.update,name='update'),#لتعديل المنتج بالادمن
    path('delete/<int:id>',views.delete,name='delete'),#لتعديل المنتج بالادمن
    path('notfound/',views.error,name='notfound'),

]
