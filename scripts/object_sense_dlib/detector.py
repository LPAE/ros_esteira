import os
import sys

import cv2
import dlib

dataset_folder_path = "./image_dataset_3"
svn_path = os.path.join(dataset_folder_path, "detector.svm")
landmarks_path = os.path.join(dataset_folder_path, "landmarks.dat")

detector = dlib.fhog_object_detector(svn_path)
landmarks_detector = dlib.shape_predictor(landmarks_path)

capture = cv2.VideoCapture(2)

def printLandmark(image, landmarks, color):    
    for p in landmarks.parts():
        cv2.circle(image, (p.x, p.y), 20, color, 2)
        
# ====================================================================================================================  
while 1:
    ret, frame = capture.read()

    [boxes, confidences, detector_idxs]  = dlib.fhog_object_detector.run(detector, 
                                                                         frame, 
                                                                         upsample_num_times=0, 
                                                                         adjust_threshold=0.1) 
    for box in boxes:
        e, t, d, b = (int(box.left()), 
                      int(box.top()), 
                      int(box.right()), 
                      int(box.bottom()))
        
        cv2.rectangle(frame, (e, t), (d, b), (0, 0, 255), 2)
        
        landmark = landmarks_detector(frame, box)
        printLandmark(frame, landmark, (255, 0, 0))

    cv2.imshow("Video", frame)

    # ------------------------------------------------------------------------------------------------------------------
    # Esc -> EXIT while
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    # Esc -> EXIT while
    #while 1:
    #  k = cv2.waitKey(1) & 0xff
    #  if k ==13 or k == 27:
    #    break
    #if k == 27:
    #    break
    # ------------------------------------------------------------------------------------------------------------------
# ====================================================================================================================

capture.release()
cv2.destroyAllWindows()