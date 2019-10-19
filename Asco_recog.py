#this is scrap text from images.
from PIL import Image
from pytesseract import image_to_string
import pytesseract

def recog():

    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

    img1 = Image.open('test.png')
    #img.show()

    text1 = pytesseract.image_to_string(img1,lang='eng')
    #print("<<<<<<<<>>>>>>>>>>>>>>>>>>")
    data1 = text1[200:600]
    print('Authors  :  ',data1)

    data2 = text1[600:]
    print('Medical Center : ',data2)


    #img2 = Image.open('api/address.jpg')
    #img.show()

    #text2 = pytesseract.image_to_string(img2,lang='eng')
    #print("<<<<<<<<>>>>>>>>>>>>>>>>>>")
    #data2 = text2[14:]
    #print('address_aadhar_no:',data2)

recog()




