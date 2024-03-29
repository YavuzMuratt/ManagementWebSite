# Generated by Django 5.0 on 2024-01-04 18:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gorev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aciklama', models.TextField(default='Bu proje hakkında bir açıklama bulunmamaktadır.')),
                ('baslangic_tarihi', models.DateField()),
                ('bitis_tarihi', models.DateField()),
                ('durum', models.CharField(choices=[('Tamamlanacak', 'Tamamlanacak'), ('Devam Ediyor', 'Devam Ediyor'), ('Tamamlandı', 'Tamamlandı')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Proje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proje_adi', models.CharField(max_length=255)),
                ('aciklama', models.TextField(choices=[('Devam Ediyor', 'Devam Ediyor'), ('Tamamlandı', 'Tamamlandı')], max_length=20)),
                ('baslangic_tarihi', models.DateField()),
                ('bitis_tarihi', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Kullanici',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasks', models.ManyToManyField(to='YonetimWebSite.gorev')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='gorev',
            name='proje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YonetimWebSite.proje'),
        ),
    ]
