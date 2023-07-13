FROM pytorch/pytorch:1.10.0-cuda11.0-cudnn8-runtime
COPY ./requirements.txt /
RUN pip install requirements.txt && \
  git clone https://github.com/Azusain/Action-Recognition.git
