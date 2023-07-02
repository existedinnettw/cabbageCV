

# tutorial 



to learn tensorflow [model](https://github.com/tensorflow/models/tree/master) (tf-model), follow

The implemented tensorflow resource can be split into 2 category, tensorflow hub or tensorflow model.  
Tensorflow hub is something more fixed, simplifing therefore less flexibility. But how flexibility it is is hard to show by value.

## tensorflow model
* [Training experiment framework](https://www.tensorflow.org/tfmodels#training_framework)
  *  [Image classification with Model Garden](https://www.tensorflow.org/tfmodels/vision/image_classification)
     * [ Object detection with Model Garden](https://www.tensorflow.org/tfmodels/vision/object_detection)
* [ How to Train Your Own Object Detector Using TensorFlow Object Detection API ](https://neptune.ai/blog/how-to-train-your-own-object-detector-using-tensorflow-object-detection-api)
  * how someone else dig in tensorflow model.

we focus on reimplement Object detection with Model Garden
### Object detection with Model Garden

tree  
* models
* BCC.v1-bccd.coco
* `expm.py`
* bccd_coco_tfrecords
* 

windows env var, to modify it to tf record.

```powershell
$Env:TRAIN_DATA_DIR='../BCC.v1-bccd.coco/train'
$Env:TRAIN_ANNOTATION_FILE_DIR='../BCC.v1-bccd.coco/train/_annotations.coco.json'
$Env:OUTPUT_TFRECORD_TRAIN='../bccd_coco_tfrecords/train'

python -m official.vision.data.create_coco_tf_record --logtostderr `
  --image_dir=$Env:TRAIN_DATA_DIR `
  --object_annotations_file=$Env:TRAIN_ANNOTATION_FILE_DIR `
  --output_file_prefix=$Env:OUTPUT_TFRECORD_TRAIN `
  --num_shards=1
```
As above, modify `train` to `test` and `valid`.  

```powershell
$Env:VALID_DATA_DIR='../BCC.v1-bccd.coco/valid'
$Env:VALID_ANNOTATION_FILE_DIR='../BCC.v1-bccd.coco/valid/_annotations.coco.json'
$Env:OUTPUT_TFRECORD_VALID='../bccd_coco_tfrecords/valid'

python -m official.vision.data.create_coco_tf_record --logtostderr `
  --image_dir=$Env:VALID_DATA_DIR `
  --object_annotations_file=$Env:VALID_ANNOTATION_FILE_DIR `
  --output_file_prefix=$Env:OUTPUT_TFRECORD_VALID `
  --num_shards=1
```

```powershell
$Env:TEST_DATA_DIR='../BCC.v1-bccd.coco/test'
$Env:TEST_ANNOTATION_FILE_DIR='../BCC.v1-bccd.coco/test/_annotations.coco.json'
$Env:OUTPUT_TFRECORD_TEST='../bccd_coco_tfrecords/test'

python -m official.vision.data.create_coco_tf_record --logtostderr `
  --image_dir=$Env:TEST_DATA_DIR `
  --object_annotations_file=$Env:TEST_ANNOTATION_FILE_DIR `
  --output_file_prefix=$Env:OUTPUT_TFRECORD_TEST `
  --num_shards=1
```



## tensorflow hub
* [ Transfer learning with TensorFlow Hub](https://www.tensorflow.org/tutorials/images/transfer_learning_with_hub)
  * [Attach a classification head](https://www.tensorflow.org/tutorials/images/transfer_learning_with_hub)
  * To do transfer learning, you have to switch head (classification layer).
  * [ Fine tuning models for plant disease detection](https://www.tensorflow.org/hub/tutorials/cropnet_on_device)
    * yet another classification transfer learning example
* [ TensorFlow Hub Object Detection Colab](https://www.tensorflow.org/hub/tutorials/tf2_object_detection)
  * directly get detection from trained model.
  * [Object Detection Made Easy with TensorFlow Hub: Step-by-Step Tutorial](https://learnopencv.com/object-detection-tensorflow-hub/)
* [ Make Object detection models fine-tunable #678 ](https://github.com/tensorflow/hub/issues/678)
  * I think maybe tensorflow hub may not design clearly about detection usage.

