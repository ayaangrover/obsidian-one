## Overview

The PCB uses MX-style switches with PCB mounting and hotswap.

## PCB

The PCB is in the /keyboard folder. Inside is the production folder, which includes the gerber file.

## Firmware

The firmware was made with QMK Configurator. It made a .hex file and I used microsoft's uf2conv.py and uf2families.json to convert it to a .uf2 file, which can be flashed to the MCU.

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
