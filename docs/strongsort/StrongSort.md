### Usage of STRONG_SORT

```bash
python track.py
```
#### Track Configurations
```bash
TRACKER_CONFIG:
    # The name of the tracker
    TRACKER_TYPE: STRONG_SORT
    # The name of the tracker
    CONFIG_PATH: trackerhub/configs/strong_sort.yaml
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

#### STRONG_SORT Configurations
```bash
STRONG_SORT:
  ECC: True              # activate camera motion compensation
  MC_LAMBDA: 0.995       # matching with both appearance (1 - MC_LAMBDA) and motion cost
  EMA_ALPHA: 0.9         # updates  appearance  state in  an exponential moving average manner
  MAX_DIST: 0.2          # The matching threshold. Samples with larger distance are considered an invalid match
  MAX_IOU_DISTANCE: 0.7  # Gating threshold. Associations with cost larger than this value are disregarded.
  MAX_AGE: 30            # Maximum number of missed misses before a track is deleted
  N_INIT: 3              # Number of frames that a track remains in initialization phase
  NN_BUDGET: 100         # Maximum size of the appearance descriptors gallery
```


#### Citations
```bibtex
@article{du2022strongsort,
  title={Strongsort: Make deepsort great again},
  author={Du, Yunhao and Song, Yang and Yang, Bo and Zhao, Yanyun},
  journal={arXiv preprint arXiv:2202.13514},
  year={2022}
}
```
