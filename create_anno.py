import numpy as np
import cv2
import os
import json

def genmaps(H, W, plist):
    line = np.zeros((H, W), dtype=np.float32)
    mask = np.zeros((H, W), dtype=np.float32)
    for i in range(0, H, 10):
        cv2.line(line, (0, i), (W, i), (255), 1)
    
    for i in range(len(plist)-1):
        cv2.line(mask, (int(plist[i][0]), int(plist[i][1])), 
                        (int(plist[i+1][0]), int(plist[i+1][1]) ), (255), 1)
    
    return mask.astype(int), line.astype(int)

def create_anno(num):
    img_dir = num
    des_dir = '{}_anno'.format(num)
    hs = 10
    json_f = open('{}.json'.format(num), 'w')
    for path in os.listdir(des_dir):
        if not path.endswith('json'): continue
        with open(os.path.join(des_dir, path), 'r') as f:
            data = json.load(f)
        H, W = data['imageHeight'], data['imageWidth']
        lanes = []
        h_sample = np.arange(0, H, 10)
        for dd in data['shapes']:
            plist = np.array(dd['points'])
            mask, line = genmaps(H, W, plist)
            ml = mask & line
            rows, cols = np.nonzero(ml)
            lane = np.ones_like(h_sample) * -2
            lane[rows//10] = cols
            lanes.append(lane.tolist())
        info = {}
        info["lanes"] = lanes
        info["raw_file"] = os.path.join(img_dir, img_dir, img_dir,  path.split('.')[0]+'.png')
        info["h_samples"] = h_sample.tolist()
        json_f.write(json.dumps(info))
        json_f.write('\n')
    
    json_f.close()

create_anno('2047')













