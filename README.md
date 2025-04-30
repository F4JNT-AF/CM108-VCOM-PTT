# [EN]
## Why/how?
Older ham radio software do not support a PTT activated by one of the GPIO pin of a CM108 chip (MMSSTV, which I love, is such an example).
This Python script listens to a serial port and pulls a CM108's GPIO3 pin high when the serial port's CTS (Clear to Send) is asserted, and low when it's cleared.

## You'll need:
1) A virtual serial port. I'm using Free Virtual Serial Ports on Windows (https://freevirtualserialports.com/)
2) hidapi library for Python (https://github.com/trezor/cython-hidapi/)
Note: Even if I use Windows, this should work on Linux and MacOS.

## How to use
1) On your TX software, set the TX serial PTT on the first port of the virtual COM port pair.
2) In the Python script, set:
   a) The COM port to the other port of the virtual COM port pair.
   b) Delay. I've found to 10 ms to be an acceptable compromise for PTT purposes.
3) Launch the Python script.
4) You can now use your TX software normally.

## Limitations/Issues
- On some older CM1xx chips, you may need to modify the PID to 0x013A.

73, F4JNT


# [FR]
## Pourquoi/Comment?
Les logiciels radioamateurs anciens ne prennent pas en charge les PTT activés à partir d'une broche GPIO d'une puce CM108 (par exemple, MMSSTV que j'aime beaucoup).
Ce script Python écoute un port série et met la broche GPIO3 d'un CM108 à l'état haut quand un signal CTS est reçu, à l'état bas lorsque il est arrêté.

## Vous aurez besoin:
1) D'un port série virtuel. J'utilise Free Virtual Serial Ports sur Windows (https://freevirtualserialports.com/)
2) De la bibliothéque hidapi pour Python (https://github.com/trezor/cython-hidapi/)
Note: Même si j'utilise Windows, cela devrait marcher sur Linux et MacOS.

## Comment s'en servir
1) Sur votre logiciel TX, paramétrez le PTT série sur le premier port de la paire de ports virtuels.
2) Dans le script Python paramétrer:
   a) Le port COM afin d'utiliser le second port série de la paire de ports virtuels.
   b) Le délai. 10 ms me semble être un compromis acceptable pour du PTT.
3) Lancer le script Python.
4) Vous pouvez désormais utiliser votre logiciel TX comme d'habitude.

## Limitations/Soucis
- Sur certaines puces CM1xx plus vieilles, il peut être nécessaire de modifier le PID à 0x013A.

73, F4JNT


