
import os
import glob
import matplotlib.pyplot as plt
import cv2

input_path = "./../"
input_file_type = "*.jpg"

output_path = "./../lowsize/"
output_name = "robot_"
output_file_type = ".png"

search_path = glob.glob(os.path.join(input_path, input_file_type))
                        
#===============================================================================  
file_path_list = []
#using enumerate() the value of n_file_found is increment for each file found in file_path
for n_files_found, file_path in enumerate(search_path):
    file_path_list.append(file_path)
n_files_found = n_files_found + 1
print("{} files found!".format(n_files_found))

#===============================================================================  
image_list = []
for n, file_path in enumerate(file_path_list):
    image_list.append(cv2.imread(file_path))
    image_list[n] = cv2.resize(image_list[n], 
                             (320, 240), 
                             interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(output_path + output_name + str(n) + output_file_type, image_list[n]);
  
#=============================================================================== 
subplot_nrows = int(n_files_found/2)+int(n_files_found%2)
subplot_ncols = 2

fig = plt.figure(figsize=(4,3*subplot_nrows))

ax = [fig.add_subplot(subplot_nrows, 
                      subplot_ncols, 
                      index+1) 
      for index in range(n_files_found)]

for index, image in enumerate(image_list):
    ax[index].imshow(image)
    ax[index].grid(False)
    ax[index].set_xticklabels([])
    ax[index].set_yticklabels([])
    ax[index].set_aspect('auto')
  
fig.subplots_adjust(wspace=0, hspace=0)

plt.show()


