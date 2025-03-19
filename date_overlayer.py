import re 
from PIL import Image,ImageDraw,ImageFont
import os
#!!!IMPORTANT:this code works only with img form ZZZ-YYYYMMDD-ZZZZ


### Any help or Question welcome to my instagram @FP.ABDOU ###

def extract_date(file_path):
    #extract the image's full name
    file_name = os.path.basename(file_path)
    #extract YYYYMMDD from image name
    date = file_name[4:12]
    #change form
    f_date = f"{date[:4]}-{date[4:6]}-{date[6:]}"
    print(f_date)
    return f_date


def overlay_date(file_path,output_path):
    try:
        image = Image.open(file_path)
     
        text = extract_date(file_path)
        #get the minimum dimention that to relate it to font size
        min_dimention = min(image.width,image.height)
        font_size= max(20,min_dimention // 30)
        try:
            font = ImageFont.truetype('arial.ttf',font_size)
        except:
            font = ImageFont.load_default()
        draw = ImageDraw.Draw(image)
        text_x=10
        text_y=image.height-font_size-10
        shadow_offset =2
        draw.text((text_x+shadow_offset,text_y+shadow_offset),text,font=font,fill="black")
        draw.text((text_x,text_y),text,font=font,fill="white")
        #use it to verify existence of image image.show()
        image.save(output_path,quality=95,subsampling=0) 
        print(image.filename)   
        print("Okay well done !")
    except Exception as e:
        print("ERROR",e)
#to work with any number of image in the folder       
for file_name in os.listdir("IMGS"):
    #verify the format of the image
    if file_name.lower().endswith((".jpg",".png")) and file_name.lower().startswith('img'):
        image_path = os.path.join("IMGS",file_name)
        output_path ="output/"+file_name
        overlay_date(image_path,output_path)
