# Obsidian One: a 75% hotswappable mechanical keyboard

## Overview

The PCB uses MX-style switches with PCB mounting and hotswap. The MCU(microcontroller - the device that tells the computer whenever you press a key) is a basic [Pi Pico RP2040/RP2350](https://www.canakit.com/raspberry-pi-pico.html).

## Why I made it

My current keyboard(Keychron K6 from #pyramid-scheme) has no function key row, and requires an uncomfortable combo to pause music. To fix this, I made Obsidian One which has the extra row.

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

The case is available at ./case

## BOM

| Quantity | Item                                | Notes/Details                                                      | Source                                                                                                            |
|----------|-------------------------------------|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| 84x      | Kailh Hotswap Sockets               |                                                                    | https://www.aliexpress.us/item/3256804104247622.html?gatewayAdapt=glo2usa                                     |
| 84x      | MX-compatible switches              | MMD Princess Tactile 48gs                                          | Amazon - https://www.amazon.com/KPREPUBLIC-Princess-Tactile-Mechanical-Keyboard/dp/B0C533FYXJ?sr=8-1                                       |
| 84x      | Compatible keycaps                  |                                                                    | [Amazon](https://www.amazon.com/dagaladoo-keycaps-Topographic-Percent-Keyboard/dp/B0CH2KSD7J?sr=8-68&xpid=GHBM-RxRzepH2)              |
| 84x      | 1N4148 THT Diodes                   |                                                                    | https://www.aliexpress.us/item/2255800939822415.html?gatewayAdapt=glo2usa          |
| 2x 2u, 1x 6.25u        | Stabilizers                         | Cherry-style                                                       | [CannonKeys](https://cannonkeys.com/products/cherry-stabilizers?variant=32257338998895)                          |
| 1x       | Orpheus Pico              | Controller board                                                   | Hack Club HQ |
| 1x       | Case                                | 3D-printed or purchased enclosure                                  | JLCPCB/#printing-legion                                                  |
| 1x       | PCB                                 | Custom-designed for this project                                   | JLCPCB                |

### Extra stuff for the BOM:

- Solder

- Soldering Iron

- Flux as needed

## Pictures: 

![CleanShot 2025-06-04 at 22 17 38](https://github.com/user-attachments/assets/72a44a06-bb19-4e4e-8e8f-baa5e49b8e10)

![CleanShot 2025-05-09 at 12 09 41@2x](https://github.com/user-attachments/assets/3ef68584-e08d-402d-ac58-158367805725)

![CleanShot 2025-05-09 at 12 36 32@2x](https://github.com/user-attachments/assets/57a26122-066b-44c1-a627-2b79cfe6c3df)

![CleanShot 2025-05-09 at 12 40 01@2x](https://github.com/user-attachments/assets/7d620331-e11d-4e52-937d-cab2aa38883d)

<img width="972" height="622" alt="CleanShot 2025-10-25 at 07 35 13@2x" src="https://github.com/user-attachments/assets/f0c58196-43b6-4aa8-938e-9deae82a6225" />



