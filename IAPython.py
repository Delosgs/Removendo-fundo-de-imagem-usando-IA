
# Romovendo o fundo da imagem usando IA com Python na Lib rembg

from rembg import remove
from PIL import Image

entrada_path = './data/delano.jpg'
saida_path = 'out_put_image.png'

entrada = Image.open(entrada_path)
saida = remove(entrada)
saida.save(saida_path)
