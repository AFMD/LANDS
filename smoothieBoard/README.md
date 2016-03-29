Here are links to the smoothieboard firmware and config files currently in use.

Folders here correspond to commit hashes for https://github.com/Smoothieware/Smoothieware

*.bin = firmware bin file  
*.txt = my modified config file  
*.orig = unmodified config file  
*.diff = diff between my .txt and their .orig config (`diff -Naur config.orig config.txt > config.diff`)

To bring a new *.orig (say from 7edfb34) up-to-date with my changes (say from fc8cfc6):
```
cd 7edfb34
HASH_DIR=fc8cfc6 patch -uN -o config.txt config.orig  ../$HASH_DIR/config.diff
```
