# Project Write-Up

This documents decribe my way around to the first project of Udacity Intel AI Edge Nanodegree Program

To watch the video result please click [here] (https://youtu.be/CsYDw7GpZuA)

### Downloading the Model

For this project I have tried three models from the [Tensorflow Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md). The models are:

- [ssd_mobilnet_v1_coco](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2018_01_28.tar.gz)
- [ssd_mobilnet_v2_coco](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz)
- [faster_cnn_inception_v2_coco](http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz)

Download the model using `wget` and extract it using `tar`:

###### For Example:
```
wget http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2018_01_28.tar.gz

tar -xvf sd_mobilenet_v1_coco_2018_01_28.tar.gz
```
### Converting model into Intermediate Representation:

Since this model is not included in the default model zoo. It needs to be converted into an IR using model optimizer. To do this use the following commands going inside the respective model directory that we have just downloaded and extracted.

###### For Example

```
python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model frozen_inference_graph.pb --tensorflow_object_detection_api_pipeline_config pipeline.config --reverse_input_channels --tensorflow_use_custom_operations_config /opt/intel/openvino/deployment_tools/model_optimizer/extensions/front/tf/ssd_v2_support.json
```

Upon successful conversion, something similar output will be displayed:
```
[ SUCCESS ] Generated IR model.
[ SUCCESS ] XML file: /home/workspace/ssd_mobilenet_v2_coco_2018_03_29/./frozen_inference_graph.xml
[ SUCCESS ] BIN file: /home/workspace/ssd_mobilenet_v2_coco_2018_03_29/./frozen_inference_graph.bin
[ SUCCESS ] Total execution time: 60.29 seconds. 
```

## Explaining Custom Layers

Custom layers are layers that are not included in the list of known layers. If your topology contains any layers that are not in the list of known layers, the Model Optimizer classifies them as custom.

The process behind converting custom layers involves the following.

- Generate the Extension Template Files Using the Model Extension Generator
- Using Model Optimizer to Generate IR Files Containing the Custom Layer
- Edit the CPU Extension Template Files
- Execute the Model with the Custom Layer

## Comparing Model Performance

My method(s) to compare models before and after conversion to Intermediate Representations
were...

The major observaation was, although the model detected the personnel quite swtly but it sometimes failed to detect the person who were in idle state.

## Assess Model Use Cases

Some of the potential use cases of the people counter app are...

- Managing vehicle at traffic signal
- counting objects on converyer belt
- Doing head count through walk through gates

## Assess Effects on End User Needs

Lighting, model accuracy, and camera focal length/image size have different effects on a
deployed edge model. The potential effects of each of these are as follows...

- Lighting and camera affects affects the image quality so it only affects the model performance indirectly
- Also the camera angle plays a vital role
