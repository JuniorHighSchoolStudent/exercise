import os
import math
import numpy as np
import pandas as pd
import os.path as osp
from tqdm import tqdm

label_warp = {'norm': 0,
              'defect1': 1,
              'defect2': 2,
              'defect3': 3,
              'defect4': 4,
              'defect5': 5,
              'defect6': 6,
              'defect7': 7,
              'defect8': 8,
              'defect9': 9,
              'defect10': 10,
              'defect11': 11,
              }

# train data
data_path = 'data/guangdong_round1_train2_20180916'
img_path, label = [], []

for first_path in os.listdir(data_path):
    first_path = osp.join(data_path, first_path)
    if 'norm' in first_path:
        for img in os.listdir(first_path):
            img_path.append(osp.join(first_path, img))
            label.append('norm')
    else:
        for second_path in os.listdir(first_path):
            defect_label = second_path
            second_path = osp.join(first_path, second_path)
            if defect_label != 'defect11':
                for img in os.listdir(second_path):
                    img_path.append(osp.join(second_path, img))
                    label.append(defect_label)
            else:
                for third_path in os.listdir(second_path):
                    third_path = osp.join(second_path, third_path)
                    if osp.isdir(third_path):
                        for img in os.listdir(third_path):
                            if 'DS_Store' not in img:
                                img_path.append(osp.join(third_path, img))
                                label.append(defect_label)

label_file = pd.DataFrame({'img_path': img_path, 'label': label})
label_file['label'] = label_file['label'].map(label_warp)

label_file.to_csv('data/label.csv', index=False)

# test data
test_data_path = 'data/guangdong_round1_test_a_20180916'
all_test_img = os.listdir(test_data_path)
test_img_path = []

for img in all_test_img:
    if osp.splitext(img)[1] == '.jpg':
        test_img_path.append(osp.join(test_data_path, img))

test_file = pd.DataFrame({'img_path': test_img_path})
test_file.to_csv('data/test.csv', index=False)

print('gen_label_csv done!')
