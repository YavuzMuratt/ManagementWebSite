from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Proje, Gorev, Calisan
from bootstrap_datepicker_plus.widgets import DatePickerInput


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    pass


class ProjeForm(forms.ModelForm):
    class Meta:
        model = Proje
        fields = ['proje_adi', 'aciklama', 'baslangic_tarihi', 'bitis_tarihi']

    # Durum alanı için combobox (kaydırmalı seçenek kutusu) ekleyin
    aciklama = forms.ChoiceField(choices=Proje.DURUM_SECENEKLERI, label='Durum')
    widgets = {
        'baslangic_tarihi': DatePickerInput(),
        'bitis_tarihi': DatePickerInput(),
    }


class GorevForm(forms.ModelForm):
    class Meta:
        model = Gorev
        fields = ['aciklama', 'baslangic_tarihi', 'bitis_tarihi', 'durum', 'proje', 'calisan']

    def __init__(self, *args, **kwargs):
        super(GorevForm, self).__init__(*args, **kwargs)
        # Proje alanını dropdown şeklinde göstermek için
        self.fields['proje'].widget = forms.Select()
        self.fields['proje'].queryset = Proje.objects.all()


class GorevDurumForm(forms.ModelForm):
    class Meta:
        model = Gorev
        fields = ['durum']


class CalisanForm(forms.ModelForm):
    class Meta:
        model = Calisan
        fields = ['user', 'ad', 'soyad', 'gorevler']

