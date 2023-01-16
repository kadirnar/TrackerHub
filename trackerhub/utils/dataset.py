import glob
import os
from pathlib import Path
import cv2


IMG_FORMATS = ["bmp", "jpg", "jpeg", "png", "tif", "tiff", "dng", "webp", "mpo"]
VID_FORMATS = ["mp4", "mov", "avi", "mkv"]
IMG_FORMATS.extend([f.upper() for f in IMG_FORMATS])
VID_FORMATS.extend([f.upper() for f in VID_FORMATS])


class LoadData:
    def __init__(self, path):
        p = str(Path(path).resolve())  # os-agnostic absolute path
        if os.path.isdir(p):
            files = sorted(glob.glob(os.path.join(p, '**/*.*'), recursive=True))  # dir
        elif os.path.isfile(p):
            files = [p]  # files
        else:
            raise FileNotFoundError(f'Invalid path {p}')
        imgp = [i for i in files if i.split('.')[-1] in IMG_FORMATS]
        vidp = [v for v in files if v.split('.')[-1] in VID_FORMATS]
        self.files = imgp + vidp
        self.nf = len(self.files)
        self.type = 'image'
        if any(vidp):
            self.add_video(vidp[0])  # new video
        else:
            self.cap = None
    @staticmethod
    def checkext(path):
        file_type = 'image' if path.split('.')[-1].lower() in IMG_FORMATS else 'video'
        return file_type
    def __iter__(self):
        self.count = 0
        return self
    def __next__(self):
        if self.count == self.nf:
            raise StopIteration
        path = self.files[self.count]
        if self.checkext(path) == 'video':
            self.type = 'video'
            ret_val, img = self.cap.read()
            while not ret_val:
                self.count += 1
                self.cap.release()
                if self.count == self.nf:  # last video
                    raise StopIteration
                path = self.files[self.count]
                self.add_video(path)
                ret_val, img = self.cap.read()
        else:
            # Read image
            self.count += 1
            img = cv2.imread(path)  # BGR
        return img, path, self.cap
    def add_video(self, path):
        self.frame = 0
        self.cap = cv2.VideoCapture(path)
        self.frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
    def __len__(self):
        return self.nf  # number of files