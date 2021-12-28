# ###################################
# Teltonika Cell Autolock Script
# ###################################

# To use, firstly configure your cell earfcn and pcid values below:
cell_earfcn = 1392
cell_pcid = 365
# Then, add a cron job to run main.py (e.g. hourly).
# For full install instructions, see README.md
# Additional configurable options are shown below.

log_file = '/root/teltonika-cell-autolock/main.log'  # File to log to
log_level = 20  # 0 NOTSET, 10 DEBUG, 20 INFO, 30 WARNING, 40 ERROR, 50 CRITICAL