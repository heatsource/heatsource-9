"""DO NOT DELETE THIS FILE. This script imports the heatsource module
and executes the model routines. This script must be located in the same
directory as HeatSource_control.csv. NOTE that executing this script
from Python shell (IDLE) will not identify __file__ correctly and will
result in an error. It must be executed from a command prompt. Your
options are to double click on this file and execute using python.exe,
use the batch command files (which point to these files), or
open terminal and execture manually by typing:
python -i path/to/this/script/HS9_Setup_Control_File.py"""

from heatsource9 import BigRedButton
from os.path import dirname, exists, join, realpath, abspath

def getScriptPath():
    """Gets the path to the directory where the script is being executed from."""
    return abspath(join(dirname(realpath(__file__)), '.'))

inputdir = getScriptPath() + '/'
control_file = 'HeatSource_Control.csv'

if exists(join(inputdir,control_file)) is True:
    raise Exception("HeatSource_Control.csv already exists.")

# Run control setup, run_type = 4
BigRedButton.run_cf_setup(inputdir, control_file)

