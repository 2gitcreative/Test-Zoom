from PIL import Image
import os

for file in os.listdir('.'):
    if file.endswith('.jpg'):
        img = Image.open(file)
        print(f"{file}: {img.width}x{img.height}")
