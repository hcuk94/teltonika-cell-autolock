# teltonika-cell-autolock

Script designed to be run on a Teltonika RUT360, to monitor the reported Cell ID and apply cell locking rules if it is pertinent to do so.

Please read the important information on this readme before using this script in your own setup.

### Important
This script was created for my own personal Teltonika device.
It is designed specifically for the RUT360 model and is untested on other Teltonika models. Indeed, it should be considered altogether untested, and for use at your own risk.

I know for a fact that other models use different commands so please do your research before using this!

If you are using a RUT360, I still suggest you familiarise yourself with cell locking before using this script. I have written about this on my blog [here](https://henrycole.uk/2021/12/28/Locking-the-Teltonika-RUT360-to-a-Specific-Cell.html).

### Installation
There is no persistent storage on the RUT360, and thus any files you store on the device are likely to be wiped if, for example, you upgrade the firmware.
I therefore recommend the following approach which should survive most routine maintenance:
#### 1. Fork this GitHub Repo into your own account
#### 2. Edit autolock.sh in your forked repo and change the following block to your desired EARFCN & PCID:
```
# Configuration - change these values!
DESIRED_EARFCN=1392
DESIRED_PCID=365
```
If you do not know your EARFCN/PCID values, please see my [blog post](https://henrycole.uk/2021/12/28/Locking-the-Teltonika-RUT360-to-a-Specific-Cell.html) on this.
#### 3. SSH to your Teltonika device, and use `crontab -e` to install the following:
```
0 * * * * wget -q https://raw.githubusercontent.com/hcuk94/teltonika-cell-autolock/main/autolock.sh -O /root/autolock.sh && chmod +x /root/autolock.sh && /root/autolock.sh >> /root/autolock.log 2>&1
```
You will need to change 'hcuk94' to your own GitHub username so that your chosen EARFCN/PCID values will be used. 
When connecting via SSH the username is root rather than admin.
#### 4. You may need to restart cron for the job to start running:
```
/etc/init.d/cron restart
```
The job will now run at the stroke of each hour, and you will be able to check its output in /root/autolock.log
The script will be downloaded from your repo each time, so if you need to change your cell you can update this in your repo.

### Feedback & Support
The best way to ask a question or leave feedback on this script is to raise an issue in this GitHub Repo.
You can also contact me directly using the links in my GitHub profile.
I look forward to hearing from you :-)

### Background
My parents live in rural Suffolk (UK), where ADSL2+ provides speeds of around 2mbps. Since 2017 I have instead used a 4G connection, which can give them speeds of around 60mbps.

However, to achieve these speeds I must use a mast which is a little further away, but with good speeds (60mbps from the house, 150mbps when nearby with my iPhone). 
The mast which is geographically closest has a pretty average uplink (presumably on the same exchange as the DSL), and only gets around 9mbps.

Using a Teltonika RUT340 with cell locking, I am able to force the device to use the farther cell, thus significantly improving internet speeds.

Cell locking is not permanent though, so I wrote this script to run on cron and re-set the lock if applicable.

I've written some more about delivering broadband over 4G in these blog posts:
- [Delivering Rural Broadband over 4G](https://henrycole.uk/2021/12/02/Delivering-Rural-Broadband-over-4G.html)
- [Locking the Teltonika RUT360 to a Specific Cell ID](https://henrycole.uk/2021/12/28/Locking-the-Teltonika-RUT360-to-a-Specific-Cell.html)
