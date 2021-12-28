import os
import config
import logging
from time import sleep

# Configure logging using config file
 logging.basicConfig(level=config.log_level, filename=config.log_file
                     , filemode="a+", format="%(asctime)-15s %(levelname)-8s %(message)s")

# Get current cell info
logging.debug("Getting current cell info...")
current_cell_cmd = os.popen('gsmctl -K')
current_cell_data_string = current_cell_cmd.read()
logging.debug("Got cell info string: " + current_cell_data_string)

# Put cell info string into a list
logging.debug("Extracting cell info...")
current_cell_data_list = current_cell_data_string.split(",")
current_earfcn = int(current_cell_data_list[8])
current_pcid = int(current_cell_data_list[7])
logging.debug("Current EARCFN: " + str(current_earfcn))
logging.debug("Current PCID: " + str(current_pcid))

# Get desired cell info
desired_earfcn = config.cell_earfcn
desired_pcid = config.cell_pcid
logging.debug("Desired EARCFN: " + desired_earfcn)
logging.debug("Desired PCID: " + desired_pcid)

# Compare earfcn/pcid
if current_pcid == desired_pcid and current_earfcn == desired_earfcn:
    # earfcn/pcid matches, log this and take no further action
    logging.info("Current EARFCN/PCID values of {}/{} match desired values of {}/{}. No further action will be taken."
          .format(current_earfcn, current_pcid, desired_earfcn, desired_pcid))
else:
    # earfcn/pcid does not match, so lets run the sequence to lock cell
    logging.info("Current EARFCN/PCID values of {}/{} do not match desired values of {}/{}. Cell lock sequence will be run..."
          .format(current_earfcn, current_pcid, desired_earfcn, desired_pcid))
    mode_override_cmd = "gsmctl -A 'AT+QCFG=\"NWSCANMODE\",3,1'"
    logging.debug("Running command: " + mode_override_cmd)
    mode_override_cmd_run = os.popen(mode_override_cmd)
    logging.debug("Output: " + mode_override_cmd_run.read())
    sleep(1)
    cell_lock_cmd = "gsmctl -A 'AT+QNWLOCK=\"common/lte\",2,{},{}'".format(desired_earfcn, desired_pcid)
    logging.debug("Running command: " + cell_lock_cmd)
    cell_lock_cmd_run = os.popen(cell_lock_cmd)
    logging.debug("Output: " + cell_lock_cmd_run.read())
    logging.info("Cell lock sequence complete.")
