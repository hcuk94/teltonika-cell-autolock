import os
import config
from time import sleep

# Get current cell info
current_cell_cmd = os.popen('gsmctl -K')
current_cell_data_string = current_cell_cmd.read()

# Put cell info string into a list
current_cell_data_list = current_cell_data_string.split(",")
current_earfcn = int(current_cell_data_list[8])
current_pcid = int(current_cell_data_list[7])

# Get desired cell info
desired_earfcn = config.cell_earfcn
desired_pcid = config.cell_pcid

# Compare earfcn/pcid
if current_pcid == desired_pcid and current_earfcn == desired_earfcn:
    # earfcn/pcid matches, log this and take no further action
    print("Current EARFCN/PCID values of {}/{} match desired values of {}/{}. No further action will be taken."
          .format(current_earfcn, current_pcid, desired_earfcn, desired_pcid))
else:
    # earfcn/pcid does not match, so lets run the sequence to lock cell
    print("Current EARFCN/PCID values of {}/{} do not match desired values of {}/{}. Cell lock sequence will be run..."
          .format(current_earfcn, current_pcid, desired_earfcn, desired_pcid))
    mode_override_cmd = "gsmctl -A 'AT+QCFG=\"NWSCANMODE\",3,1'"
    mode_override_cmd_run = os.popen(mode_override_cmd)
    print("Mode Override: " + mode_override_cmd_run.read())
    sleep(1)
    cell_lock_cmd = "gsmctl -A 'AT+QNWLOCK=\"common/lte\",2,{},{}'".format(desired_earfcn, desired_pcid)
    cell_lock_cmd_run = os.popen(cell_lock_cmd)
    print("Cell Lock: " + cell_lock_cmd_run.read())
    print("Cell lock sequence complete.")
