import os
from os import listdir
from PIL import Image

folder_dir = "helmet_classify_img"
for images_path in os.listdir(folder_dir):
    im = Image.open(f"helmet_classify_img/{images_path}")
    left_tilt_im = im.rotate(30)
    right_tilt_im = im.rotate(-30)
    origin_name = images_path.split('.')[0]
    left_tilt_im.save(f'helmet_classify_img/left_titl_{origin_name}.jpg')
    right_tilt_im.save(f'helmet_classify_img/right_titl_{origin_name}.jpg')