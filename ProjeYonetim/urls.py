"""
URL configuration for ProjeYonetim project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from YonetimWebSite import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('kayit/', views.kayit_ol, name='kayit'),
    path('giris/', auth_views.LoginView.as_view(template_name='giris.html'), name='giris'),
    path('inanasayfa/', views.inanasayfa, name='inanasayfa'),
    path('projeler/', views.projeler, name='projeler'),
    path('proje_listele/', views.projeleri_listele, name='proje_listele'),
    path('proje_ekle/', views.proje_ekle, name='proje_ekle'),
    path('gorevler/', views.gorevler, name='gorevler'),
    path('gorev_ekle/', views.gorev_ekle, name='gorev_ekle'),
    path('gorevleri_listele/', views.gorevleri_listele, name='gorevleri_listele'),
    path('gorev_durum_degistir/<int:gorev_id>/', views.gorev_durum_degistir, name='gorev_durum_degistir'),
    path('calisanlar/', views.calisanlari_listele, name='calisanlar'),
    path('calisan_ekle/', views.calisan_ekle, name='calisan_ekle'),
    path('calisan_detay/<int:calisan_id>/', views.calisan_detay, name='calisan_detay'),
    path('cikis/', auth_views.LogoutView.as_view(), name='cikis'),
]
