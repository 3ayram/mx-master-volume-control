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

THRESHOLD = 10
accum = 0

for event in dev.read_loop():
    if event.type == ecodes.EV_REL and event.code == 12:
        accum += event.value
        if accum >= THRESHOLD:
            os.system('pactl --server unix:/run/user/1000/pulse/native set-sink-volume @DEFAULT_SINK@ -7%')
            accum = 0
        elif accum <= -THRESHOLD:
            os.system('pactl --server unix:/run/user/1000/pulse/native set-sink-volume @DEFAULT_SINK@ +7%')
            accum = 0