# picture-clustering

This source code obtains the feature vectors from images and write them in result.csv.


After that you cluster feature vectors by unsupervised clustering (as clustering_example.py).

unsupervised clustering example: SpectralClustering, k-medoids, etc ...


## notice

you need meanfile, modelfile, and networkfile.

I recommend to use Caffe model. 
- meanfile: ilsvrc_2012_mean.npy
- modelfile: caffe_reference_imagenet_model
- networkfile: imagenet_deploy.prototxt.

Please, rewrite there path(line 16 ~ 18).


## files

### input

put the image in the folder './data'.

- ./data/picture_images

### output
- ./result.csv


if you do clustering_example.py,

- ./result

## usage

	python feature.py


and you want to try clustering example.

	python clustering_example.py

