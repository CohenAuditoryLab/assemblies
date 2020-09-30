import os
import scipy.io
from find_triggers import find_triggers

# Function to load the triggers
def load_triggers(path,dmr):
    #prefixed = [filename for filename in os.listdir(path) if filename.startswith("AudiResp")]
    path_triggers_dir= 'I:\Parooa\Synapse\i\kiloSorted_DMR\Triggers'
    filename=find_triggers(path_triggers_dir,path)
    if os.path.exists(filename):
        trig = scipy.io.loadmat(filename)
        if dmr==1:
            return trig['TrigA'][0],filename
        elif dmr==2:
            return trig['TrigB'][0],filename
    else:
        print("Sorry, this folder doesn't exist, try another one")
        return
