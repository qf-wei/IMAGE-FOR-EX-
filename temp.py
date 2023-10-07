import os
import numpy as np
import shutil


image_folder = 'D_face_w'
npy_file = 'D_face_w/std_1.npy'
#npy_file_2 = 'D_anime_man/std_1_2.npy'

output_folder = 'D_face_w_sorted'
os.makedirs(output_folder, exist_ok=True)

all_vectors = np.load(npy_file)
#vector2 = np.load(npy_file_2)
#all_vectors = np.concatenate((vector1, vector2), axis=0) 


image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')] 
image_files.sort()

selected_vectors = []

for idx, image_file in enumerate(image_files):
    index = int(os.path.splitext(image_file)[0])
    vector = all_vectors[index]
    selected_vectors.append(vector)
    new_image_file = f'{idx:04d}.png' 

    old_image_path = os.path.join(image_folder, image_file)
    new_image_path = os.path.join(output_folder, new_image_file)
    shutil.copy(old_image_path, new_image_path)

selected_vectors = np.array(selected_vectors)

print(selected_vectors.shape)
output_npy_file = 'D_face_man_sorted_randered_fixed.npy'
np.save(output_npy_file, selected_vectors)

