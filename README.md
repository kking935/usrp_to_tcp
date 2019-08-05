# Description

This program facilitates a basic radio link between two USRB B205 Mini SDRs.

The GNURadio receiver program reads power from the radio using libUHD and outputs it to a ZeroMQ socket.

This is part of a larger project which uses the radio signal strength to optimize drone position in a self-forming aerial network.



# Setup Instructions

```
sudo apt install gnuradio libuhd-dev

sudo /usr/lib/uhd/utils/uhd_images_downloader.py

export UHD_IMAGES_DIR=/usr/share/uhd/images

gnuradio-companion
```

Within the GNU Radio Companion, open the *.grc flowgraph files from this repository

In a seperate terminal, run
```
uhd_find_devices
```
to find the serial IDs of all the usrps connected to this device

Copy the desired IDs and paste each into the usrp_ID variable block of their respective *.grc flowgraph files

In the usrp_tx_from_gaussian flowgraph file, press the green play button to start trasmitting gaussian noise.

Finally, in the usrp_rx_to_power flowgraph file, press the green play button to begin receiving the signal and outputting its power to a ZeroMQ socket.
