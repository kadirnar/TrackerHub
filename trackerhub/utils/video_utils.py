import cv2


def create_video_writer(video_path, output_path, fps=None) -> cv2.VideoWriter:
    """
    This function is used to create video writer.
    Args:
        video_path: video path
        output_path: output path
        fps: fps
    Returns:
        video writer
    """
    from pathlib import Path

    from trackerhub.utils.file_utils import create_dir

    save_dir = create_dir(output_path)
    save_path = str(Path(save_dir) / Path(video_path).name)
    if fps is None:
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)

    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    size = (width, height)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    videoWriter = cv2.VideoWriter(save_path, fourcc, fps, size)
    return videoWriter


def get_video_formats():
    """
    This function is used to get video formats.
    Returns:
        video formats
    """
    extensions = [".asf", ".avi", ".gif", ".m4v", ".mkv", ".mov", ".mp4", ".mpeg", ".mpg", ".ts", ".wmv"]
    video_formats = [x.upper() for x in extensions] + extensions
    return video_formats
