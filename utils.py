from cmath import e
import magic
import pandas
import json
import os
from PIL import Image
import shutil

# this returns a json 
def excel_file_to_json(excel_file, sheet='Hoja 1', orient='records'):
    #converts from excel db to json (define orientation of document in this case from up to down)
    try:
        excel = pandas.read_excel(excel_file, sheet).to_json(orient=orient)
    except:
        excel = pandas.read_excel(excel_file, sheet_name='Sheet1').to_json(orient=orient)
    return json.loads(excel)


def excel_info_to_json():
    shutil.rmtree(os.path.dirname(os.path.realpath(__file__)) + '/precios_actualizados')
    os.remove(os.path.dirname(os.path.realpath(__file__)) + '/data.json')
    input('asdfasdf')
    database_json = excel_file_to_json(excel_file='data.xlsx')
    # database_json = excel_file_to_json(excel_file='data.xlsx')
    print(database_json)
    new_prices_json = excel_file_to_json(excel_file='precios_nuevos.xlsx')


    # crea o en su defecto actualiza la base de datos
    merged_json = {}   
    
    for itemInfo in database_json:
        barcode = itemInfo['codigoDeBarras']
        del itemInfo['codigoDeBarras']

        merged_json[barcode] = itemInfo

        print(merged_json[barcode])

        merged_json[barcode]['xCoord'] = merged_json[barcode]['xCoord'] or 0
        merged_json[barcode]['yCoord'] = merged_json[barcode]['yCoord'] or 0

    # le agrega los precios nuevos al json de la base de datos
    for new_price in new_prices_json:
        if(new_price['codigoDeBarras'] in merged_json):
            merged_json[new_price['codigoDeBarras']]['precioFinal'] = new_price['precioFinal']
            print(new_price['nombre'] + ' agregado correctamente','\n')
        else:
            print(
                'el producto ', new_price['nombre'],
                ' con codigo: ', new_price['codigoDeBarras'], 
                ' no existe en la base de datos\n'
            )



    string_database = pandas.DataFrame(merged_json).to_json()
    
    # Print out the result
    # print('Excel Sheet to JSON:\n', string_database)

    # Make the string into a list to be able to input in to a JSON-file
    database_json_file = json.loads(string_database)



    # Define file to write to and 'w' for write option -> json.dump() 
    # defining the list to write from and file to write to
    with open('data.json', 'w') as json_file:
        json.dump(database_json_file, json_file)


def convert_all_images_to_png():

    # Gets only files present in a path.
    vanilla_images_files = os.listdir(path=os.path.dirname(os.path.realpath(__file__)) + '/vanilla_images')
    
    for image_file in vanilla_images_files:
        
        mime = magic.Magic(mime=True)
        
        #Full path with ext(if it hasnt any full path + filename)
        path_file_ext = os.path.dirname(os.path.realpath(__file__)) + '/vanilla_images/' + image_file
        
        ## Full path to the image + filename ONLY
        path_file = path_file_ext.split('.')[0]

        extension = mime.from_file(path_file_ext).split('/')[-1]

        if(extension != 'png'):
            try:
                im1 = Image.open(path_file_ext)
                im1.save(path_file + '.png')
                os.remove(path_file_ext)
            except e:
                print(e)
