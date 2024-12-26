mkdir -p myapp/opt/myapp
mkdir -p myapp/etc/systemd/system
cp ../app/* myapp/opt/myapp/
cp ../service/myapp.service myapp/etc/systemd/system/
fpm -s dir -t deb -n myapp -v 1.0 --deb-systemd myapp/etc/systemd/system/myapp.service -C myapp .
rm -rf myapp
echo "Debian paketi oluşturuldu: myapp_1.0_amd64.deb"
