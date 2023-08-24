from rembg import remove
from PIL import Image

input_patch = 'photo_2022-11-29_22-05-17.jpg'
output_patch = 'img_output.png'

open_image = Image.open(input_patch)
output = remove(open_image)

output.save(output_patch)