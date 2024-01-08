import torch
from ultralytics import YOLO
import cv2
import argparse
# project modules
from sports_fsm import PushupFSM, SitupFSM, HighkneeFSM
from app_utils import draw_text

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode')
    parser.add_argument('-s', '--source')
    parser.add_argument('-p', '--pose_model', default='./models/yolov8s-pose.pt')
    parser.add_argument('-d', '--detection_model', default='./models/best.pt')    
    parser.add_argument('-w', '--wait_ms', type=int, default=1)
    args = parser.parse_args()    
    
    # runtime options 
    mode = None
    if args.mode == 'situp':
        mode = SitupFSM
    elif args.mode == 'pushup':
        mode = PushupFSM
    elif mode == 'highknee':
        mode = HighkneeFSM
    else:
        exit(-1)    

    detection_model_path = args.detection_model
    pose_model_path = args.pose_model
    src_video_path = args.source
    # display options
    frame_wait_time_ms = args.wait_ms
    displayed_angle = 0
    score_refresh_frames = 1
    refresh_frames_count = 0
    
    # model initialization
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f'inference device: {device}')
    detection_model = YOLO(detection_model_path)
    pose_model = YOLO(pose_model_path)
    detection_model.to(device)
    pose_model.to(device)

    # setup video stream and FSM 
    fsm = mode()
    sport_classes_dict = {member.value : member for member in fsm.TypeInput}
    cap = cv2.VideoCapture(src_video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_time_sec = float(format(1 / fps, '.4f'))
    frame_cnt = 0
    print(f'video fps: {fps} -> {frame_time_sec}s per frame')

    
    while True:
        success, frame = cap.read()
        if not success:
            break
        frame_cnt += 1
        detection_results = detection_model.predict(frame)
        # check whether there are detected objects 
        _class_id_vec = detection_results[0].boxes.cls
        _class_id = -1
        object_detected = True   
        if _class_id_vec.shape[0] == 0: 
            object_detected = False

        if object_detected:
            _class_id = (int)(_class_id_vec[0].item())
        
            # fsm 
            id_enum_type = sport_classes_dict.get(_class_id)
            if id_enum_type is not None:
                pose_results = pose_model.predict(frame)
                fsm.transfer(id_enum_type, pose_results)
                frame = pose_results[0].plot()
                
        # plot results and display
        if refresh_frames_count % score_refresh_frames == 0:
            displayed_angle = fsm.angle_
            if mode == HighkneeFSM:
                mean_angle_fmt = format(fsm.mean_angle_, '.2f')
                draw_text(frame, f'mean angle: {mean_angle_fmt}' + ' deg', (50, 450))
            elif mode == PushupFSM:
                flatness_fmt = format(fsm.flatness_, '.2f')
                draw_text(frame, f'flatness: {flatness_fmt}', (50, 450))
        refresh_frames_count += 1
        
        draw_text(frame, 'frame id:' + str(frame_cnt), (50, 50))
        draw_text(frame, str(f'count: {fsm.count_}'), (50, 150))
        speed = format(60 * fsm.count_ / (frame_cnt * frame_time_sec), '.2f')
        draw_text(frame, str(f'{speed} (per mins):'), (50, 250))
        draw_text(frame, 'angle: ' + format(displayed_angle, '.2f') + ' deg', (50, 350))

        cv2.imshow(' ', frame)
        cv2.waitKey(frame_wait_time_ms) 
        