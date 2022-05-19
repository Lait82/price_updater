import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from utils import *
import json
import os

excel_info_to_json()
convert_all_images_to_png()

json_data = []
with open('data.json', 'r') as jf: #jf = json file
    json_data = json.load(jf)

for barcode in json_data:
    element = json_data[barcode]

    # Crea un nuevo nombre para la imagen
    new_image_name = element['imagen'] + '_precioactual' # No Extension
    
    # Opens the Image
    try:
        img = Image.open('./precios_actualizados/' + new_image_name + '.png')
    except:
        img = Image.open('./vanilla_images/' + element['imagen'] + '.png')

    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)

    # Custom font style and font size
    myFont = ImageFont.truetype('Arial.ttf', 35)

    # Add Text to an image
    I1.text((element['xCoord'], element['yCoord']), str(element['precioFinal']), font = myFont, fill=(0, 0, 0))

    
    # creates the folder where all updated prices will be stored
    new_folder_path = os.path.dirname(os.path.abspath(__file__)) + "/precios_actualizados"
    os.makedirs(new_folder_path, exist_ok=True)


    # Save the edited image
    img.save(new_folder_path + "/" + new_image_name + '.png')

