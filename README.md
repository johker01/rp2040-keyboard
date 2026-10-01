# rp2040-keyboard

A USB HID keyboard sending the key F13 when GPIO 0 is pulled down.

photobooth2 maps F13 to a capture and records it as coming from this buzzer. The Bluetooth buzzer ([photobooth-buzzer](https://github.com/johker01/photobooth-buzzer)) sends F14, and `c` stays the operator's keyboard key.

## Prerequisites
* [CircuitPython](https://circuitpython.org/) installed on the RP2040
* [adafruit_hid](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/) library

## References

Based on
* https://learn.adafruit.com/diy-pico-mechanical-keyboard-with-fritzing-circuitpython/code-the-pico-keyboard
* https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/Pico_RP2040_Mech_Keyboard/code.py
* https://www.heise.de/tests/Ausprobiert-Raspberry-Pico-mit-USB-HID-als-Tastatur-oder-Maus-benutzen-6011697.html
