### Usage of Norfair

```bash
python track.py
```
#### Track Configurations
```bash
TRACKER_CONFIG:
    # The name of the tracker
    TRACKER_TYPE: NORFAIR_TRACK
    # The name of the tracker
    CONFIG_PATH: trackerhub/configs/norfair_track.yaml
    # The path of the config file
 
DETECTOR_CONFIG:
  # The name of the detector
  IOU_TH: 0.05
  # The threshold for the IOU score
  CONF_TH: 0.05
  # The threshold for the confidence score
  IMAGE_SIZE: 640
  # The size of the image
  WEIGHT_PATH: yolov5m6.pt
  # The path of the weight file
  DEVICE: cuda:0
  # The device to run the detector

VIDEO_CONFIG:
  INPUT_PATH: 1.mp4
  # The path of the input video
  OUTPUT_PATH: Results
  # The path of the output video
  SHOW_VIDEO: True
  # Whether to show the video
  SAVE_VIDEO: False
  # Whether to save the video
```

#### Norfair Configurations
```bash
NORFAIR_TRACK:
  DISTANCE_FUNCTION: "frobenius" # mean_manhattan, mean_euclidean, iou, iou_opt
  DISTANCE_THRESHOLD: 500
  HIT_COUNTER_MAX: 15
  INITIALIZATION_DELAY: null
  POINTWISE_HIT_COUNTER_MAX: 4
  DETECTION_THRESHOLD: 0
  PAST_DETECTIONS_LENGTH: 4
  REID_DISTANCE_THRESHOLD: 0
  REID_HIT_COUNTER_MAX: null
```

#### License

Copyright © 2022, [Tryolabs](https://tryolabs.com). Released under the [BSD 3-Clause](https://github.com/tryolabs/norfair/blob/master/LICENSE).