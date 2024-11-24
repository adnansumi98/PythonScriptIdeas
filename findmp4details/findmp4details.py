import os
import sys
import cv2

def get_video_duration(file_path):
    """
    Get the duration of the video using OpenCv.
    """
    try:
        video = cv2.VideoCapture(file_path)
        fps = video.get(cv2.CAP_PROP_FPS)
        frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
        duration = frame_count/fps if fps > 0 else 0
        video.release()
        return duration
    except Exception as e:
        print(f"Error getting duration for {file_path}:{e}")
        return None
    
    def format_duration(seconds):
        """
        Format seconds into HH:MM:SS.
        """

        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def main(directory):
        if not os.path.isdir(directory):
            print(f"Invalid directory: {directory}")
            sys.exit(1)
        
        print("File, Duration, Parent")

        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".mp4"):
                    file_path = os.path.join(root, file)
                    parent_dir = os.path.dirname(file_path)
                    duration = get_video_duration(file_path)
                    
                    if duration is not None:
                        formatted_duration = format_duration(duration)
                        print(f"{file}, {formatted_duration}, {parent_dir}")
                        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path-todirectory>")
        sys.exit(1)
        main(sys.argv[1])
             
      
