
import matplotlib.pyplot as plt
from PIL import Image

# Cargar imagen desde archivo
img = Image.open("Edgar-Arteaga.jpg")

# Convertir imagen a escala de grises
gray_img = img.convert('L')

# Mostrar imagen original y en escala de grises
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(img)
axs[0].set_title("Imagen original")
axs[1].imshow(gray_img, cmap='gray')
axs[1].set_title("Imagen en escala de grises")
plt.show()
