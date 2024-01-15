import os
import shutil

# setup
ratio_train_test = 4 / 1;
sampling_interval = ratio_train_test + 1
num_images = 1625
path_images = 'allinone'
path_labels = 'allinone_labels'

postfix_images = '.jpg'
postfix_labels = '.txt'
dir_output_images = 'allinone_val'
dir_output_labels = 'allinone_val_labels'

# main 
if not os.path.exists(dir_output_images):
    os.mkdir(dir_output_images)
if not os.path.exists(dir_output_labels):
    os.mkdir(dir_output_labels)

count = 0
for file_name in os.listdir(path_images):
    if count % sampling_interval == 0:
        # move single image
        shutil.move(
            os.path.join(path_images, file_name), 
            os.path.join(dir_output_images, file_name)
        )
        # move single label
        output_label_name = file_name.replace(postfix_images, postfix_labels)
        shutil.move(
            os.path.join(
                path_labels, 
                output_label_name
            ), 
            os.path.join(dir_output_labels, output_label_name)
        )
    count += 1
