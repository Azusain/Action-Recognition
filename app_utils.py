import cv2

def draw_text(img, text, pos, fontScale=2.0):
    cv2.putText(img = img, text = text,org = pos, fontFace = cv2.QT_FONT_NORMAL, 
        fontScale = fontScale,  color = (76, 228, 228), thickness = 3)
     