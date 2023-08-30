# This file contains the video data classes
#
# Other modules
import cv2
import imageio

# Modules of ICVT
from ..utility import utils


class VideoReaderMixin:

    def __init__(self):

        # Define logger
        self.logger = utils.log_define()

    def opencv_reader(self, filepath, frame_number):
        frame = None
        try:
            # Read the frame
            cap = cv2.VideoCapture(filepath)
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            success, frame = cap.read()
            cap.release()
        except Exception as e:
            self.logger.warning(f'Unable to read video frame. Video: {filepath}, Exception: {e}')
            success = False
        return success, frame

    def imageio_reader(self, filepath, frame_number):
        frame = None
        try:
            # Open the video file using imageio
            video = imageio.get_reader(filepath)

            # Read the first frame
            frame = video.get_data(frame_number)

        except IndexError:
            original_frame_number = frame_number
            success = False
            self.logger.warning(
                f'IndexError when reading a frame number: {original_frame_number} from file: {filepath}')
            try:

                # Read the frame using open-cv
                success, frame = self.opencv_reader(filepath, original_frame_number)

            except Exception as e:
                self.logger.warning(f'Error occurred when reading the frame using open-cv: {e}')
                pass
            self.logger.warning(f'Attempted reading the frame with open-cv, status: {success}')
            if not success:
                self.logger.warning(f'Scanning for existing frames...')
                video = imageio.get_reader(filepath)
                while not success:
                    try:
                        if frame_number >= 0:
                            frame_number -= 1
                            frame = video.get_data(max(1, frame_number))
                        else:
                            break
                    except:
                        success = False
                    else:
                        self.logger.warning(f'Frame found at index: {frame_number}')
                        success = True
        else:
            # Convert the frame to BGR color space
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            # Reading successful
            success = True

        return success, frame

