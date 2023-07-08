


usually, we though yolov6>spinenet>resnet fpn>fasterrcnn  

* [Real-Time Object Detection on COCO](https://paperswithcode.com/sota/real-time-object-detection-on-coco?p=spinenet-learning-scale-permuted-backbone-for)
* [Object detection: speed and accuracy comparison (Faster R-CNN, R-FCN, SSD, FPN, RetinaNet and YOLOv3)](https://jonathan-hui.medium.com/object-detection-speed-and-accuracy-comparison-faster-r-cnn-r-fcn-ssd-and-yolo-5425656ae359)
    * ![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*tOkQQ5g2Tp5xWShaO4VUpQ.jpeg)
* [TensorFlow 2 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)
    * As you can see, larger input image--> higher mAP score.

however, in this experiment. 
fasterrcnn(0.95.8)>spinnet(0.94.1)>resnet fpn(0.87)(0.77)

It's possible, because cabbage are in similar size without stack each other, therefore we don't need feature pyramid to find out data in different size.

Therefore, AP value is highly depend on what your dataset looks.
