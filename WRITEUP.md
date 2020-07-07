# Project Write-Up

This documents decribe my way around to the first project of Udacity Intel AI Edge Nanodegree Program

To watch the video result please click [here] (https://youtu.be/CsYDw7GpZuA)

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
