## Overview

The PCB uses MX-style switches with PCB mounting and hotswap. The MCU(microcontroller - the device that tells the computer whenever you press a key) is a basic [Pi Pico RP2040/RP2350](https://www.canakit.com/raspberry-pi-pico.html).

## PCB

The PCB is in the /keyboard folder. Inside is the production folder, which includes the gerber file.

## Firmware

### KMK

In the /firmware/kmk folder, you'll find a CIRCUITPY folder showing exactly what your MCU should look like when you plug it in. First, flash micropython. You can find instructions on how to do that [here](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html). Then, eject, unplug, and reconnect the MCU. Once you're done, it should appear as a usb drive named CIRCUITPY. Now, replace the contents of the drive/mcu with the items in the /firmware/kmk/CIRCUITPY directory. Upon restarting(unplugging + reconnecting) the MCU, it should be functioning properly.

NOTE: This KMK firmware hasn't been tested. Flashing it to your microcontroller may cause damage or render it incapable of function. Use it at your own risk.

### QMK

The QMK firmware was made with QMK Configurator. It made a .hex file and I used microsoft's uf2conv.py and uf2families.json to convert it to a .uf2 file, which can be flashed to the MCU. You can see it at /firmware/qmk.

NOTE: This QMK firmware hasn't been tested. Flashing it to your microcontroller may cause damage or render it incapable of function. Use it at your own risk.

## Case

The case isn't designed yet.

## BOM

- 84x Kailh Hotswap Sockets

- 84x MX-compatible switches

- 84x Compatible keycaps

- 84x 1N4148 THT Diodes

- 1x Orpheus Pico/Pi Pico

- 1x USB C to USB A/USB C to USB C cable

### Extra stuff for the BOM:

- Solder

- Soldering Iron

- Flux as needed