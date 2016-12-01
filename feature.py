#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import itertools
import csv

import numpy as np
import caffe
import cv2


class Feature():

    def __init__(self, flag_separate=False):
        MEAN = '../path/to/mean_file'
        NET = '../path/to/network_file'
        MODEL = '../path/to/model_file'
        self.LAYER = 'fc6wi'
        self.INDEX = 4
        self.feature = []
        self.flag_separate = flag_separate

        self.net = caffe.Classifier(NET, MODEL)
        caffe.set_mode_cpu()
        self.net.transformer.set_mean('data', np.load(MEAN))
        self.net.transformer.set_raw_scale('data', 255)
        self.net.transformer.set_channel_swap('data', (2, 1, 0))

    def input_data(self):
        self.files = os.listdir('./data/')

    def get_featurevextor(self):
        self.input_data()
        for filename in self.files:
            if not self.flag_separate:
                self.feature_extraction(filename)
            else:
                separated_files = self.separate(filename)
                for separated_filename in separated_files:
                    self.feature_extraction(separated_filename)
        self.output_csv()

    def feature_extraction(self, filename, position=0):
        if self.flag_separate:
            print filename + ' is end.'
            image = caffe.io.load_image('./temp/' + filename)
        else:
            image = caffe.io.load_image('./data/' + filename)
        self.net.predict([image])
        feat = self.net.blobs[self.LAYER].data[self.INDEX].flatten().tolist()
        feat.insert(0, filename)
        # if self.flag_separate:
        #    feat.insert(1, position)
        self.feature.append(feat)

    def output_csv(self):
        with open('result.csv', 'wb') as csvfile:
            featwriter = csv.writer(csvfile)
            featwriter.writerows(self.feature)

    @staticmethod
    def separate(filename):
        new_filenames = []
        img = cv2.imread('./data/' + filename)
        height, width = img.shape[:2]
        name = filename[:filename.rfind('.')]
        h = int(height / 4)
        w = int(width / 3)
        if not os.path.isdir('./temp/'):
            os.mkdir('./temp')
        for i, j in itertools.product(xrange(3), xrange(4)):
            new_name = name + '_pos%d.png' % (i * 4 + j)
            cv2.imwrite('./temp/' + new_name,
                    img[h * (j + 1) - int(height / 4):h * (j + 1),
                        w * (i + 1) - int(width / 3):w * (i + 1)])
            new_filenames.append(new_name)
        return new_filenames


if __name__ == '__main__':
    I = Feature(flag_separate=False)
    I.get_featurevextor()
