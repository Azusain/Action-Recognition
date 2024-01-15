import os
import re
import torch

# +--------------------------- NTU-RGB+D actions filter ------------------------+ 

# set interested actions here, so this program will output corresponding coco format data
interested_act_idx = [5, 7]  

# get category id from filename
def get_category_idx(file_name):
    return int(re.search("A([0-9]{3})", file_name).group(1))


def is_interested_category(file_name):
    if get_category_idx(file_name) not in interested_act_idx:
        return False
    return True
        
        
# +--------------------------- Read from local file -----------------------------+

def format_to_coco(ntu_list):
    return [
        ntu_list[3],  # nose 
        ntu_list[3],  # left eye
        ntu_list[3],  # right eye
        ntu_list[3],  # left ear
        ntu_list[3],  # right ear
        ntu_list[8],  # left shoulder
        ntu_list[4],  # right shoulder
        ntu_list[9],  # left elbow
        ntu_list[5],  # right elbow
        ntu_list[10], # left wirst
        ntu_list[6],  # right wirst
        ntu_list[16], # left hip
        ntu_list[12], # right hip
        ntu_list[17], # left knee
        ntu_list[13], # right knee
        ntu_list[18], # left ankle
        ntu_list[14]  # right ankle
    ]
     
# format ntu to coco format which only contains 17 2D joints data
def format_single_file(file_path, output_path):
    # read from NTU RGB+D file
    file_in = open(file_path, "r")
    n_frames = int(file_in.readline())
    # read each frame
    file_out = open(output_path, "w")
    file_out.write(f"{n_frames}\n")
    for _ in range(n_frames):
        joints_xyn = []
        n_person = int(file_in.readline())
        if n_person != 1:
            return False
        file_in.readline() # omit body info
        file_in.readline() # omit number of joints which is a constant 25
        for __ in range(25):
            str_xyn = file_in.readline().split(" ")[:2]
            joints_xyn.append( 
                [float(str_xyn[0]), float(str_xyn[1])]
            )
        for joint in format_to_coco(joints_xyn):
            file_out.write(f"{joint[0]} {joint[1]}\n")
    
    file_in.close()
    file_out.close()        
    return True   

def process_ntu_data(dir_name):
    if not os.path.exists(f"{dir_name}/output"):
        os.mkdir(f"{dir_name}/output")
    
    test_list = os.listdir(dir_name)
    
    # nturgb+d_skeletons
    for filename in os.listdir(dir_name):
        if not os.path.isfile(os.path.join(dir_name, filename)):
            continue
        if not is_interested_category(filename):
            continue
        
        format_single_file(
            os.path.join(dir_name, filename), 
            f"{dir_name}/output/{filename}(coco)"
        )
        print(f"save {filename}...")
        

# +-------------------------------- Utils for reading coco-format data --------------------------+ 

# this function can be used in other files
def read_formated_data(file_path):
    frame_joints_data_all = []
    fd = open(file_path, 'r')
    n_frames = int(fd.readline())
    for _ in range(n_frames):
        frame_joints_data = []
        for __ in range(17):
            str_xyns = fd.readline().replace("\n", "").split(" ")
            frame_joints_data.append(
                [float(str_xyns[0]), float(str_xyns[1])]
            )
        frame_joints_data_all.append(frame_joints_data)
    return n_frames, torch.tensor(frame_joints_data_all).view(n_frames, 34)


if __name__ == '__main__':
    process_ntu_data("nturgb+d_skeletons")

    