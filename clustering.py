#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import shutil


def result(filenames, labels):
    n_clusters = max(labels)
    for i in xrange(n_clusters + 1):
        if not os.path.exists('./result/' + str(i)):
            os.makedirs('./result/' + str(i))
    for label, txtname in zip(labels, filenames):
        name = txtname[0:txtname.rfind('.')] + '.jpg'
        shutil.copyfile('./data/' + name,
                './result/' + str(label) + '/' + name)
