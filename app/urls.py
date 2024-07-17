from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="app/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path("customers_list/", views.customers_list, name="customers_list"),
    path('customer/<int:pk>/toggle_status/', views.toggle_customer_status, name='toggle_customer_status'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
