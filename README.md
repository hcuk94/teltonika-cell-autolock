# teltonika-cell-autolock

Script designed to be run on a Teltonika RUT360, to monitor the reported Cell ID and apply cell locking rules if it is pertinent to do so.

Please read the important information on this readme before using this script in your own setup.

### Important
This script was created for my own personal Teltonika device.
It is designed specifically for the RUT360 model and is untested on other models. Indeed, it should be considered altogether untested, and for use at your own risk.

I know for a fact that other models use different commands so please do your research before using this!

If you are using a RUT360, I still suggest you familiarise yourself with cell locking before using this script. Teltonika have kindly provided some guidance on cell locking here: https://community.teltonika-networks.com/38696/rut360-cell-lock?show=38739#c38739

### Installation
Firstly you will need to SSH to your Teltonika device, and install Python:

`opkg update`

`opkg install python-light`

I then created a directory for the script, and downloaded the raw files from github:
````
mkdir teltonika-cell-autolock
cd teltonika-cell-autolock
wget https://raw.githubusercontent.com/hcuk94/teltonika-cell-autolock/main/config.py
wget https://raw.githubusercontent.com/hcuk94/teltonika-cell-autolock/main/main.py
````

The better option would be to `opkg install git` and clone the repository, but my device did not have sufficient storage space to do so.

Next, it is important to edit the cell_earfcn and cell_pcid values in config.py

If you do not know what these are, then you should first familiarise yourself with cell locking on this device, and work out which cell is best for you.
The following instructions were kindly provided to me by Teltonika and should help:
https://community.teltonika-networks.com/38696/rut360-cell-lock?show=38739#c38739

Finally, install main.py into your crontab. I went for an hourly schedule:

`0 * * * * /root/teltonika-cell-autolock/main.py`

### Background
My parents live in rural Suffolk (UK), where ADSL2+ provides speeds of around 2mbps. Since 2017 I have instead used a 4G connection, which can give them speeds of around 60mbps.

However, to achieve these speeds I must use a mast which is a little further away, but with good speeds (60mbps from the house, 150mbps when nearby with my iPhone). 
The mast which is geographically closest has a pretty average uplink (presumably on the same exchange as the DSL), and only gets around 9mbps.

Using a Teltonika RUT340 with cell locking, I am able to force the device to use the farther cell, thus significantly improving internet speeds.

Cell locking is not permanent though, so I wrote this script to run on cron and re-set the lock if applicable.
