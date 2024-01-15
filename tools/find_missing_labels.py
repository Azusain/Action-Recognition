import os

file_names =  []
cnt = 0


for file_name in os.listdir('allinone_labels/labels'):
    file_names.append(file_name.replace('.txt', ''))
    
for file_name in os.listdir('allinone'):
    if file_name.replace(".jpg", "") not in file_names:
        cnt += 1
        print(f'{file_name.replace(".jpg", "")} is missing')

print(cnt)
    
    

