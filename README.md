<div align="center">
<h1>
  TrackerHub: Real-time Multi-Object Tracking Library 
</h1>
</div>

This repo is a real-time multi-object tracking library based on [PyTorch](https://pytorch.org/). Yolov5 is used for object detection and [ByteTrack](https://github.com/ifzhang/ByteTrack), [OcSort](https://github.com/noahcao/OC_SORT) and [NorFair](https://github.com/tryolabs/norfair) are used for object tracking. The library is designed to be easy to use and easy to extend. It is also easy to integrate with other object detection and tracking libraries.


### Tracker Algorithms
<table bordercolor="#66b2b2">
  <tr>
    <td width="25%" valign="top">
      <h3>OCSORT </h3>
        <a target="_blank" href="docs/oc_sort">
            <img src="docs/oc_sort/ocsort_demo.gif" width="100%" alt="https://github.com/kadirnar/TrackerHub"/>
        </a>
        <p>Observation-Centric SORT on video Multi-Object Tracking</p>
    </td>
    <td width="25%" valign="top">
      <h3>BYTETRACK </h3>
        <a target="_blank" href="docs/byte_sort">
            <img src="docs/byte_track/bytetrack_demo.gif" width="100%" alt="https://github.com/kadirnar/TrackerHub"/>
        </a>
        <p>Multi-Object Tracking by Associating Every Detection Box</p>
    </td>
    <td width="25%" valign="top">
      <h3>NorFair </h3>
        <a target="_blank" href="docs/norfair_track">
            <img src="docs/norfair_track/norfair_demo.gif" width="100%" alt="https://github.com/kadirnar/TrackerHub"/>
        </a>
        <p>Norfair is a customizable lightweight Python library for real-time multi-object tracking.</p>
    </td>
  </tr>
</table>

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
