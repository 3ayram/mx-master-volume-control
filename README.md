# MX Master 2S Side Wheel Volume Control

Linux üzerinde Logitech MX Master 2S farenin yan tekerleğini (thumb wheel) sistem ses seviyesi kontrolü için eşleyen Python tabanlı bir otomasyon servisidir.

## Özellikler
- **evdev** kütüphanesi ile düşük gecikmeli (low-latency) donanım erişimi.
- **Systemd** servisi sayesinde arka planda kesintisiz çalışma.
- Otomatik cihaz algılama (Cihaz adı üzerinden dinamik eşleşme).
- Özelleştirilebilir hassasiyet (\`THRESHOLD\`) ve ses değişim adımları.

## Kurulum

### 1. Bağımlılıklar
Sistemine gerekli paketleri yükle (Arch/CachyOS):
\`\`\`bash
sudo pacman -S python-evdev libpulse
\`\`\`

### 2. Dosya Yapısı
Scriptin bulunacağı dizini oluştur ve dosyayı yerleştir:
\`\`\`bash
mkdir -p ~/scripts
# mouse_volume.py dosyasını bu klasöre koyun.
\`\`\`

### 3. Systemd Servisi Oluşturma
\`/etc/systemd/system/mouse-volume.service\` yoluna aşağıdaki içeriği kaydedin:

\`\`\`ini
[Unit]
Description=MX Master 2S Volume Control
After=network.target

[Service]
Type=simple
Environment=PULSE_SERVER=unix:/run/user/1000/pulse/native
ExecStart=/usr/bin/python3 /home/bayram/scripts/mouse_volume.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
\`\`\`

### 4. Servisi Aktifleştir
\`\`\`bash
sudo systemctl daemon-reload
sudo systemctl enable --now mouse-volume.service
\`\`\`

## Kullanım ve İnce Ayarlar
\`mouse_volume.py\` dosyasındaki şu değişkenlerle oynayarak deneyimi kişiselleştirebilirsiniz:
- \`THRESHOLD = 10\`: Değer düştükçe tekerlek daha hassas olur.
- \`+7% / -7%\`: Her tıkta değişecek ses yüzdesi.

## Lisans
MIT