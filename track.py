import os
from pathlib import Path

import cv2

# limit the number of cpus used by high performance libraries
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

from trackerhub.tracker_zoo import create_tracker
from trackerhub.utils.config_utils import get_config
from trackerhub.utils.video_utils import create_video_writer
from trackerhub.utils.track_vis import video_vis
from torchyolo import YoloHub


def load_detector_model(config_path: str) -> object:
    """
    This function is used to load yolov5 model.
    """

    config = get_config(config_path)
    model = YoloHub(
        model_type=config.DETECTOR_CONFIG.DETECTOR_TYPE,
        model_path=config.DETECTOR_CONFIG.WEIGHT_PATH,
        device=config.DETECTOR_CONFIG.DEVICE,
        image_size=config.DETECTOR_CONFIG.IMAGE_SIZE,
    ).load_model()
    model.save = False  
    return model.model


def load_tracker_model(config_path: str) -> object:
    """
    This function is used to track objects in a video using yolov5 and strong sort.
    Args:
        video_path: video path(str)
    """
    config = get_config(config_path)
    tracker_module = create_tracker(
        tracker_type=config.TRACKER_CONFIG.TRACKER_TYPE,
        tracker_weight_path=Path(config.TRACKER_CONFIG.WEIGHT_PATH),
        tracker_config_path=config.TRACKER_CONFIG.CONFIG_PATH,
        device=config.DETECTOR_CONFIG.DEVICE,
        half=config.DETECTOR_CONFIG.HALF,
        conf_th=config.DETECTOR_CONFIG.CONF_TH,
        iou_th=config.DETECTOR_CONFIG.IOU_TH,
    )
    return tracker_module


def track_objects(config_path):
    config = get_config(config_path)
    model = load_detector_model(config_path)
    tracker_module = load_tracker_model(config_path)
    if config.VIDEO_CONFIG.SAVE_VIDEO:
        video_input_path = config.VIDEO_CONFIG.INPUT_PATH
        video_output_path = config.VIDEO_CONFIG.OUTPUT_PATH
        video_writer = create_video_writer(video_input_path, video_output_path)

    video_capture = cv2.VideoCapture(config.VIDEO_CONFIG.INPUT_PATH)
    tracker_outputs = [None]
    while True:
        frame_is_returned, frame = video_capture.read()
        if frame_is_returned:
            prediction_result = model.predict(config.VIDEO_CONFIG.INPUT_PATH)
            for image_id, result in enumerate(prediction_result):
                if config.DETECTOR_CONFIG.DETECTOR_TYPE == 'yolov8':
                    tracker_outputs[image_id] = tracker_module.update(result['det'], frame)
                else:
                    tracker_outputs[image_id] = tracker_module.update(result.cpu(), frame)
                    
                for output in tracker_outputs[image_id]:
                    tracker_box, track_id, track_category_id, tracker_score = (
                        output[:4],
                        int(output[4]),
                        output[5],
                        output[6],
                    )
                    track_category_name = model.model.names[int(track_category_id)]
                    box_labels = f"Id:{track_id} {track_category_name} {float(tracker_score):.2f}"
                    video_vis(
                        track_id=track_id,
                        label=box_labels,
                        frame=frame,
                        tracker_box=tracker_box,
                    )
            if config.VIDEO_CONFIG.SAVE_VIDEO:
                video_writer.write(frame)
            if config.VIDEO_CONFIG.SHOW_VIDEO:
                cv2.imshow("frame", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
        else:
            break
    video_capture.release()


def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(description="Track objects in a video using yolov5 and strong sort.")
    parser.add_argument(
        "--config_path",
        type=str,
        default="trackerhub/configs/default_config.yaml",
        help="path to config file",
    )
    return parser.parse_args()


def run():
    args = parse_arguments()
    track_objects(args.config_path)


if __name__ == "__main__":
    run()
