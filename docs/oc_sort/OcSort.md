### Usage of OcSort

```bash
python track.py
```
#### Track Configurations
```bash
TRACKER_CONFIG:
    # The name of the tracker
    TRACKER_TYPE: OC_SORT
    # The name of the tracker
    CONFIG_PATH: trackerhub/configs/oc_sort.yaml
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

#### OcSort Configurations
```bash
OC_SORT:
  # The name of the sort
  CONF_THRESHOLD: 0.05 
  # The threshold for the confidence score
  IOU_THRESHOLD: 0.3
  # The threshold for the IOU score
  MAX_AGE: 30
  # The maximum age of the track
  MIN_HITS: 3
  # The minimum number of hits for the track
  DELTA_T: 3
  # The time interval between two frames
  ASSO_FUNC: "iou"  # giou, ciou, diou, ct_dist
  # The association function
  INERTIA: 0.2
  # The inertia of the track
  USE_BYTE: False
  # Whether to use byte as the unit of the bounding box
```


#### References
```bibtex
@misc{yolov5-strongsort-osnet-2022,
    title={Real-time multi-camera multi-object tracker using YOLOv5 and StrongSORT with OSNet},
    author={Mikel Broström},
    howpublished = {\url{https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet}},
    year={2022}
}
```
```bibtex
@article{cao2022observation,
  title={Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking},
  author={Cao, Jinkun and Weng, Xinshuo and Khirodkar, Rawal and Pang, Jiangmiao and Kitani, Kris},
  journal={arXiv preprint arXiv:2203.14360},
  year={2022}
}
```
