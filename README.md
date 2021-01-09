# PyFrame

In my tests I ran this on a Raspberry Pi Zero W with a WaveShare IT8951 driver board and a 6-inch e-Paper display (4-bit greyscale; 800x600 px). I used raspian lite as an os.

Make sure that SPI is enabled in `raspi-config`.

### Required Python libraries

IT8951 driver library for Python by GregDMeyer (all creds to him):
```
https://github.com/GregDMeyer/IT8951
```

Common libraries
```
pip3 install RPi.GPIO
pip3 install pillow
pip3 install flask

sudo apt-get install libopenjp2-7
sudo apt install libtiff5
```

### How to run
1. Run `sudo python3 epaper_api.py` to enable web api.
2. Access your Pi via hostname or IP address in a browser
3. Upload a file

You can also upload an image file via posting a form in an http-request (`POST http://[IP address]/upload`).
