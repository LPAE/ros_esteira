import os
import sys
import glob
import matplotlib.pyplot as plt
import cv2
import dlib

dataset_folder_path = "./dataset/2019-06-26/lowsize/"
svn_path = os.path.join(dataset_folder_path, "detector.svm")
landmarks_path = os.path.join(dataset_folder_path, "landmarks.dat")

detector = dlib.fhog_object_detector(svn_path)

landmarks_detector = dlib.shape_predictor(landmarks_path)

image_name = "robot_1.png"
image_path = os.path.join(dataset_folder_path, image_name)
image = dlib.load_rgb_image(image_path)

[boxes, confidences, detector_idxs] = dlib.fhog_object_detector.run(detector, 
                                                                    image, 
                                                                    upsample_num_times=1, 
                                                                    adjust_threshold=0.0)
for i in range(len(boxes)):
    print("detector {} found box {} with confidence {}.".format(detector_idxs[i], 
                                                                boxes[i], 
                                                                confidences[i]))

def printLandmark(image, landmarks, color):    
    for p in landmarks.parts():
        cv2.circle(image, (p.x, p.y), 20, color, 2)
      
print("...")  
for file in glob.glob(os.path.join(dataset_folder_path, "*.png")):
  
    image = cv2.imread(file)
    
    [boxes, confidences, detector_idxs]  = dlib.fhog_object_detector.run(detector, 
                                                                           image, 
                                                                           upsample_num_times=1, 
                                                                           adjust_threshold=0.0)
    
    for box in boxes:
        e, t, d, b = (int(box.left()), 
                      int(box.top()), 
                      int(box.right()), 
                      int(box.bottom()))
        
        cv2.rectangle(image, (e, t), (d, b), (0, 0, 255), 2)
        
        landmark = landmarks_detector(image, box)
        printLandmark(image, landmark, (255, 0, 0))
        
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.show()
    print(".")

print("...")