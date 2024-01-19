from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from views import giris_yap

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('kayit/', views.kayit_ol, name='kayit'),
    path('giris/', giris_yap, name='giris'),
    path('inanasayfa/', views.inanasayfa, name='inanasayfa'),
    path('projeler/', views.projeler, name='projeler'),
    path('proje_listele/', views.projeleri_listele, name='proje_listele'),
    path('proje_ekle/', views.proje_ekle, name='proje_ekle'),
    path('gorevler/', views.gorevler, name='gorevler'),
    path('gorev_ekle/', views.gorev_ekle, name='gorev_ekle'),
    path('gorevleri_listele/', views.gorevleri_listele, name='gorevleri_listele'),
    path('gorev_durum_degistir/<int:gorev_id>/', views.gorev_durum_degistir, name='gorev_durum_degistir'),
    path('calisanlar/', views.calisanlari_listele, name='calisanlari_listele'),
    path('calisan_ekle/', views.calisan_ekle, name='calisan_ekle'),
    path('calisan_detay/<int:calisan_id>/', views.calisan_detay, name='calisan_detay'),
    path('cikis/', auth_views.LogoutView.as_view(), name='cikis'),
]