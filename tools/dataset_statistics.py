import os

dirs = ['train', 'val', ]
_dict = {}
n_file_total = 0

for d in dirs:
    for filename in os.listdir(f'{d}/labels'):
        n_file_total += 1
        fd = open(f'./{d}/labels/{filename}')
        i  = (int)(fd.read(1))
        val = _dict.get(i)
        if val is None:
            _dict[i] = 1
        else:
            _dict[i] = val + 1
        fd.close()
        
print(_dict)
print(f'{n_file_total} files in total')
