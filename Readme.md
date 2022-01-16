# SimpleSudo - sudo but worse and for windows
Check bottom 
## How?

Install it:
```
npm install -g https://github.com/inkrnt/sudo.git
```
or install the zip and then and add the bin to PATH
```
PATH = %PATH%; (dir of the package)\bin
```
Use it:
```
sudo wt
```
or
```
sudo cmd
```
or just use 
```
sudo
```
this was insprired by https://github.com/tehsenaus/windosu
right now its really simple but i will work more on it later feel free to contribute what you think is best.
i will also try to write this in rust or c for it to be faster.
## Update _logs
added `sudo nano <file>`\
this only accepts txt files for now and any thing else will be ignored.\
for example, `sudo nano c:\coding_files\test.py`\
will return
`file test.py.txt does not exist, do you want make a new one?`

if this appears
```
C:\Users\Imran>npm install -g https://github.com/inkrnt/sudo.git
npm ERR! code ENOENT
npm ERR! syscall spawn git
npm ERR! path git
npm ERR! errno -4058
npm ERR! enoent An unknown git error occurred
npm ERR! enoent This is related to npm not being able to find a file.
npm ERR! enoent

npm ERR! A complete log of this run can be found in:
npm ERR!     C:\Users\Imran\AppData\Local\npm-cache\_logs\2022-01-13T04_43_27_086Z-debug-0.log
```
then download and zip and extract somewhere safe documents for example and run this command 
```
npm install -g (dir of package)
```