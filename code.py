# SPDX-FileCopyrightText: 2021 John Park for Adafruit Industries
# SPDX-License-Identifier: MIT
# RaspberryPi Pico RP2040 Mechanical Keyboard (single-key macro pad)

import time

import board
import keypad
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction

print("---Pico Pad Keyboard---")

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = False  # lights up while the key is held, for press feedback

kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

KEY = 1
MEDIA = 2

# What the single key does. Swap ACTION_TYPE/ACTION_CODE to change it,
# e.g. ACTION_TYPE = MEDIA; ACTION_CODE = ConsumerControlCode.MUTE
# F13 is a key nobody types, so photobooth2 can tell this buzzer apart from a
# real keyboard's `c` and from the Bluetooth buzzer (F14).
ACTION_TYPE = KEY
ACTION_CODE = Keycode.F13

# GP15 is skipped on the Pico because it's funky; the switch lives on GP0.
key = keypad.Keys((board.GP0,), value_when_pressed=False, pull=True)

while True:
    event = key.events.get()
    if event is not None:
        led.value = event.pressed

        if event.pressed:
            try:
                if ACTION_TYPE == KEY:
                    kbd.press(ACTION_CODE)
                else:
                    cc.send(ACTION_CODE)
            except ValueError as e:  # six-key rollover limit
                print("HID report full:", e)
        else:
            if ACTION_TYPE == KEY:
                try:
                    kbd.release(ACTION_CODE)
                except ValueError as e:
                    print("release failed:", e)

    time.sleep(0.01)
