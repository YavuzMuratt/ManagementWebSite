# Create your models here.
from datetime import timezone

from django.db import models
from django.contrib.auth.models import User

from django.db import models


class Proje(models.Model):
    DURUM_SECENEKLERI = (
        ('Devam Ediyor', 'Devam Ediyor'),
        ('Tamamlandı', 'Tamamlandı'),
    )

    proje_adi = models.CharField(max_length=255)
    aciklama = models.TextField(max_length=20, choices=DURUM_SECENEKLERI)
    # durum = models.TextField(max_length=20, choices=DURUM_SECENEKLERI, default='devam')
    baslangic_tarihi = models.DateField()
    bitis_tarihi = models.DateField()
    calisanlar = models.ManyToManyField(User, related_name='projeler')

    def __str__(self):
        return self.proje_adi

    def kontrol_ve_guncelle(self):
        # Projedeki tüm görevleri al
        projedeki_gorevler = self.gorev_set.all()

        # Eğer hiç görev yoksa, projenin durumunu güncelle
        if not projedeki_gorevler:
            self.aciklama = 'Tamamlandı'
            self.save()
        else:
            # Projedeki görevlerin durumunu kontrol et
            tamamlanmis_gorevler = projedeki_gorevler.filter(durum='Tamamlandı')

            # Eğer tüm görevler tamamlanmışsa, projenin durumunu güncelle
            if self.durum == 'Devam Ediyor' and self.bitis_tarihi <= timezone.now().date():
                self.durum = 'Tamamlandı'
                self.save()

    def save(self, *args, **kwargs):
        super(Proje, self).save(*args, **kwargs)
        # Log kaydını ekleyin
        if self.calisanlar.exists():  # Eğer projede çalışan kullanıcılar varsa
            Log.objects.create(kullanici=self.calisanlar.first(), mesaj=f"{self.calisanlar.first()} {self.proje_adi} projesini oluşturdu.")


class Gorev(models.Model):
    proje = models.ForeignKey(Proje, on_delete=models.CASCADE)
    calisan = models.ForeignKey(User, related_name='gorevler', null=True, blank=True, on_delete=models.SET_NULL)
    atanma_tarihi = models.DateField(null=True, blank=True)
    aciklama = models.TextField(default="Bu proje hakkında bir açıklama bulunmamaktadır.")
    baslangic_tarihi = models.DateField()
    bitis_tarihi = models.DateField()

    STATUS_CHOICES = [
        ('Tamamlanacak', 'Tamamlanacak'),
        ('Devam Ediyor', 'Devam Ediyor'),
        ('Tamamlandı', 'Tamamlandı'),
    ]
    durum = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.aciklama

    def save(self, *args, **kwargs):
        super(Gorev, self).save(*args, **kwargs)
        # Log kaydını ekleyin
        Log.objects.create(kullanici=self.calisan, mesaj=f"{self.calisan} {self.aciklama} görevini oluşturdu.")


class Calisan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    ad = models.CharField(max_length=255)
    soyad = models.CharField(max_length=255)
    gorevler = models.ManyToManyField('Gorev', related_name='calisanlar', blank=True)

    def __str__(self):
        return f"{self.ad} {self.soyad}"


class Log(models.Model):
    kullanici = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    mesaj = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)
