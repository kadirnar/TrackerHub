### Usage of ByteTrack

```bash
python track.py
```
#### Track Configurations
```bash
TRACKER_CONFIG:
    # The name of the tracker
    TRACKER_TYPE: BYTE_TRACK
    # The name of the tracker
    CONFIG_PATH: trackerhub/configs/byte_track.yaml
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

#### ByteTrack Configurations
```bash
BYTE_TRACK:
  # The name of the sort
  TRACK_BUFFER: 25
  # The buffer for the track
  FRAME_RATE: 30
  # The frame rate of the video
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
@article{zhang2022bytetrack,
  title={ByteTrack: Multi-Object Tracking by Associating Every Detection Box},
  author={Zhang, Yifu and Sun, Peize and Jiang, Yi and Yu, Dongdong and Weng, Fucheng and Yuan, Zehuan and Luo, Ping and Liu, Wenyu and Wang, Xinggang},
  booktitle={Proceedings of the European Conference on Computer Vision (ECCV)},
  year={2022}
}
```
