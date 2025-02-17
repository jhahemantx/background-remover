from flask import Flask, render_template, Response
import cv2
import os
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
from threading import Lock

app = Flask(__name__)

# Global variables
camera_lock = Lock()
current_index = 0
segmentor = SelfiSegmentation(1)

# Load background images
listImg = os.listdir("Images")
imgList = []
for imgPath in listImg:
    img = cv2.imread(f'Images/{imgPath}')
    imgList.append(img)
n = len(imgList)

def get_frame():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    
    while True:
        success, img = cap.read()
        if not success:
            break
            
        with camera_lock:
            imgOut = segmentor.removeBG(img, imgList[current_index])
            
        # Encode the frame
        ret, buffer = cv2.imencode('.jpg', imgOut)
        frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(get_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/change_background/<direction>')
def change_background(direction):
    global current_index
    
    with camera_lock:
        if direction == 'prev':
            if current_index == 0:
                current_index = n - 1
            else:
                current_index -= 1
        elif direction == 'next':
            if current_index == n - 1:
                current_index = 0
            else:
                current_index += 1
    
    return {'status': 'success', 'index': current_index}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)