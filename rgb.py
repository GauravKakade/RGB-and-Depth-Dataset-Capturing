import pyrealsense2 as rs
import numpy as np
import cv2
import os
import time


print("Program Started")
time.sleep(4)
PATH = os.getcwd()
output_data_dir = 'front'
folder_for_saving = '55'
# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 5)  # Frame adjustment by changing FPS(here 15)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 5)

# Start streaming
pipeline.start(config)
print("Camera Started")

# 1 starts
frame_num = 0
# Defining the output path
folder_name = os.path.join(PATH, output_data_dir, folder_for_saving) + '/'
print("Saving in Images in:", folder_name)


if not os.path.exists(folder_name):
    os.mkdir(folder_name)

try:
    while True:

        for x in range(5):
            pipeline.wait_for_frames()
            print("Skipping some frames")

        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        if not depth_frame or not color_frame:
            continue

        # Convert images to numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', color_image)
        cv2.waitKey(1)

        # 2 Saving the images
        #base_name = 'img'
        output_file_name = folder_for_saving + '_{:06d}'.format(frame_num) + '.png'
        output_file_path = folder_name + output_file_name
        cv2.imwrite(output_file_path, color_image)  # saving colour  to defined location
        # cv2.imwrite(output_file_path, depth_image) #saving depth images to defined location, but file path needs to be changed
        frame_num += 1

finally:

    # Stop streaming
    pipeline.stop()

