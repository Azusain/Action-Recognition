from enum import Enum
import torch

PI = 3.1415926535

class SportState(Enum):
    INIT = 0
    READY = 1
    ONGOING = 2    
    DONE = 3
    
class SitupFSM():
    class TypeInput(Enum):
        SITUP_UP = 0
        SITUP_ING = 1
        SITUP_DOWN = 2
    
    state_ = SportState.INIT
    count_ = 0
    angle_ = 0
 
    def transfer(self, _input, pose_results):
        # State INIT
        if SportState.INIT == self.state_:
            if SitupFSM.TypeInput.SITUP_DOWN == _input:
                self.state_ = SportState.READY
        
        # State READY
        elif SportState.READY == self.state_:
            if SitupFSM.TypeInput.SITUP_ING == _input:
                self.state_ = SportState.ONGOING
            elif SitupFSM.TypeInput.SITUP_DOWN != _input:
                self.state_ = SportState.INIT
        
        # State ONGOING
        elif SportState.ONGOING == self.state_:
            if SitupFSM.TypeInput.SITUP_UP == _input:
                last_angle = self.angle_
                self.evaluate(pose_results)
                if last_angle >= self.angle_:
                    self.count_ += 1
                    self.state_ = SportState.INIT
                else:
                    self.state_ = SportState.ONGOING
                
            elif SitupFSM.TypeInput.SITUP_ING != _input:
                self.state_ = SportState.INIT

    def evaluate(self, pose_results):
        keypoints = pose_results[0].keypoints.xyn[0]
        x_delta = keypoints[11][0] - keypoints[5][0]
        y_delta = keypoints[11][1] - keypoints[5][1]

        angle_rad = torch.arctan(y_delta / abs(x_delta))
        if x_delta < 0:
            self.angle_ = PI - angle_rad
        else: 
            self.angle_ = angle_rad
        self.angle_ = self.angle_ * 180 / PI

class HighkneeFSM():
    class TypeInput(Enum):
        HIGHKNEE_LEFT = 3
        HIGHKNEE_RIGHT = 4
        HIGHKNEE_ING = 5

    state_ = SportState.INIT
    count_ = 0
    mean_angle_ = 0.0
    angle_ = 0.0
    
    def transfer(self, _input, pose_results):
        # State INIT
        if SportState.INIT == self.state_:
            if HighkneeFSM.TypeInput.HIGHKNEE_ING == _input:
                self.state_ = SportState.READY
        
        # State READY
        elif SportState.READY == self.state_:
            if HighkneeFSM.TypeInput.HIGHKNEE_LEFT == _input or \
                HighkneeFSM.TypeInput.HIGHKNEE_RIGHT == _input:
                last_score = self.angle_
                self.evaluate(pose_results)
                if self.angle_ <= last_score:
                    self.mean_angle_ = (self.angle_ + self.mean_angle_) / 2
                    self.count_ += 1
                    self.state_ = SportState.INIT
                else: 
                    self.state_ = SportState.READY
            
            elif  HighkneeFSM.TypeInput.HIGHKNEE_ING!= _input:
                self.state_ = SportState.INIT
        
    def evaluate(self, pose_results):
        keypoints = pose_results[0].keypoints.xyn[0]
        y_delta = 0.0
        x_delta = 0.0
        
        if keypoints[13][1] < keypoints[14][1]:
            y_delta = keypoints[13][1] - keypoints[11][1]
            x_delta = abs(keypoints[13][0] - keypoints[11][0])
        else:
            y_delta = keypoints[14][1] - keypoints[12][1]
            x_delta = abs(keypoints[14][0] - keypoints[12][0])

        angle_rad = torch.arctan(x_delta / y_delta).item()
        if angle_rad < 0:
            angle_rad += PI - angle_rad

        self.angle_ = angle_rad * 180 / PI
        

class PushupFSM():
    class TypeInput(Enum):
        PUSHUP_UP = 6
        PUSHUP_ING = 7
        PUSHUP_DOWN = 8
    
    state_ = SportState.INIT
    flatness_ = 0
    angle_ = 0
    count_ = 0
        
    def transfer(self, _input, pose_results):
        # State INIT
        if SportState.INIT == self.state_:
            if PushupFSM.TypeInput.PUSHUP_UP == _input:
                self.state_ = SportState.READY
        
        # State READY
        elif SportState.READY == self.state_:
            if PushupFSM.TypeInput.PUSHUP_ING == _input:
                self.state_ = SportState.ONGOING
            elif PushupFSM.TypeInput.PUSHUP_UP != _input:
                self.state_ = SportState.INIT
        
        # State ONGOING
        elif SportState.ONGOING == self.state_:
            if PushupFSM.TypeInput.PUSHUP_DOWN == _input:
                last_angle = self.angle_
                self.evaluate(pose_results)
                if last_angle >= self.angle_:
                    self.count_ += 1
                    self.state_ = SportState.INIT 
                else:
                    self.state_ = SportState.ONGOING
                
            elif PushupFSM.TypeInput.PUSHUP_ING != _input:
                self.state_ = SportState.INIT        
        
    def evaluate(self, pose_results):
        # flatness
        keypoints = pose_results[0].keypoints.xyn[0]
        y_leg_delta = abs(keypoints[16][1] - keypoints[12][1])
        x_leg_delta = abs(keypoints[16][0] - keypoints[12][0])
        leg_angle = torch.arctan(y_leg_delta / x_leg_delta)
        y_body_delta = abs(keypoints[12][1] - keypoints[6][1])
        x_body_delta = abs(keypoints[12][0] - keypoints[6][0])
        body_angle = torch.arctan(y_body_delta / x_body_delta)
        self.flatness_ = abs(leg_angle - body_angle)
        
        # angle 
        y_delta = keypoints[16][1] - keypoints[6][1]
        x_delta = abs(keypoints[16][0] - keypoints[6][0])
        self.angle_ = torch.arctan(y_delta / x_delta) * 180 / PI
