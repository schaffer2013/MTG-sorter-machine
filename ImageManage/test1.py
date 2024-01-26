from Scanner import Scanner
from PIL import Image

s = Scanner()
img = Image.open('ImageManage\\cardImages\\jud\\Wormfang Drake.png')
name = s.nameFromImage(img)
a = 1