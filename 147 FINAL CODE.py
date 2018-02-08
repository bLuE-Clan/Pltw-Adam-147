'''
Client #4: Developer 
Functions to help the photoshop workflow ,
will edit any photo that the client would like
with a varity of different ways.
'''

import PIL #Pulls in PIL For later use  
from PIL import ImageFilter  #Pulls in image filters from PIL For later use
from PIL import Image  #Pulls in Image functions from PIL For later use
from PIL import ImageFont  #Pulls in fonts from PIL For later use
import os.path  #Pulls in directory base code For later use
import PIL.ImageDraw  #Pulls in PIL.ImageDraw For later use
import textwrap  #Pulls in textwrap For later use so user can add text
# get_images code adapted from source code provided by PLTW.
def get_images(directory=None): #grabs the directory of the pictures
    if directory == None: # if no directory specified 
        directory = os.getcwd() # Use working directory.
        
    image_list = [] # Puts all of the images into a list
    file_list = [] # puts all of the file names into a list ( used for fonts and folders)
    
    directory_list = os.listdir(directory) # Go to the directory of the pictures
    for entry in directory_list: # for all of the files in the directory
        absolute_filename = os.path.join(directory, entry) # The file name is equal to the file name in the directory
        try:
            image = PIL.Image.open(absolute_filename) # images is set to a image in the directory
            file_list += [entry] # lists all files that are not picture extensions
            image_list += [image] # lists all pictures by name
        except IOError: # if their is an error
            pass # do nothing with errors tying to open non-images
    return image_list, file_list # returns the list of images and files
    


def frame_image(image, wide, r,g,b):
    ''' Frames an image where..
    
        image = Image to frame.
        wide = Thickness of frame.
        r = Red color value of frame.
        g = Green color value of frame.
        b = Blue color value of frame.
        
        *************************************
        * Only works with frame_all_images, *
        * NOT standalone.                   *
        *************************************
        '''
    width, height= image.size # width and height are equal the image size
    frame = PIL.Image.new('RGBA', (width, height), (0,0,0,0)) # makes new image with specified values
    drawing_layer = PIL.ImageDraw.Draw(frame) # draws a frame 
    drawing_layer.rectangle([(width/wide,height/wide), ((width/wide)*(wide-1),(height/wide)*(wide-1))],fill=(127,0,127,255)) # specifications of the frame to be pasted
    result = PIL.Image.new('RGBA', image.size, (r,g,b,255)) # New image with only a frame/ border
    result.paste(image,(0,0),mask=frame) # Make the frame a mask and place ontop of origonal images
    print 'Framing Image...' # prints framing image
    print 'Image',image,'has been framed.' # Prints image (Imamage name) has been framed
    return result #returns a picture with a frambe
    
def frame_all_images(wider, r,g,b, directory=None):
    ''' Frames all images in working directory,
        stores them in a folder called "Framed Images" '''
    directory = os.getcwd() #gets the directory specified or the current working directory
    new_directory = os.path.join(directory, "Framed Images") # sets new_directory to "Framed Images" 
    try: # try command
        os.mkdir(new_directory) # make a new directory named "Framed Images"
    except: # except command
        pass #pass or move on
    images, files = get_images(directory) # gets images from directory
    for n in range(len(images)): # for the number of images 
        fname,ftype = files[n].split('.') # splits the file in the directory into a name and type
        new_image = frame_image(images[n], wider ,r,g,b) # specifications for new image
        new_name = os.path.join(new_directory,fname + ".png") # adds the file type to the name of the new image
        new_image.save(new_name) # saves it as a new image
    print 'Success! All images have been framed!' # prints "Success! All images have been framed!"
    
def tint_image(image, r,g,b):
    ''' Tints an image where..
    
        image = Image to tint.
        r = Red color value of tint.
        g = Green color value of tint.
        b = Blue color value of tint.
        
        *************************************
        * Only works with tint_all_images,  *
        * NOT standalone.                   *
        *************************************
        '''
    result = PIL.Image.new('RGBA', image.size, (r,g,b,105)) # the result is the new image specifications
    image.paste(result,(0,0),result) # paste result
    print 'Tinting Image...' # prints "Tinting Image..."
    print 'Image',image,'has been tinted.' # prints "Image (image name) has been tinted"
    return image # returns image
    
def tint_all_images(r,g,b, directory=None):
    ''' Tints all images in working directory,
        stores them in a folder called  "Tinted Images" '''
    directory = os.getcwd()#gets the directory specified or the current working directory
    new_directory = os.path.join(directory, "Tinted Images")# sets new_directory to "Tinted Images" 
    try:# try command
        os.mkdir(new_directory) # make a new directory named "Framed Images"
    except: # except command
        pass #pass or move on
    images, files = get_images(directory) # gets image from directory
    for n in range(len(images)): # for the number of images
        fname,ftype = files[n].split('.') # splits the file in the directory into a name and type
        new_image = tint_image(images[n], r,g,b) # specification for the new image
        new_name = os.path.join(new_directory,fname + ".png") # adds the file type to the name of the new image
        new_image.save(new_name) # saves it as a new image
    print 'Success! All images have been tinted!' # prints "Success! All images have been tinted!"
    
def blur_image(image, radius):
    ''' Blurs an image where..
    
        image = Image to blur.
        radius = Amount of blur to apply on the image.
        
        *************************************
        * Only works with blur_all_images,  *
        * NOT standalone.                   *
        *************************************
        '''
    blur = image.filter(ImageFilter.GaussianBlur(radius))
    image.paste(blur,(0,0))
    print 'Blurring Image...'
    print 'Image',image,'has been blurred.'
    return image
    
def blur_all_images(radius, directory=None):
    ''' Blurs all images in working directory, 
        stores them in a folder called "Blurred Images" '''
    directory = os.getcwd()
    new_directory = os.path.join(directory, "Blurred Images")
    try:
        os.mkdir(new_directory)
    except:
        pass
    images, files = get_images(directory)
    for n in range(len(images)):
        fname,ftype = files[n].split('.')
        new_image = blur_image(images[n], radius)
        new_name = os.path.join(new_directory,fname + ".png")
        new_image.save(new_name)
    print 'Success! All images have been blurred!'
    
def text_on_image(image, text, size, line, r,g,b):
    ''' Puts text on an image where..
    
        image = Image to apply text to.
        text = Text to place on image.
        size = Font size.
        line_width = Width of each line of text(*)
            - If text goes off of page, make this 
            value larger OR make suze value smaller.
        r = Red color value of text.
        g = Green color value of text.
        b = Blue color value of text.
        
        (*)LEAVE AS DEFAULT (50) - MULTILINE TEXT 
        NOT CURRENTLY SUPPORTED!
        
        ****************************************
        * Only works with text_on_all_images,  *
        * NOT standalone.                      *
        ****************************************
        * NOTE: FONT FILE "Arial.tff" MUST BE  *
        * IN WORKING DIRECTORY!                *
        ****************************************
        '''
    font = ImageFont.truetype("Arial.ttf",size)
    width, height = image.size
    img = Image.new('RGBA', (width,height), (0,0,0,0))
    write = PIL.ImageDraw.Draw(img)
    lines = textwrap.fill(text, width=line_width)
    w,h = font.getsize(lines)
    print w,width,h,height
    write.text((((width-w)/2),((height-h)/2)),lines,(r,g,b),font=font)
    image.paste(img,(0,0),img)
    print 'Image',image,'now has text on it!'
    return image
    
def text_on_all_images(text, size, line_width, r,g,b, directory=None):
    directory = os.getcwd()
    new_directory = os.path.join(directory, "Images With Text")
    try:
        os.mkdir(new_directory)
    except:
        pass
    images, files = get_images(directory)
    for n in range(len(images)):
        fname,ftype = files[n].split('.')
        new_image = text_on_image(images[n], text, size, line_width, r,g,b)
        new_name = os.path.join(new_directory,fname + ".png")
        new_image.save(new_name)
    print 'Success! All images have text on them!'
    
def contour_image(image):
    contour = image.filter(ImageFilter.CONTOUR)
    image.paste(contour,(0,0))
    print 'Applying Contour To Image...'
    print 'Countur applied to image',image,'!'
    return image
    
def contour_all_images(directory=None):
    directory = os.getcwd()
    new_directory = os.path.join(directory, "Contoured Images")
    try:
        os.mkdir(new_directory)
    except:
        pass
    images, files = get_images(directory)
    for n in range(len(images)):
        fname,ftype = files[n].split('.')
        new_image = contour_image(images[n])
        new_name = os.path.join(new_directory,fname + ".png")
        new_image.save(new_name)
    print 'Success! All images have been contoured!'
