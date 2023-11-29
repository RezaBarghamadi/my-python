
import os
import imageio

png_dir = 'G:\Python\my-python\Assignment 8\photos'
images = []
for file_name in sorted(os.listdir(png_dir)):
    if file_name.endswith('.jpg'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))

for _ in range(10):
    images.append(imageio.imread(file_path))

imageio.mimsave('G:\Python\my-python\Assignment 8\photos/my.gif', images)