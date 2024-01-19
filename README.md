# Proje Yönetim Uygulaması
Bir şirket vb. kurum içerisinde yapılan projeleri, projelere eklenen görevleri (task) ve bu görevleri yapacak çalışanları yönetebildiğiniz bir web sitesi.

## Başlangıç

Projeyi yerel bilgisayarınıza klonlayın.

```bash
git clone https://github.com/kullanici_adi/proje_adı.git
```

## Gereksinimler
Projenin çalışması için gerekli olan paketleri yüklemek için aşağıdaki komutu kullanın.
```
pip install -r requirements.txt
```

## Veritabanı Migrations
Proje içindeki Django modellerini veritabanına uygulamak için aşağıdaki komutları kullanın.
```
python manage.py makemigrations
python manage.py migrate
```

## Çalıştırma
Proje Django geliştirme sunucusu üzerinde çalıştırabilirsiniz.
```
python manage.py runserver
```
