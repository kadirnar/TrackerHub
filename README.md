<div align="center">
<h1>
  TrackerHub: Real-time Multi-Object Tracking Library 
</h1>
<h4>
    <img width="500" alt="teaser" src="docs/video/demo.gif">
</h4>
</div>

## <div align="center">Overview</div>
This repo is a real-time multi-object tracking library based on [PyTorch](https://pytorch.org/). Yolov5 is used for object detection and [ByteTrack](https://github.com/ifzhang/ByteTrack) and [OcSort](https://github.com/noahcao/OC_SORT) are used for object tracking. The library is designed to be easy to use and easy to extend. It is also easy to integrate with other object detection and tracking libraries.

| Model  | Description  |
|---|---|
| [ByteTrack](docs/byte_track/ByteTracker.md)  |  ByteTrack: Multi-Object Tracking by Associating Every Detection Box  |
| [OCSort](docs/oc_sort/OcSort.md)  |  Observation-Centric SORT on video Multi-Object Tracking. OC-SORT is simple, online and robust to occlusion/non-linear motion.  | 
### Installation 
```bash
git clone https://github.com/kadirnar/TrackerHub
cd TrackerHub
pip install -r requirements.txt
```
### Code Formatter
```bash
bash scripts/code_format.sh
```
### Citation
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