import os
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image

# Let's inspect export_individual_plots in FDA-RoLoRA
fda_dir = r"C:\Users\GKaralis\Documents\GitHub\FDA-RoLoRA"
sys.path.insert(0, fda_dir)
os.chdir(fda_dir)

import export_individual_plots as exp

print("Imported export_individual_plots successfully!")
print("Comm rates:", exp.comm_rates)
