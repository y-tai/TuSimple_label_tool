import numpy as np
import cv2
import os
import json

def add_lines(num):
    img_dir = '{}/{}/{}/'.format(num,num,num)
    des_dir = '{}_anno'.format(num)
    if not os.path.exists(des_dir):
        os.makedirs(des_dir)
    for path in os.listdir(img_dir):
        print(path)
        img_path = os.path.join(img_dir, path)
        img = cv2.imread(img_path)
        h, w = img.shape[:2]
        h, w, c = img.shape
        for i in range(0, h, 10):
            cv2.line(img, (0, i), (w, i), (0,0,255), 1)
        des_path = os.path.join(des_dir, path)
        cv2.imwrite(des_path, img)

add_lines('2047')













