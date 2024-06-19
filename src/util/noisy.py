import cv2
import numpy as np
import os

# Загрузка изображения
image = cv2.imread("C:/Users/Admin/Desktop/siakod_proj/red.jpg")

# Создание папки для сохранения изображений
output_folder = "noisy_images_1_1"
os.makedirs(output_folder, exist_ok=True)

# Количество итераций
iterations = 10

# Цикл наложения шума
for i in range(iterations):
    # Создание шума
    noise = np.random.normal(0, i, image.shape).astype(np.uint8)

    # Наложение шума на изображение
    noisy_image = cv2.add(image, noise)

    # Сохранение изображения
    output_filename = f"{output_folder}/noisy_image_1_1{i+1}.jpg"
    cv2.imwrite(output_filename, noisy_image)

print("Изображения с шумом сохранены в папку:", output_folder)