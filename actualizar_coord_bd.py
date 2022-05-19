# importing the tkinter module and PIL
# that is pillow module
from csv import excel
from tkinter import *
from copy import deepcopy

import pandas

from utils import excel_file_to_json

event2canvas = lambda e, c: (c.canvasx(e.x), c.canvasy(e.y))

def forward(img_no):
    # GLobal variable so that we can have
    # access and change the variable
    # whenever needed
    global canvas
    global button_forward
    global button_back
    global button_exit
    global arr_data_keys
    global data_json
    # canvas.grid_forget()
    canvas.delete('all')

    image_no_index = img_no-1 if img_no-1 != len(List_images) else len(List_images)-1 # Only god knows why it works
    def printcoords(event):
        print('precio de '+ List_images[image_no_index]['nombre'] + " colocado en: (x: " + str(event.x) + ', y: ' + str(event.y) + ') \n\n')
        data_json[image_no_index]['xCoord'] = event.x
        data_json[image_no_index]['yCoord'] = event.y
        if img_no <= len(List_images):
            df = pandas.DataFrame(data_json)
            df.to_excel('fileTest.xlsx', index=False)

            forward(img_no+1)
        else:
            forward(img_no)
    #mouseclick event
    canvas.bind("<ButtonPress-1>",printcoords)



    # This is for clearing the screen so that
    # our next image can pop up
    print('IMG_NO===>', img_no)
    print('LIST_IMAGES===>', len(List_images))
    canvas.create_image(0,0,image=List_images[image_no_index]['imagen'],anchor="nw")
    input_text = 'clickea para colocar el precio de: ' + List_images[image_no_index]['nombre']
    print(input_text)

    # as the list starts from 0 so we are
    # subtracting one
    canvas.grid(row=1, column=0, columnspan=3)
    button_forward = Button(root, text="forward", command=lambda: forward(img_no+1))

    # img_no+1 as we want the next image to pop up
    if img_no == len(data_json):
        button_forward = Button(root, text="Forward", state=DISABLED)

    # img_no-1 as we want previous image when we click
    # back button
    button_back = Button(root, text="Back", command=lambda: back(image_no_index))

    # Placing the button in new grid
    button_back.grid(row=5, sticky=W)
    button_exit.grid(row=5, sticky=W, padx=200)
    button_forward.grid(row=5, sticky=W, padx=400)

def back(img_no):

    # We will have global variable to access these
    # variable and change whenever needed
    global canvas
    global button_forward
    global button_back
    global button_exit
    # for clearing the image for new image to pop up
    canvas.delete('all')
    # canvas.grid_forget()


    def printcoords(event):
        print('precio de '+ List_images[img_no-1]['nombre'] + " colocado en: (x: " + str(event.x) + ', y: ' + str(event.y) + ') \n\n')
        data_json[img_no-1]['xCoord'] = event.x
        data_json[img_no-1]['yCoord'] = event.y
        # print(data_json[List_images[img_no-1]['barcode']])
        if img_no < len(List_images):
            df = pandas.DataFrame(data_json)
            df.to_excel('fileTest.xlsx', index=False)
            forward(img_no+1)
        else:
            forward(img_no)
    #mouseclick event
    canvas.bind("<ButtonPress-1>",printcoords)




    canvas.create_image(0,0,image=List_images[img_no-1]['imagen'],anchor="nw")
    input_text = 'clickea para colocar el precio de: ' + List_images[img_no-1 if img_no < len(List_images)  else img_no-2]['nombre']
    print(input_text)
    
    canvas.grid(row=1, column=0, columnspan=3)
    button_forward = Button(root, text="forward", command=lambda: forward(img_no + 1))
    button_back = Button(root, text="Back", command=lambda: back(img_no-1))
    # print(img_no)

    # whenever the first image will be there we will
    # have the back button disabled
    if img_no == 1:
        button_back = Button(root, text="Back", state=DISABLED)

    canvas.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=5, sticky=W)
    button_exit.grid(row=5, sticky=W, padx=200)
    button_forward.grid(row=5, sticky=W, padx=400)


# Calling the Tk (The initial constructor of tkinter)
root = Tk()

# We will make the title of our app as Image Viewer
root.title("Image Viewer")

# The geometry of the box which will be displayed
# on the screen
root.geometry("1024x700")


frame = Frame(root)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
canvas = Canvas(frame, bd=0, height=650, width=1000)
canvas.grid(row=0, column=0)
frame.grid(row=1)


def printcoords(event):
    print('precio de '+ List_images[1-1]['nombre'] + " colocado en: (x: " + str(event.x) + ', y: ' + str(event.y) + ') \n\n')
    data_json[1-1]['xCoord'] = event.x
    data_json[1-1]['yCoord'] = event.y
    
    df = pandas.DataFrame(data_json).T
    df.to_excel('fileTest.xlsx', index=False)
    
    forward(1+1)
#mouseclick event
canvas.bind("<ButtonPress-1>",printcoords)








# List of the images so that we traverse the list
List_images = []

# Load data.json to start opening files
data_json = excel_file_to_json('data.xlsx')

# with open('data.json', 'r') as jf: #jf = json file
#     data_json = json.load(jf)

# arr_data_keys=list(data_json.keys())
new_data_json = deepcopy(data_json)

for product in new_data_json:
    # print(product)
    image_name = './vanilla_images/' + product['imagen'] + '.png'
    product['imagen'] = PhotoImage(file=image_name)
    # new_data_json['barcode'] = key
    List_images.append(product)
    # print(List_images)

# label = Label(image=List_images[0])
canvas.create_image(0,0,image=List_images[0]['imagen'],anchor="nw")

print('clickea para colocar el precio de: ' + List_images[1-1]['nombre'])


# We have to show the the box so this below line is needed
canvas.grid(row=1, column=0, columnspan=3)

# We will have three button back ,forward and exit
button_back = Button(root, text="Back", command=back, state=DISABLED)

# root.quit for closing the app
button_exit = Button(root, text="Exit", command=root.quit)

button_forward = Button(root, text="Forward", command=lambda: forward(1))

# grid function is for placing the buttons in the frame
button_back.grid(row=5, sticky=W)
button_exit.grid(row=5, sticky=W, padx=200)
button_forward.grid(row=5, sticky=W, padx=400)




root.mainloop()