#Description

This program facilitates a basic radio link between two USRB B205 Mini SDRs.

The GNURadio receiver program reads power from the radio using libUHD and outputs it to a ZeroMQ socket.

This is part of a larger project which uses the radio signal strength to optimize drone position in a self-forming aerial network.



#Setup Instructions

```
sudo apt install gnuradio libuhd-dev

sudo /usr/lib/uhd/utils/uhd_images_downloader.py

export UHD_IMAGES_DIR=/usr/share/uhd/images

uhd_find_devices
```

Copy the serial ID

```
gnuradio-companion
```

Open the *.grc flowgraph file from this repository (one for each radio)

Paste the serial ID into the USRP block

Press play to run the flowgraph

