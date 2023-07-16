FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu18.04

# basic pkg-m
RUN apt-get update
RUN apt install -y python3.8 
RUN apt install -y python3-pip

# pytorch
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118


# yolov5 dependencies


# for remote ssh, default passwd: 0000
# RUN apt install -y ssh sed sudo && \
#     sudo echo 'root:0000' | chpasswd && \ 
#     sudo sed -i 's/#PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config
# CMD /etc/init.d/ssh start && tail -f /dev/null


