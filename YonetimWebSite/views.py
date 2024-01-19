# YonetimWebSite/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ProjeForm, GorevForm, CalisanForm, GorevDurumForm
from .models import Proje, Gorev, Calisan, User, Log


def home(request):
    return render(request, 'home.html', {})


def kayit_ol(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Başka bir sayfaya yönlendirme
    else:
        form = CustomUserCreationForm()
    return render(request, 'kayit.html', {'form': form})


def giris_yap(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Giriş başarılıysa yönlendirme yapabilirsiniz
    else:
        form = CustomAuthenticationForm()

    return render(request, 'giris.html', {'form': form})


@login_required
def inanasayfa(request):
    kullanici = request.user

    # Kullanıcının projelerini ve görevlerini sayma
    tamamlanan_gorevler = Gorev.objects.filter(calisan=kullanici, durum='Tamamlandı').count()
    devam_eden_gorevler = Gorev.objects.filter(calisan=kullanici, durum='Devam Ediyor').count()
    tamamlanamayan_gorevler = Gorev.objects.filter(calisan=kullanici, durum='Tamamlanacak').count()

    projeler = Proje.objects.filter(calisanlar=kullanici)

    # Sistem logunu çekme
    loglar = Log.objects.filter(kullanici=kullanici).order_by('-tarih')[:10]

    context = {
        'kullanici_adi': kullanici.get_full_name() if kullanici.get_full_name() else kullanici.username,
        'tamamlanan_gorev_sayisi': tamamlanan_gorevler,
        'devam_eden_gorev_sayisi': devam_eden_gorevler,
        'tamamlanamayan_gorev_sayisi': tamamlanamayan_gorevler,
        'projeler': projeler,
        'loglar': loglar,
    }

    return render(request, 'inanasayfa.html', context)


def projeler(request):
    return render(request, 'projeler.html', {'projeler': projeler})


def projeleri_listele(request):
    projeler = Proje.objects.all()
    return render(request, 'proje_listele.html', {'projeler': projeler})


def proje_ekle(request):
    if request.method == 'POST':
        form = ProjeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proje_listele')
    else:
        form = ProjeForm()

    return render(request, 'proje_ekle.html', {'form': form})


def gorevler(request):
    gorevler = Gorev.objects.all()
    projeler = Proje.objects.all()
    return render(request, 'gorevler.html', {'gorevler': gorevler, 'projeler': projeler})


"""
def gorev_ekle(request):
    if request.method == 'POST':
        form = GorevForm(request.POST)  # Eğer bir forms.py dosyanız varsa
        if form.is_valid():
            form.save()
            return redirect('gorevler')
    else:
        form = GorevForm()  # Eğer bir forms.py dosyanız varsa
    return render(request, 'gorev_ekle.html', {'form': form})
"""


def proje_listele(request):
    projeler = Proje.objects.all()

    # Her projenin durumunu kontrol et ve güncelle
    for proje in projeler:
        proje.kontrol_ve_guncelle()

    return render(request, 'proje_listele.html', {'projeler': projeler})


def projeyi_goster(request, proje_id):
    proje = Proje.objects.get(id=proje_id)
    gorevler = Gorev.objects.filter(proje=proje)
    return render(request, 'proje_goster.html', {'proje': proje, 'gorevler': gorevler})


def projeleri_ekle(request):
    if request.method == 'POST':
        form = ProjeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projeleri_listele')
    else:
        form = ProjeForm()
    return render(request, 'proje_ekle.html', {'form': form})


def calisanlari_listele(request):
    calisanlar = Calisan.objects.all()
    return render(request, 'calisanlar.html', {'calisanlar': calisanlar})


"""
def calisani_goster(request, calisan_id):
    calisan = Calisan.objects.get(id=calisan_id)
    projeler = Proje.objects.filter(gorev__calisan=calisan).distinct()
    tamamlanan_gorev_sayisi = Gorev.objects.filter(calisan=calisan, durum='Tamamlandı').count()
    devam_eden_gorev_sayisi = Gorev.objects.filter(calisan=calisan, durum='Devam Ediyor').count()
    baslamamis_gorev_sayisi = Gorev.objects.filter(calisan=calisan, durum='Tamamlanacak').count()
    return render(request, 'calisan_goster.html', {'calisan': calisan, 'projeler': projeler,
                                                   'tamamlanan_gorev_sayisi': tamamlanan_gorev_sayisi,
                                                   'devam_eden_gorev_sayisi': devam_eden_gorev_sayisi,
                                                   'baslamamis_gorev_sayisi': baslamamis_gorev_sayisi})
"""


def gorevleri_listele(request):
    gorevler = Gorev.objects.all()
    return render(request, 'gorevler.html', {'gorevler': gorevler})


def gorev_ekle(request):
    if request.method == 'POST':
        form = GorevForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gorevleri_listele')
    else:
        form = GorevForm()
    return render(request, 'gorev_ekle.html', {'form': form})


def gorev_durum_degistir(request, gorev_id):
    gorev = Gorev.objects.get(pk=gorev_id)

    if request.method == 'POST':
        form = GorevDurumForm(request.POST, instance=gorev)
        if form.is_valid():
            form.save()
            return redirect('gorevleri_listele')

    else:
        form = GorevDurumForm(instance=gorev)

    return render(request, 'gorev_durum_degistir.html', {'form': form, 'gorev': gorev})


def calisanlar(request):
    calisanlar = Calisan.objects.all()
    return render(request, 'calisanlar.html', {'calisanlar': calisanlar})


def calisan_detay(request, calisan_id):
    calisan = get_object_or_404(Calisan, id=calisan_id)
    return render(request, 'calisan_detay.html', {'calisan': calisan})


def calisan_ekle(request):
    if request.method == 'POST':
        form = CalisanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calisanlar')  # Çalışanlar sayfasına yönlendirme
    else:
        form = CalisanForm()

    return render(request, 'calisan_ekle.html', {'form': form, 'gorevler': Gorev.objects.all()})
