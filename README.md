<div align="center">
<h1>
  TrackerHub: Real-time Multi-Object Tracking Library 
</h1>
<h4>
    <img width="700" alt="teaser" src="docs/norfair_track/norfair_demo.gif">
</h4>
</div>

This repo is a real-time multi-object tracking library based on [PyTorch](https://pytorch.org/). [Yolov5](https://github.com/ultralytics/yolov5) and [Yolov7](https://github.com/WongKinYiu/yolov7) is used for object detection and [ByteTrack](https://github.com/ifzhang/ByteTrack), [OcSort](https://github.com/noahcao/OC_SORT) [StrongSort](https://github.com/dyhBUPT/StrongSORT) and [NorFair](https://github.com/tryolabs/norfair) are used for object tracking. The library is designed to be easy to use and easy to extend. It is also easy to integrate with other object detection and tracking libraries.


## Installation 
```bash
pip install trackerhub
```

## Usage
```python
from trackerhub.track import track_objects

track_objects("trackerhub/configs/default_config.yaml")
```

## Code Formatter
```bash
bash scripts/code_format.sh
```
## Citation
```bibtex
@article{cao2022observation,
  title={Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking},
  author={Cao, Jinkun and Weng, Xinshuo and Khirodkar, Rawal and Pang, Jiangmiao and Kitani, Kris},
  journal={arXiv preprint arXiv:2203.14360},
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
```bibtex
@article{du2022strongsort,
  title={Strongsort: Make deepsort great again},
  author={Du, Yunhao and Song, Yang and Yang, Bo and Zhao, Yanyun},
  journal={arXiv preprint arXiv:2202.13514},
  year={2022}
}
```
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
```bibtex
@article{wang2022yolov7,
  title={{YOLOv7}: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors},
  author={Wang, Chien-Yao and Bochkovskiy, Alexey and Liao, Hong-Yuan Mark},
  journal={arXiv preprint arXiv:2207.02696},
  year={2022}
}
```
