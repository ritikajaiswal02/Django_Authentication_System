from django.contrib import admin
from django.urls import path
from auapp.views import home,ulogin,usignup,ulogout

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("ulogin",ulogin,name="ulogin"),
    path("usignup",usignup,name="usignup"),
    path("ulogout",ulogout,name="ulogout"),
]
