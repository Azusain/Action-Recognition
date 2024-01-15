import os
import random

# settings
n_file_total = 164
n_file_to_remove = 100
PROB_REMOVE = n_file_to_remove / n_file_total
idx_to_delete = 1 
dirs = ['val', ]

# main
removed_file_count = 0
for d in dirs:
    for filename in os.listdir(f'{d}/labels'):
        complete_label_path = f'./{d}/labels/{filename}'
        complete_image_path = f'./{d}/images/{filename.replace(".txt", "")}.jpg'
        fd = open(complete_label_path)
        i  = (int)(fd.read(1))
        fd.close()
        if i == idx_to_delete and random.random() <= PROB_REMOVE:
            removed_file_count += 1
            os.remove(complete_label_path)
            os.remove(complete_image_path)
            print(f'remove {complete_image_path}')
        
print(f'remove {removed_file_count} files in total')
