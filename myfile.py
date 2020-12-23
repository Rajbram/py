import os
location = 'C://Users//Ritur//Desktop//Demo//'
files_in_dir = []

# r=>root, d=>directories, f=>files
for r, d, f in os.walk(location):
   for item in f:
      if '.py' in item:
         files_in_dir.append(os.path.join(r, item))

for item in files_in_dir:
   print("file in dir: ", item)
