# picture-clustering

This source code obtains the feature vectors from images and write them in result.csv.


After that you cluster feature vectors by unsupervised clustering (as clustering_example.py).

unsupervised clustering example: SpectralClustering, k-medoids, etc ...


## notice

you need meanfile, modelfile, and networkfile.

I recommend to use Imagenet model in Caffe. 
- meanfile: ilsvrc_2012_mean.npy
- modelfile: caffe_reference_imagenet_model
- networkfile: imagenet_deploy.prototxt.

Please, rewrite there path(line 16 ~ 18).

### How to get there files.

- caffe_reference_imagenet_model
```
wget https://raw.githubusercontent.com/sguada/caffe-public/master/models/get_caffe_reference_imagenet_model.sh
chmod u+x get_caffe_reference_imagenet_model.sh
./get_caffe_reference_imagenet_model.sh
```

- imagenet_deploy.prototxt
```
wget https://raw.githubusercontent.com/aybassiouny/wincaffe-cmake/master/examples/imagenet/imagenet_deploy.prototxt
```
- ilsvrc_2012_mean

	ilsvrc_2012_mean.npy is in
		caffe/python/caffe/imagenet/ilsvrc_2012_mean.npy


### rewrite imagenet_deploy.prototxt

```
line 174: "fc6" -> "fc6wi"  
line 186: "fc6" -> "fc6wi"
```

It shows an example.
```
   
layers {
  name: "fc6"
  type: INNER_PRODUCT
  bottom: "pool5"
  top: "fc6wi"
  blobs_lr: 1
  blobs_lr: 2
  weight_decay: 1
  weight_decay: 0
  inner_product_param {
    num_output: 4096
  }
}
layers {
  name: "relu6"
  type: RELU
  bottom: "fc6wi"
  top: "fc6"
}
layers {
```


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

