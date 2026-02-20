#!/bin/bash

# 1. Pip versiyonunu göster
pip --version

# 2. & 3. Kütüphaneyi 'local_lib' klasörüne kur ve logları kaydet
# --target: Kütüphaneyi nereye kuracağını belirtir.
# --upgrade: Eğer varsa üzerine yazar (crush it).
# git+...: GitHub deposundan direkt kurulum yapar.
# > install.log: Çıktıyı ekrana değil dosyaya yazar.
pip install --upgrade --target local_lib git+https://github.com/jaraco/path.git > install.log

# 4. Kurulum başarılıysa python programını çalıştır
if [ $? -eq 0 ]; then
    python3 my_program.py
else
    echo "Kurulum sırasında bir hata oluştu. install.log dosyasını kontrol edin."
fi