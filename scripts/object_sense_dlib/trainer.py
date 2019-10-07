import os
import sys
import glob
import matplotlib.pyplot as plt
import cv2
import dlib



#===============================================================================
print("svn_options ...")
svn_options = dlib.simple_object_detector_training_options()

#-------------------------------------------------------------------------------
# During training stage: This option flip the input image. 
# This helps it get the most value out of the training data.
svn_options.add_left_right_image_flips = True

#-------------------------------------------------------------------------------
# The trainer is a kind of support vector machine and therefore has the usual
# SVM C parameter.  In general, a bigger C encourages it to fit the training
# data better but might lead to overfitting.  You must find the best C value
# empirically by checking how well the trained detector works on a test set of
# images you haven't trained on.  Don't just leave the value set at 5.  Try a
# few different C values and see what works best for your data.
svn_options.C = 5

#-------------------------------------------------------------------------------
# Set how many CPU cores your computer has for the fastest training.
svn_options.num_threads = 3

#-------------------------------------------------------------------------------
# Verbose Mode
svn_options.be_verbose = True

print("ok!")

#===============================================================================
print("path load ...")
dataset_folder_path = "./image_dataset_3"
training_xml_path = os.path.join(dataset_folder_path, "robotArmGripper_imglab_3.xml")
svn_path = os.path.join(dataset_folder_path, "detector.svm")
landmarks_path = os.path.join(dataset_folder_path, "landmarks.dat")

print("ok!")

#===============================================================================
print("training svn ...")
dlib.train_simple_object_detector(training_xml_path, 
                                  svn_path, 
                                  svn_options)

print("ok!")

#===============================================================================
print("training landmarks ...")
landmarks_options = dlib.shape_predictor_training_options()

dlib.train_shape_predictor(training_xml_path, landmarks_path, landmarks_options)

print("ok!")