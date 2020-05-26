from PIL import Image
import matplotlib.pyplot as plt
#%matplotlib inline

tokyo_tower = Image.open("tokyo_tower.png")
print(type(tokyo_tower))
plt.imshow(tokyo_tower)

