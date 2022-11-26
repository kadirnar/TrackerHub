import cv2
import numpy as np
from yolov5.utils.plots import colors


def tracker_vis(
    track_id,
    label,
    frame,
    tracker_box,
) -> np.ndarray:
    x, y, w, h = int(tracker_box[0]), int(tracker_box[1]), int(tracker_box[2]), int(tracker_box[3])
    MIN_FONT_SCALE = 0.7
    color = colors(track_id % 10)
    txt_color = (0, 0, 0) if np.mean(color) > 0.5 else (255, 255, 255)
    font_scale = max(MIN_FONT_SCALE, 0.3 * (w + h) / 600)
    thickness = 2
    txt_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)[0]
    cv2.rectangle(frame, (x, y), (w, h), color, thickness)  # object box
    cv2.rectangle(frame, (x, y - txt_size[1]), (x + txt_size[0], y), color, -1)  # object label box
    cv2.putText(
        frame,
        label,
        (x, y - 2),
        cv2.FONT_HERSHEY_SIMPLEX,
        font_scale,
        txt_color,
        thickness,
        cv2.LINE_AA,
    )
