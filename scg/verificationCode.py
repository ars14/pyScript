import pytesseract
from PIL import Image




#image = Image.open('aaa.GIF')

#code = pytesseract.image_to_string(image)
#print(code)


aaa = pytesseract.image_to_string(Image.open('aaa.PNG'),lang='chi_sim')
print(aaa)
