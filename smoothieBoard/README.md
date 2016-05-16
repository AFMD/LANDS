Here are links to the smoothieboard firmware and config files currently in use.

Folders here correspond to commit hashes for https://github.com/Smoothieware/Smoothieware

*.bin = firmware bin file  
*.txt = my modified config file  
*.orig = unmodified config file  
*.diff = diff between my .txt and their .orig config (`diff -Naur config.orig config.txt > config.diff`)

To bring a new *.orig (say from 7edfb34) up-to-date with my changes (say from fc8cfc6):
```
cd 7edfb34
patch -uN -o config.txt config.orig  ../fc8cfc6/config.diff
```


# Compiling the firmware
This builds the `edge` branch of the upstream firmware project (under Arch):
```
git clone https://github.com/Smoothieware/Smoothieware.git
cd Smoothieware
git checkout edge
sudo pacman -S 	arm-none-eabi-gcc arm-none-eabi-newlib
make clean
make all
```
Now the firmware bin is here: ../LPC1768/main.bin  
Rename that to firmware.bin and put it on the root of the smoothieboard's sd card and reboot it to flash the new firmware.
There's an incompatibility with the very latest GCC here, for now downgrade arm-none-eabi-gcc (6.1.1-1 => 5.3.0-1) and arm-none-eabi-newlib (2.4.0-2 => 2.4.0-1) so that this builds
