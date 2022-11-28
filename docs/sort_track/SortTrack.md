### Usage of SortTrack

```bash
python track.py
```
#### Track Configurations
```bash
TRACKER_CONFIG:
    # The name of the tracker
    TRACKER_TYPE: SORT_TRACK
    # The name of the tracker
    CONFIG_PATH: trackerhub/configs/sort_track.yaml
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

#### SortTrack Configurations
```bash
SORT_TRACK:
  # The name of the sort
  MAX_AGE: 1
  # The maximum number of frames to keep alive a track without associated detections
  MIN_HITS: 3
  # The minimum number of associated detections before track initialization
```


#### References
```bibtex
@inproceedings{Bewley2016_sort,
  author={Bewley, Alex and Ge, Zongyuan and Ott, Lionel and Ramos, Fabio and Upcroft, Ben},
  booktitle={2016 IEEE International Conference on Image Processing (ICIP)},
  title={Simple online and realtime tracking},
  year={2016},
  pages={3464-3468},
  keywords={Benchmark testing;Complexity theory;Detectors;Kalman filters;Target tracking;Visualization;Computer Vision;Data Association;Detection;Multiple Object Tracking},
  doi={10.1109/ICIP.2016.7533003}
}
```