#!/usr/bin/env ash                                                                                                                                                                                          
##################                                                                                                                                                                                          
# A Shell Script to lock the Teltonika RUT360 LTE Modem to a specified cell                                                                                                                                 
# Henry Cole - henrycole.uk                                                                                                                                                                                 
##################                                                                                                                                                                                          
                                                                                                                                                                                                            
# Configuration - change these values!                                                                                                                                                                      
DESIRED_EARFCN=1392
DESIRED_PCID=281
                    
##################
# Logging Function
##################
logger() {
    log_date=$(date +'%F %R')
    echo "$log_date - $1"
}

##################                                                                                                                                                                                          
# Main Program                                                                                                                                                                                              
##################                                                                                                                                                                                          

# Get currently connected cell, and determine current earfcn/pcid                                                                                                                                         
current_cell=`gsmctl -A 'AT+QENG="servingcell"'`                                                                                                                                                                                    
current_cell_data_list=$(echo $current_cell | tr "," "\n")                                                                                                                                                  
                                                                                                                                                                                                            
current_earfcn=`echo -e "$current_cell_data_list" | sed -n '9p'`                                                                                                                                            
current_pcid=`echo -e "$current_cell_data_list" | sed -n '8p'`                                                                                                                                              
                                                                                                                                                                                                            
                                                                                                                                                                                                            
# Check Match                                                                                                                                                                                               
if [[ $current_earfcn == $DESIRED_EARFCN && $current_pcid == $DESIRED_PCID ]]; then                                       
    logger "Current EARFCN/PCID of $current_earfcn/$current_pcid match desired $DESIRED_EARFCN/$DESIRED_PCID. No action will be taken."
else                                                                                                                                                                                                     
    logger "$run_dateiCurrent EARFCN/PCID of $current_earfcn/$current_pcid do not match desired $DESIRED_EARFCN/$DESIRED_PCID. Running cell lock sequence..."                      
                                                                                                                                                                                                            
    # Main Cell Locking Sequence                                                                                                                                                                            
    force_scanmode=`gsmctl -A 'AT+QCFG="NWSCANMODE",3,1'`                                                                                                                                                   
    if [[ $force_scanmode == *"OK"* ]]; then                                                                                                                                                                
        lock_cell=$(gsmctl -A 'AT+QNWLOCK="common/lte",2,'$DESIRED_EARFCN','$DESIRED_PCID'')                                                                                                                  
        if [[ $lock_cell == *"OK"* ]]; then                                                                                                                                                                 
            logger "Cell lock completed successfully"                                                                                                                                                         
        else                                                                                                                                                                                                
            logger "An error was encountered while locking the cell"                                                                                                                                          
        fi                                                                                                                                                                                                  
    else                                                                                                                                                                                                    
        logger "An error was encountered while setting the scanmode to LTE only"                                                                                                                              
    fi                                                                                                                                                                                                      
fi
