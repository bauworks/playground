from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


#Jupytter notebook の中で表示
#%matplotlib inline

tokyo_tower = Image.open("tokyo_tower.png")
print(type(tokyo_tower))
#plt.imshow(tokyo_tower)

tokyo_tower.show()


tokyo_tower_list = np.asarray(tokyo_tower)
plt.imshow(tokyo_tower_list)
plt.show()



gray_tower = tokyo_tower.convert("L")
plt.imshow(gray_tower)
plt.show()



plt.imshow(gray_tower, cmap="gray")
plt.show()


tokyo_tower_resized = tokyo_tower.resize((250, 375))
plt.imshow(tokyo_tower_resized)
plt.show()



tokyo_tower_rotated = tokyo_tower.rotate(60)
plt.imshow(tokyo_tower_rotated)
plt.show()


tokyo_tower_rotated = tokyo_tower.rotate(60, expand=True)
plt.imshow(tokyo_tower_rotated)
plt.show()


tokyo_tower_translated = tokyo_tower.rotate(0, translate=(100, 100))
plt.imshow(tokyo_tower_translated)
plt.show()
