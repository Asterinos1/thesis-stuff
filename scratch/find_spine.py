from PIL import Image
import numpy as np

im = Image.open('scratch/test_crop_17/17_MNLI_C20_R50_LR0.1_A0.5_1_accuracy.png')
arr = np.array(im)

# The top spine is a black line near y=60-80
# Let's inspect rows around y=40 to 100
for y in range(40, 110):
    row = arr[y, :, :3]
    black_pixels = np.sum(np.all(row < 50, axis=-1))
    if black_pixels > 500:
        print(f'Top spine found at y={y} with {black_pixels} black pixels')
