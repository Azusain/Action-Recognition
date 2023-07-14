FROM ultralytics/yolov5:latest

# project pkgs
RUN pip install PySide6 

# for remote ssh, default passwd: 0000
RUN apt install -y ssh sed sudo && \
    sudo echo 'root:0000' | chpasswd && \ 
    sudo sed -i 's/#PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config
CMD /etc/init.d/ssh start && tail -f /dev/null


