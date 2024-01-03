from PIL import Image

for i in range(4, 16):
    im = Image.open(f'helmet_classify_img/picture{i}.jpg')
    width, height = im.size
    original_name = f"picture{i}"
    top = 0
    bottom = height

    # 1 quarter
    for quart in range(1, 5):
        new_name = original_name + str(quart)
        left = (width / 4) * (quart - 1)
        right = (width / 4) * quart
        img_quart = im.crop((left, top, right, bottom))
        img_quart.save(f'helmet_classify_img/{new_name}.jpg')


