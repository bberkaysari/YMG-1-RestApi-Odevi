# YMG 1 - REST API Ödevi

Bu proje, bir RESTful API uygulamasını geliştirmek ve bir **Linux servisi** olarak çalıştırılabilir hale getirmek amacıyla hazırlanmıştır. Uygulama, Python'da Flask framework'ü ile geliştirilmiş ve Debian paketine dönüştürülerek kolayca dağıtılabilir hale getirilmiştir.

## Özellikler
- **Flask RESTful API**: Veri işlemleri için basit bir REST API.
- **Systemd Servisi**: Uygulama, `systemctl` komutu ile yönetilebilecek bir servis olarak çalıştırılabilir.
- **Debian Paketi**: Uygulama ve servis, bir Debian paketi içerisinde dağıtılabilir.
- **Bağımlılık Yönetimi**: Gerekli tüm bağımlılıklar `requirements.txt` üzerinden kurulabilir.

  
 ## Çalıştırma Komutları
```bash
 curl "http://127.0.0.1:3838/sum?a=9&b=7"
 curl "http://127.0.0.1:3838/subtract?a=9&b=7"
 curl -X POST -H "Content-Type: application/json" -d '{"num1": 6, "num2": 3}' http://127.0.0.1:3838/multiply
 curl -X POST -H "Content-Type: application/json" -d '{"num1": 10, "num2": 2}' http://127.0.0.1:3838/divide
```
## Kurulum

### 1. Gerekli Bağımlılıkların Yüklenmesi
- Python 3.9 veya daha üstü bir sürüm gereklidir.
- Aşağıdaki komutlarla gerekli bağımlılıkları yükleyebilirsiniz:
  ```bash
  pip install -r requirements.txt
  ```

### 2. Uygulamanın Çalıştırılması
- Uygulamayı manuel olarak çalıştırmak için:
  ```bash
  python app.py
  ```

### 3. Systemd Servisi Olarak Çalıştırma
- **Servis Dosyasını Kopyalayın**:
  Servis dosyasını systemd dizinine taşıyın:
  ```bash
  sudo cp myapp.service /etc/systemd/system/
  ```

- **Servisi Başlatın**:
  ```bash
  sudo systemctl daemon-reload
  sudo systemctl start myapp.service
  sudo systemctl enable myapp.service
  ```

- **Servis Durumunu Kontrol Edin**:
  ```bash
  systemctl status myapp.service
  ```

### 4. Debian Paketi Oluşturma
Debian paketini oluşturmak için proje dizininde şu adımları izleyin:
```bash
dpkg-deb --build myapp
```
Oluşan `.deb` dosyasını kullanarak uygulamayı kurabilirsiniz:
```bash
sudo dpkg -i myapp.deb
```

## Kullanılan Teknolojiler
- **Python**: Uygulamanın geliştirilmesi için.
- **Flask**: REST API oluşturmak için.
- **Systemd**: Linux servis yönetimi.
- **Debian Paketleme**: Uygulama ve servisi dağıtmak için.



## Proje Yapısı
```
.
├── app.py               # Ana uygulama dosyası
├── requirements.txt     # Bağımlılık dosyası
├── myapp.service        # Systemd servis dosyası
├── debian/              # Debian paketleme dosyaları
└── README.md            # Proje açıklama dosyası
```


