from PIL import Image
import numpy as np

im = Image.open('thesis/figures/17_MNLI_C20_R50_LR0.1_A0.5_all6_telemetry_stacked.png')
w, h = im.size

# The 6 subplots in a 3x2 grid:
# row 0: y from 0 to h/3
# row 1: y from h/3 to 2*h/3
# row 2: y from 2*h/3 to h
# col 0: x from 0 to w/2
# col 1: x from w/2 to w

panels = [
    ("1_accuracy", (0, 0, w//2, h//3)),
    ("4_accuracy_vs_cost", (w//2, 0, w, h//3)),
    ("2_allocated_epochs", (0, h//3, w//2, 2*h//3)),
    ("5_fda_threshold", (w//2, h//3, w, 2*h//3)),
    ("3_client_variance", (0, 2*h//3, w//2, h)),
    ("6_variance_vs_epoch", (w//2, 2*h//3, w, h)),
]

import os
os.makedirs('scratch/test_crop_17', exist_ok=True)
for name, bbox in panels:
    crop_im = im.crop(bbox)
    crop_im.save(f'scratch/test_crop_17/17_MNLI_C20_R50_LR0.1_A0.5_{name}.png')
print("Cropped panels saved to scratch/test_crop_17")
