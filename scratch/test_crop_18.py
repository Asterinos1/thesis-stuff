from PIL import Image
import numpy as np
import os

im18 = Image.open('thesis/figures/18_QNLI_C20_R50_LR0.1_A0.5_all6_telemetry_stacked.png')
w, h = im18.size

panels = [
    ("1_accuracy", (0, 0, w//2, h//3)),
    ("4_accuracy_vs_cost", (w//2, 0, w, h//3)),
    ("2_allocated_epochs", (0, h//3, w//2, 2*h//3)),
    ("5_fda_threshold", (w//2, h//3, w, 2*h//3)),
    ("3_client_variance", (0, 2*h//3, w//2, h)),
    ("6_variance_vs_epoch", (w//2, 2*h//3, w, h)),
]

os.makedirs('scratch/test_crop_18', exist_ok=True)
for name, bbox in panels:
    crop_im = im18.crop(bbox)
    # find top spine black line
    arr = np.array(crop_im)
    top_y = 55
    for y in range(40, 110):
        row = arr[y, :, :3]
        black_pixels = np.sum(np.all(row < 50, axis=-1))
        if black_pixels > 500:
            top_y = max(0, y - 8)
            break
    cw, ch = crop_im.size
    final_im = crop_im.crop((0, top_y, cw, ch))
    final_im.save(f'scratch/test_crop_18/18_QNLI_C20_R50_LR0.1_A0.5_{name}.png')

print("Cropped 18 panels successfully!")
