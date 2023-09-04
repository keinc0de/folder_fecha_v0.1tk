import binascii
import base64
import json
from pathlib import Path


# def uno():
#     img = 'folder.png'
#     with open(img, 'rb') as f:
#         contenido = f.read()
#     texto = binascii.hexlify(contenido)
#     return texto

# def dos():
#     img = 'folder.png'
#     with open(img, 'rb') as f:
#         return base64.b64encode(f.read())
    
def imagen_a_64(imagen):
    with open(imagen, 'rb') as f:
        return base64.b64encode(f.read())
    
def img64str_a_img64data(img_str):
    return img_str.decode('utf-8')
    
def json_imgs(lista_imagenes):
    d = {}
    for img in lista_imagenes:
        stem = Path(img).stem
        d[stem] = imagen_a_64(img).decode('utf-8')
    with open('imgs64.json', 'w') as txt:
        json.dump(d, txt, indent=4)

def json_lee():
    mjson = 'imgs64.json'
    with open(mjson) as file:
        return json.load(file)

# json_imgs(['folder24_am.png', 'folder24_ng.png'])
