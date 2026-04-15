from evdev import list_devices, InputDevice, ecodes
import os

devices = [InputDevice(path) for path in list_devices()]
dev = None
for d in devices:
    if 'MX Master 2S' in d.name:
        dev = d
        break

if not dev:
    exit(1)

def move_window():
    # qdbus yerine qdbus6 kullanarak KDE Plasma 6 uyumluluğu sağlıyoruz
    os.system('qdbus6 org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut "Window to Next Screen"')

for event in dev.read_loop():
    if event.type == ecodes.EV_KEY and event.code == 276:
        if event.value == 1: # Sadece basildiginda tetikle
            move_window()