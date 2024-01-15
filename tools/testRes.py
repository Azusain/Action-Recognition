
import argparse
# import torch
# from ultralytics import YOLO
# import cv2

from app_utils import draw_text

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', default='situp')
    print('get args...')
    print(parser.parse_args().mode)