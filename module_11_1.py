from PIL import Image
# Изменяем размер изображения с помощью библиотеки pillow

image_path = f'./tiger.jpg'
image = Image.open(image_path)
image = image.resize((600, 850))
image.save(image_path)

import numpy as np
#Создаем массив с помощью библиотеки numpu

arr = np.array([10, 20, 30, 40, 50])
result = arr + 10
print("Массив увеличенный на 10:", result)

import matplotlib.pyplot as plt

#Создадим график (пока просто рандомный) с помощью библиотеки matplotlib и numpy

x = np.linspace(0, 20, 100)
y = np.sin(x)
plt.figure(figsize=(6,6))
plt.plot(x, y, 'b--', label='Sine curve')
plt.title('Plot of Sine Function')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
plt.show()
